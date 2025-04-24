import os
import sqlite3
import shutil
import stat

def remove_readonly(func, path, _):
    """Force delete read-only files on Windows."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

# --- INPUT ---
enrollment = input("Enter Enrollment ID: ")
name = input("Enter Name: ")
folder_path = f"known_faces/{enrollment}_{name}"

# --- DELETE FACE FOLDER ---
if os.path.exists(folder_path):
    try:
        shutil.rmtree(folder_path, onerror=remove_readonly)
        print(f"✅ Deleted folder: {folder_path}")
    except Exception as e:
        print(f"❌ Error deleting folder: {e}")
else:
    print(f"⚠️ Folder not found: {folder_path}")

# --- DELETE FROM STUDENTS.DB ---
try:
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE enrollment = ?", (enrollment,))
    conn.commit()
    conn.close()
    print(f"✅ Deleted '{name}' from students.db")
except Exception as e:
    print("❌ Error deleting from students.db:", e)

# --- DELETE FROM ATTENDANCE.DB ---
try:
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM attendance WHERE enrollment = ?", (enrollment,))
    conn.commit()
    conn.close()
    print(f"✅ Deleted attendance for '{name}' from attendance.db")
except Exception as e:
    print("⚠️ Error deleting from attendance.db (if not found, ignore):", e)
