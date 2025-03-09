# ☕ Cafe & Wifi API

This repository contains a **Flask-based API** for exploring and managing a list of cafes. Each cafe includes details such as location, seating, WiFi availability, coffee price, and more. 

---

## 📂 Project Files

### 🔹 `main.py`
- Core Flask application.
- Defines routes for **GET, POST, PATCH, and DELETE** operations.
- Connects to the SQLite database (`cafes.db`) using **SQLAlchemy**.
- Implements endpoints such as:
  - `/random` → Returns a random cafe.
  - `/all` → Returns all cafes in JSON format.
  - `/search?loc=YourLocation` → Searches for cafes by location.
  - `/add` → Adds a new cafe (requires form data).
  - `/update-price/<cafe_id>` → Updates the coffee price.
  - `/report-closed/<cafe_id>` → Deletes a cafe from the database.

### 🔹 `requirements.txt`
- Lists all dependencies needed for the project.
- Install dependencies with:
  ```sh
  pip install -r requirements.txt

🔹 index.html
	•	A simple landing page displaying API information.

🔹 contact.html
	•	A placeholder contact page.

🔹 cafes.db
	•	SQLite database storing cafe records with fields such as:
	•	name, map_url, img_url, location, seats, has_wifi, has_toilet, coffee_price, etc.

🔹 styles.css
	•	Contains CSS styles for the web pages.

🔹 Procfile (if present)
	•	Required for deployment on platforms like Render.
	•	Specifies how to start the Flask application using gunicorn.

🔹 .env & .gitignore
	•	.env: Stores environment variables like secret keys.
	•	.gitignore: Excludes unnecessary files from version control.

⸻

🚀 How to Run the API

1️⃣ Clone the Repository

git clone https://github.com/your-username/cafe-api.git
cd cafe-api

2️⃣ Create and Activate a Virtual Environment
	•	Windows:

python -m venv venv
venv\Scripts\activate


	•	Mac/Linux:

python3 -m venv venv
source venv/bin/activate



3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Flask Application

python main.py

	•	By default, the app runs at http://127.0.0.1:5000

⸻

🔥 API Endpoints & Usage

🔹 Get a Random Cafe

Request:

GET /random

Response:

{
  "name": "Cafe XYZ",
  "location": "New York",
  "coffee_price": "$3.50",
  "has_wifi": true
}

🔹 Get All Cafes

Request:

GET /all

Response:

[
  {
    "id": 1,
    "name": "Cafe ABC",
    "location": "Los Angeles",
    "coffee_price": "$4.00"
  },
  {
    "id": 2,
    "name": "Cafe XYZ",
    "location": "New York",
    "coffee_price": "$3.50"
  }
]

🔹 Search Cafes by Location

Request:

GET /search?loc=New York

Response:

{
  "name": "Cafe XYZ",
  "location": "New York",
  "coffee_price": "$3.50"
}

🔹 Add a New Cafe

Request:

POST /add
Content-Type: application/x-www-form-urlencoded

Form Data:

name=Cafe New
map_url=https://maps.google.com/xyz
img_url=https://imageurl.com/cafe.jpg
location=San Francisco
seats=30
has_wifi=True
has_sockets=False
can_take_calls=True
coffee_price=$4.50

Response:

{
  "success": "Cafe added successfully."
}

🔹 Update Coffee Price

Request:

PATCH /update-price/1?new_price=$5.00

Response:

{
  "success": "Coffee price updated."
}

🔹 Delete a Cafe

Request:

DELETE /report-closed/2

Response:

{
  "success": "Cafe deleted successfully."
}



⸻

🛠️ Troubleshooting
	•	Error: email_validator missing?

pip install email_validator


	•	Deployment Issues?
	•	Ensure the Procfile is correctly set (web: gunicorn main:app).
	•	Check that PORT is set in Render/Heroku settings.

⸻

🤝 Contributing
	1.	Fork the repository.
	2.	Create a feature branch (git checkout -b feature-name).
	3.	Commit changes (git commit -m "Add feature").
	4.	Push to the branch (git push origin feature-name).
	5.	Open a pull request.
