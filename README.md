# ☕️ Cafe & Wifi API Project

Welcome to the **Cafe & Wifi API Project**! This is a simple but powerful Flask-based RESTful API that manages data about cafes. You can easily add, update, retrieve, and delete cafe records. Each cafe entry includes useful information like its name, location, wifi availability, coffee prices, seating, and more.

## 📂 Project Structure

Here's what each file in the project does:

- **main.py**:
  - Main Flask app containing all API endpoints.
  - Handles HTTP methods: GET, POST, PATCH, DELETE.

- **requirements.txt**:
  - Contains a list of Python packages used in the project.
  - Use this file to quickly set up your Python environment.

- **cafes.db**:
  - SQLite database holding cafe details.
  - Fields include name, map URL, image URL, location, seating, wifi, sockets, toilets, phone call permissions, and coffee price.

- **index.html / contact.html**:
  - Basic web pages providing project information or contact forms.

- **styles.css**:
  - Contains CSS for basic page styling.

- **Procfile**:
  - Helps deploy the application on services like Heroku or Render.

- **.env**:
  - Used to store environment variables like secret keys.

- **.gitignore**:
  - Specifies files/folders that Git should ignore.

## 🚀 Getting Started

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd cafe-api-project
```

### 2. Create and Activate a Virtual Environment

- **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

- **macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python main.py
```

Your app will now be running at `http://127.0.0.1:5000`

## 📌 API Endpoints

### GET Endpoints
- `/random` – Fetches a random cafe from the database.
- `/all` – Lists all cafes.
- `/search?loc=<location>` – Searches cafes by location.

### POST Endpoint
- `/add` – Adds a new cafe.

### PATCH Endpoint
- `/update-price/<cafe_id>?new_price=$<price>` – Updates the coffee price of a cafe.

### DELETE Endpoint
- `/report-closed/<cafe_id>` – Deletes a cafe.

## 📚 Usage Examples

- **Get Random Cafe:**
  ```
  GET /random
  ```

- **Add Cafe:**
  ```
  POST /add
  name=My Cafe
  map_url=...
  has_wifi=True
  ```

- **Update Coffee Price:**
  ```
  PATCH /update-price/1?new_price=$2.99
  ```

## 🐞 Troubleshooting

- Ensure all dependencies are installed properly.
- If deploying online (e.g., Heroku or Render), ensure a `Procfile` exists with the correct web command, typically:
  ```bash
  web: gunicorn main:app
  ```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork the repo.
- Open issues.
- Submit pull requests.
