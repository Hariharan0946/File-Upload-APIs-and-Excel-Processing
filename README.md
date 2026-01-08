
# 🚀 Backend File Upload & Excel Processing API

A **production-ready backend system** built using **Django** that allows users to upload Excel files, process records safely, store them in a database, and retrieve them using paginated REST APIs.

This project demonstrates **clean architecture**, **data validation**, **file handling**, and **scalable backend design** — exactly what product companies look for in backend interns.

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-5.x-green?logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/REST-API-orange"/>
  <img src="https://img.shields.io/badge/Postman-Testing-orange?logo=postman"/>
</p>

---
## 🔗 Project Purpose

The goal of this project is to:

- Handle **file uploads securely**
- Parse and validate **Excel / CSV data**
- Prevent **duplicate records**
- Store structured data in a database
- Expose **clean REST APIs**
- Support **pagination for scalability**

This is a **backend-only system** and can be easily integrated with any frontend or mobile application.

---

## 📦 Key Features

✅ Upload Excel (`.xls`, `.xlsx`) and CSV (`.csv`) files  
✅ File type & size validation  
✅ Safe Excel parsing  
✅ Duplicate record prevention  
✅ Database persistence  
✅ Pagination support for large datasets  
✅ Clean API structure  
✅ Production-style folder organization  


---

## 📂 Project Structure
```
backend_assignment/
│
├── backend/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── core/
│ ├── models.py
│ ├── views.py
│ ├── utils.py
│ └── urls.py
│
├── uploads/
├── logs/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions (Run Locally)

### 1️⃣ Clone the repository

```
git clone <repo-url>
cd backend_assignment
```

2️⃣ Create & activate virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

3️⃣ Install dependencies
```
pip install -r requirements.txt
```
4️⃣ Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

5️⃣ Start the server
```
python manage.py runserver
```

📍 Server runs at:

http://127.0.0.1:8000/



---

## 🔌 API Endpoints

### 1️⃣ Upload Excel File
#### Endpoint: POST /api/v1/files/upload

Body: form-data | Key: file (File)

Response:

JSON

{
  "file_path": "uploads/uuid_filename.xlsx"
}



<img width="1555" height="979" alt="image" src="https://github.com/user-attachments/assets/0f81302b-35e2-4a5a-a53f-4430dc3a46ec" />


### 2️⃣ Process Uploaded Excel
#### Endpoint: POST /api/v1/process-excel

Body: x-www-form-urlencoded | Key: file_path

Response:

JSON

{
  "inserted": 2,
  "skipped": 1
}



<img width="1553" height="977" alt="image" src="https://github.com/user-attachments/assets/616ff640-0e40-428f-88ea-badfbc05ea55" />



### 3️⃣ Get Records (With Pagination)
#### Endpoint: GET /api/v1/getAll?page=1&limit=10

Response:

JSON

{
  "page": 1,
  "limit": 10,
  "total": 2,
  "data": [
    {
      "id": 1,
      "excel_id": 5,
      "name": "Ravi",
      "age": 25,
      "education": "Engineering"
    }
  ]
}


<img width="1555" height="979" alt="image" src="https://github.com/user-attachments/assets/013c5275-2729-47f9-879c-1548f55efdaa" />


---
## 🧠 Design Decisions & Architecture
### 🔹 Service Layer Pattern

- Business logic moved to utils.py

- Views remain thin and readable

- Easy to extend and test

### 🔹 Pagination for Scalability

- Prevents memory overload

- Handles large datasets efficiently

- Production-friendly API design

### 🔹 Strict Validation

- File type validation

- File size validation

- Duplicate prevention

- Data integrity checks

### 🔹 Local File Storage

- Files stored locally as required

- Can be upgraded to S3 / Cloud storage easily

## 🧪 Testing

- All APIs tested using Postman
- Invalid file formats handled gracefully
- Duplicate records prevented
- Pagination verified
- Error responses validated

## 👨‍💻 Author
### Hariharan Balasubramaniyam


