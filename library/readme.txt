Team Member 1: Kenneth Parrack - Backend Models & Database Setup

What has been completed:
------------------------
- Created the Django app `library`.
- Defined and commented all required models in `library/models.py`:
    - Custom User model (with user_type: admin/member)
    - Author
    - Book
    - Loan (tracks borrowing and returning)
- Registered all models in `library/admin.py` for Django admin management.
- Updated `myproject/settings.py`:
    - Added 'library' to INSTALLED_APPS
    - Set AUTH_USER_MODEL = 'library.User'
- Ran initial migrations to set up the database schema.

What’s next for the group:
--------------------------
- (Frontend/Views) Build views, templates, or REST APIs for interacting with the models.
- (Testing) Write unit tests for model logic and relationships.
- (Admin) Optionally customize Django admin for better usability.
- (Documentation) Expand this README as new features are added.

Other notes:
------------
- If you change the User model, update AUTH_USER_MODEL in settings.py before running migrations.
- Use `python manage.py createsuperuser` to create an admin account for the Django admin interface.
- All models are documented with comments and help_text for clarity.
- If you encounter migration issues, ensure your database is up to date with `python manage.py migrate`.
- I really tried to add as many comments as possible to help with co-op.
- If there is anything else, or any problems with this please let me know and I will do my dardest to fix it asap.