# Week 3 Bootcamp: Web Development & APIs

Welcome to the **Week 3 Bootcamp** repository!  This week’s focus is on building **web applications**, designing **RESTful APIs**, and optimizing performance using **caching**—all powered by Python and Flask.

---

## 🎯 Project Objectives

By the end of this week, you'll be able to:

* Build a basic Flask web application.
* Develop REST APIs and consume third-party APIs.
* Implement simple yet effective **caching** to enhance responsiveness.

---

## 📚 Learning Outcomes

| What You’ll Learn  | Description                                                                    |
| ------------------ | ------------------------------------------------------------------------------ |
| Flask Web App      | Build a **To‑Do List** with full CRUD support.                                 |
| SQLite Integration | Persist To‑Do data using a lightweight SQLite database.                        |
| REST API           | Create `/weather/<city>` endpoint that returns real-time weather data as JSON. |
| API Consumption    | Fetch and process data from external services (OpenWeatherMap).                |
| Caching            | Reduce redundant external API calls using dictionary/Redis-based caching.      |

---

## 📝 Assigned Tasks & Deliverables

### 1. **Flask To‑Do App**

* Users can **Create**, **Read**, **Update**, and **Delete** to-do items.
* Store to-dos in **SQLite** for persistence.
* Include a feature to **mark tasks as done**.

### 2. **Weather REST API Endpoint**

* Endpoint: `GET /weather/<city>`
* Retrieves weather data from **OpenWeatherMap API** (requires API key).
* Returns JSON:

  ```json
  {
    "city": "CityName",
    "temperature": 25.4,
    "humidity": 68,
    "condition": "Cloudy"
  }
  ```

### 3. **Caching Mechanism**

* Store weather responses in memory using a **dictionary** or using **Redis**.
* Return cached data when available to cut down on API requests.

---

## ⚙️ Setup & Running the Project

### Prerequisites

* **Python 3.x**
* **Flask**
* **Requests**
* **Redis** (optional, for Redis-based caching)

### Installation

```bash
git clone https://github.com/azeemasabir/week3-bootcamp.git
cd week3-bootcamp
pip install flask requests redis  # If using Redis
```

### Configuration

* **OpenWeatherMap API Key**: Set as an environment variable:

  ```bash
  export OWM_API_KEY="your_api_key_here"
  ```

### Running the App

```bash
# Start the Flask server
python app.py
```

* **To-Do Application**: Visit `http://localhost:5000/` to manage your tasks.
* **To-Do API (optional)**: If implemented, use `GET /todos`, `POST /todos`, etc.
* **Weather API**: Access via `http://localhost:5000/weather/Lahore` (or any other city name).

---

## 🔍 Example Usage

| Action        | Endpoint               | Description                                         |
| ------------- | ---------------------- | --------------------------------------------------- |
| Create a task | `POST /todos`          | Add a new to-do with title/description.             |
| Mark as done  | `PUT /todos/<id>/done` | Mark a specific to-do item as completed.            |
| View tasks    | `GET /todos`           | List all current to-dos.                            |
| Get weather   | `GET /weather/Lahore`  | Get live weather data for Lahore (caching enabled). |

```bash
curl http://localhost:5000/weather/Lahore
```

---

## 🧪 Testing & Verification

* Run any included unit tests with:

  ```bash
  pytest
  ```
* Manually test key features via your browser or tools like `curl` or Postman.

---

## 🎓 Goals Recap

* **Web App Development**: Use Flask to build interactive, RESTful web services.
* **Database Persistence**: Store and manage data using SQLite.
* **Third-Party API Integration**: Fetch external data via HTTP requests.
* **Performance Optimization**: Implement efficient caching to improve API responsiveness.

---

## 🤝 Contributing

Contributions are always welcome! Feel free to fork this repository, suggest improvements, or submit pull requests.

