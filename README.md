# Library Book Management System (Django)

## Team Member 1: Kenneth Parrack - Backend Models & Database Setup

---

### What Has Been Completed

- Created the Django app **`library`**.
- Defined and commented all required models in `library/models.py`:
  - **Custom User** model (with `user_type`: admin/member)
  - **Author**
  - **Book**
  - **Loan** (tracks borrowing and returning)
- Registered all models in `library/admin.py` for Django admin management.
- Updated `myproject/settings.py`:
  - Added `'library'` to `INSTALLED_APPS`
  - Set `AUTH_USER_MODEL = 'library.User'`
- Ran initial migrations to set up the database schema.
- Added sample data in `fixtures/sample_data.json` and loaded it into the database.

---

### What’s Next for the Group

- **Frontend/Views:** Build views, templates, or REST APIs for interacting with the models.
- **Testing:** Write unit tests for model logic and relationships.
- **Admin:** Optionally customize Django admin for better usability.
- **Documentation:** Expand this README as new features are added.

---

### Other Notes

- If you change the User model, update `AUTH_USER_MODEL` in `settings.py` before running migrations.
- Use `python manage.py createsuperuser` to create an admin account for the Django admin interface.
- All models are documented with comments and `help_text` for clarity.
- If you encounter migration issues, ensure your database is up to date with `python manage.py migrate`.
- Sample data can be loaded with:  
  ```
  C:\Users\deser\AppData\Local\Programs\Python\Python312\python.exe manage.py loaddata fixtures/sample_data.json
  ```
- I have added as many comments as possible to help with co-op.
- If there are any problems or requests, please let me know and I will do my best to fix them ASAP.

---

## Quick Start

1. **Clone the repository:**
   ```
   git clone https://github.com/Desertiocaine/AppDevProject.git
   cd AppDevProject
   ```

2. **Install dependencies:**
   ```
   pip install django
   ```

3. **Run migrations:**
   ```
   python manage.py migrate
   ```

4. **Load sample data:**
   ```
   python manage.py loaddata fixtures/sample_data.json
   ```

5. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

7. **Access the admin interface:**  
   [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Contact

Kenneth Parrack  
If you have questions or need help, please reach out!