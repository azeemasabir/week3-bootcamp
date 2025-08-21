from flask import render_template, request, redirect, url_for
from models import Task, db
import requests, time


# cache for weather
cache = {}
CACHE_TTL = 300   # 5 minutes
API_KEY = "your_api_key_here"   # 👈 replace with your OpenWeatherMap API key


def init_routes(app):
    # ------------------ To-Do List Routes ------------------
    @app.route('/')
    def index():
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)

    @app.route('/add', methods=['POST'])
    def add():
        title = request.form.get('title')
        if title:
            new_task = Task(title=title)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('index'))

    @app.route('/done/<int:task_id>')
    def done(task_id):
        task = Task.query.get_or_404(task_id)
        task.done = True
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/delete/<int:task_id>')
    def delete(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))

    # ------------------ Weather Routes ------------------
    @app.route('/weather', methods=['GET'])
    def weather_form():
        cities = ["London", "New York", "Paris", "Tokyo", "Sydney", "Delhi"]
        return render_template("weather_form.html", cities=cities)

    @app.route('/weather-result', methods=['POST'])
    def weather_result():
        city = request.form.get("city")

        current_time = time.time()
        if city in cache and current_time - cache[city]['time'] < CACHE_TTL:
            weather_data = cache[city]['data']
        else:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code != 200:
                return render_template("weather_result.html", error="City not found!")

            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data['main']['temp'],
                "humidity": data['main']['humidity'],
                "condition": data['weather'][0]['description']
            }
            cache[city] = {"data": weather_data, "time": current_time}

        return render_template("weather_result.html", weather=weather_data)
