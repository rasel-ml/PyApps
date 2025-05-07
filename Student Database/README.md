
## 📘 Student Information System (SIS)

A Python-based command-line application to manage student records. It allows you to add, view, search, edit, and delete student information, storing all data in a text file.


### ✅ Features

- ➕ Add student records with validation  
- 📋 View all students in a sorted table  
- 🔍 Search by ID, name, or department  
- ✏️ Edit any student’s info interactively  
- 🗑️ Delete specific or all student data  
- ⚠️ Logs invalid lines to `error_log.txt`  


### 🧾 File Structure

```
│─ Student_Database.py      # Main Python script
│─ Database.txt             # Stores valid student records
│─ error_log.txt            # Stores invalid or corrupted entries
└─ README.md                # Project documentation
```


### ▶️ How to Run

This program is written in pure Python and **does not require any third-party libraries** — just make sure you have **Python 3.x** installed on your system.

**To run the program:**
```bash
python Student_Database.py
```

### 📸 Screenshot
<img src="https://github.com/rasel-ml/rasel-ml/blob/main/Screenshots/SIS_ss.png" alt="Screenshot" width="100%"></img>

### 🛠️ Function Overview

◽ `loadDatabase()`
- Loads data from `Database.txt`
- Ignores invalid lines (Logged in `error_log.txt`)

◽ `updateDatabase()`
- Writes the current student list back to `Database.txt`

◽ `addStudent()`
- Validates input and adds a new student record

◽ `viewStudent()`
- Displays all student data in a formatted table (Sorted by ID)

◽ `searchStudent()`
- Lets you search by ID, name, or department (Support partial matching)

◽ `editStudent()`
- Allows editing of ID, name, or department

◽ `deleteStudent()`
- Delete one or more students by ID or delete all using `"ALL"`


### 🧪 Sample `Database.txt` Entry

Each line must follow the format: `ID,Name,Department`

```
101,Md. Rasel Molla,Geology & Mining
102,Jannatul Marjan Akhi,Bangla
```

### 👤 Author

Developed by **[Md. Rasel Molla](https://github.com/rasel-ml)**


### 📄 License

This project is open-source and free for educational use.
