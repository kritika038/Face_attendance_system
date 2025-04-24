
# Face Recognition Attendance System

This is a complete real-time face recognition-based attendance system built using Python, OpenCV, Flask, and SQLite. It allows students to register using their facial data and records attendance automatically via webcam. The system supports both desktop-based attendance recording and a web-based dashboard for tracking and managing data.

---

## 👩‍💻 Developed by

**Kritika Bansal**  
B.Tech CSE (AI & ML), Bennett University

---

## ✅ Features

- Real-time face detection and recognition
- Student registration with name and enrollment ID (e.g., `123_kritika`)
- Face image saving under `known_faces/` directory
- Attendance recorded with timestamp and enrollment
- Flask-based web dashboard with:
  - Date filtering using calendar
  - Attendance percentage
  - Holiday recognition (Sat/Sun and special days)
  - Search by name or enrollment
  - 'No data found' if no records
- Clean and modern HTML dashboard
- Manual control for adding/removing students
- Uses `students.db` and `attendance.db` for persistent data

---

## 🗂️ Folder Structure

```
face_attendance_system/
├── known_faces/             # e.g., 123_kritika/
├── templates/
│   ├── index.html           # Web form for name/enrollment
│   └── dashboard.html       # Attendance calendar + stats
├── static/css/style.css     # Styling for web UI
├── students.db              # Student info (name + enrollment)
├── attendance.db            # Attendance logs
├── app.py                   # Flask dashboard backend
├── add_student.py           # Register new student + capture face
├── desktop_attendance.py    # Run webcam for marking attendance
├── requirements.txt         # Project dependencies
└── README.md                # You are here!
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/kritika038/face-attendance-system.git
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   cd C:\Users\DELL\OneDrive\Desktop\face_attendance_system
   python -m venv venv
   .\venv\Scripts\Activate
  
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage Guide

### 1. Register a Student (Face + Enrollment)
```bash
python add_student.py
```
- Enter full name and enrollment ID (`e.g., 123_kritika`)
- Face images will be saved inside `known_faces/123_kritika/`

### 2. Mark Attendance (Desktop Webcam)
```bash
python desktop_attendance.py
```
- When face is recognized:
  - Name and “Attendance Recorded” appear
  - Data is saved in `attendance.db`

### 3. View Attendance Dashboard (Web)
```bash
python app.py
```
- Go to `http://localhost:5000`
- Use calendar to select a date
- Search by name or enrollment
- See attendance % based on total scanned dates
- Holidays are auto-marked on weekends/special days
- If no data found, proper message displayed

---
## 4. To delete any student detail
 Remove-Item .\known_faces\E23CSEU2321_AMRIT -Recurse -Force

## 🗄️ Database Schema

**students.db**
| Column     | Type    |
|------------|---------|
| id         | INTEGER |
| enrollment | TEXT    |
| name       | TEXT    |

**attendance.db**
| Column     | Type    |
|------------|---------|
| id         | INTEGER |
| enrollment | TEXT    |
| name       | TEXT    |
| date       | TEXT    |
| time       | TEXT    |

---

## 📊 Attendance Percentage Logic

- Calculated as:  
  `(Days Present / Total Attendance Days) * 100`
- Only includes known students in `known_faces/`

---

## 📅 Holidays

- Weekends (Saturday & Sunday)
- Can be extended with custom dates in code
- No attendance expected on holidays — shows 'Holiday' only

---

## 🧪 Testing & Validation

- Register at least 2 students
- Simulate absence by skipping webcam detection
- Validate dashboard for:
  - Date filtering
  - 'No data found'
  - Percentage accuracy

---

## ⚙️ Technologies Used

- Python 3
- OpenCV
- face_recognition (Dlib)
- Flask
- SQLite
- HTML/CSS (for dashboard UI)

---

## 📦 Future Enhancements

- Admin login system
- Export to Excel / PDF
- Email alerts for absentees
- Attendance summary charts
- Web-based face scan via webcam

---


