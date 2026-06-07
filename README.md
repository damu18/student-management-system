# Student Management System

A Django-based web application for managing student records, marks, and academic information.

## Features

- ✅ Add, view, update, and delete student records
- ✅ Track student marks and grades
- ✅ User-friendly web interface
- ✅ Responsive design with Bootstrap
- ✅ Django admin panel for management

## Technologies Used

- **Python 3.x**
- **Django 2.7+**
- **SQLite** (Database)
- **HTML/CSS** (Frontend)

## Project Structure

```
student-management-system/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── student/                 # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── user/                    # Main app
    ├── models.py            # Student model
    ├── views.py             # Views and logic
    ├── forms.py             # Django forms
    ├── urls.py              # App URLs
    ├── admin.py             # Admin configuration
    ├── templates/           # HTML templates
    │   └── user/
    │       ├── base.html
    │       ├── student_list.html
    │       ├── student_detail.html
    │       ├── student_form.html
    │       └── student_confirm_delete.html
    └── migrations/          # Database migrations
```

## Installation

### Prerequisites
- Python 3.6+
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/damu18/student-management-system.git
   cd student-management-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to enter username, email, and password.

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Web App: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Usage

### Student Management
- **View Students**: Navigate to the home page to see all students
- **Add Student**: Click "Add Student" button to create a new record
- **View Details**: Click on a student name to see full details
- **Edit Student**: Update student information from the detail page
- **Delete Student**: Remove a student record from the system

### Admin Panel
- Log in to http://127.0.0.1:8000/admin/
- Manage students, marks, and other data
- Create additional user accounts

## Database Schema

### Student Model
- ID (Primary Key)
- Name
- Email
- Phone
- Enrollment Date
- Marks
- Status

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeatureName`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeatureName`)
5. Create a Pull Request

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Issues
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## Future Enhancements

- 📧 Email notifications
- 📊 Grade analytics and reports
- 👥 Role-based access control
- 📱 Mobile app
- 🔐 Two-factor authentication

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on GitHub: [GitHub Issues](https://github.com/damu18/student-management-system/issues)

---

**Created by:** Damu Sreenu  
**Last Updated:** 2026-06-07
