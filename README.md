```markdown
# 📚 FastAPI Books API

A simple FastAPI application to manage books, including CRUD operations (Create, Read, Update, Delete).

## 🚀 Features
- List all books
- Get a book by title
- Filter books by category or author
- Add a new book
- Update an existing book
- Delete a book

## 🛠 Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/)
- Python 3.10+
- Uvicorn (ASGI Server)

## 📂 Project Structure
```bash
fastapi-books/
│
├── app/
│ ├── main.py # FastAPI code
│ ├── init.py
│
├── .gitignore # Ignore unnecessary files
├── requirements.txt # Dependencies list
├── README.md # Project documentatio
```

## 📦 Installation & Running Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/NRKRaj14397/fastapi-books-api.git
cd fastapi-books-api
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*(If you don’t have requirements.txt, run: `pip install fastapi uvicorn`)*

### 4️⃣ Run the FastAPI app

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

### 5️⃣ Explore API Docs

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Example Requests

### Get all books

```bash
curl -X GET "http://127.0.0.1:8000/books" -H "accept: application/json"
```

### Add a new book

```bash
curl -X POST "http://127.0.0.1:8000/books/create_book" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{
  "title": "New Book",
  "author": "John Doe",
  "category": "Programming"
}'
```
