# ☕ Cafe API

## Overview
The **Cafe API** is a RESTful API built using Flask that allows users to manage a database of cafes. Users can **retrieve a random cafe**, **view all cafes**, **search for cafes by location**, **add new cafes**, **update coffee prices**, and **delete cafes**. The API is backed by an SQLite database and supports CRUD operations via HTTP methods.

## 🚀 Features
- **Retrieve a Random Cafe**: Get a randomly selected cafe from the database.
- **View All Cafes**: Fetch a complete list of cafes.
- **Search Cafes by Location**: Look up cafes based on their city or region.
- **Add a New Cafe**: Register a new cafe, including details like name, location, coffee price, and amenities.
- **Update Coffee Prices**: Modify the price of a specific cafe’s coffee.
- **Delete a Cafe**: Remove a cafe entry from the database.

## 🏗 Tech Stack
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Testing & API Client**: Postman
- **Version Control**: Git & GitHub

## 🔧 Setup Instructions

### Prerequisites
- Python (>=3.8)
- Flask
- SQLite

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/PaoloIbanez/files-cafe-api.git
   cd files-cafe-api
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python main.py
   ```
5. The API will be available at:
   ```sh
   http://127.0.0.1:5000/
   ```

## 📌 API Endpoints

| Method | Endpoint             | Description |
|--------|----------------------|-------------|
| GET    | `/random`            | Get a random cafe |
| GET    | `/all`               | Retrieve all cafes |
| GET    | `/search?loc=<city>` | Search for cafes by location |
| POST   | `/add`               | Add a new cafe |
| PATCH  | `/update-price/<id>` | Update a cafe’s coffee price |
| DELETE | `/delete/<id>`       | Remove a cafe from the database |

## 🧪 Example Requests

### ➤ Get All Cafes
```sh
GET http://127.0.0.1:5000/all
```

### ➤ Add a New Cafe
```sh
POST http://127.0.0.1:5000/add
Content-Type: application/json

{
  "name": "Star Coffee",
  "location": "New York",
  "coffee_price": "4.50"
}
```

### ➤ Update Coffee Price
```sh
PATCH http://127.0.0.1:5000/update-price/1
Content-Type: application/json

{
  "new_price": "3.99"
}
```

### ➤ Delete a Cafe
```sh
DELETE http://127.0.0.1:5000/delete/1
```

## 📌 Future Improvements
- Implement **authentication** for managing cafe entries securely.
- Add **rating and review** functionalities for cafes.
- Extend the database to include **WiFi quality, seating availability, and ambiance ratings**.

## 📄 License
This project is open-source and available under the MIT License.

---
Made with ❤️ by **Paolo Ibanez**
