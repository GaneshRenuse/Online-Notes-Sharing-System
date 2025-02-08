# 📝 Online Notes Sharing System

An **Online Notes Sharing System** built using Python, Django, and MySQL, allowing users to upload, share, and manage notes efficiently.

## 🛠 Tech Stack

- **Language Used:** Python  
- **Framework Used:** Django  
- **Database:** MySQL  
- **User Interface:** HTML, AJAX, jQuery, JavaScript  
- **Compatible Browsers:** Mozilla Firefox, Google Chrome, IE8, Opera  
- **IDE Used:** PyCharm  

## ✨ Features

- **User authentication** (Students).
- **Upload, download, and manage notes** securely.
- **Categorized note organization** for easy access.
- **Search functionality** to quickly find notes.
- **Interactive dashboard** for a seamless user experience.

## 📂 Project Setup

### 1️⃣ Prerequisites
- Install **Python 3.x** and **MySQL**.
- Install **Django framework** and required dependencies:
  ```bash
  pip install django mysqlclient
  ```

### 2️⃣ Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/GaneshRenuse/online-notes-sharing.git
   ```
2. Navigate to the project directory:
   ```bash
   cd online-notes-sharing
   ```
3. Configure the **database settings** in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'notes_db',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the system in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## 📸 Screenshots  
(Add screenshots here)

## 🔒 Login Credentials (Sample)
| Role  | Username | Password |
|--------|------------|------------|
| User | user1 | u123 |

## 🏗 Future Enhancements
- Integration of **file preview functionality**.
- Implementing **email notifications** for new notes.
- Adding **discussion forums** for collaboration.

## 🤝 Contributing
Contributions are welcome! Fork the repo, create a branch, and submit a pull request.

## 📜 License
This project is licensed under the **MIT License**.

---  
