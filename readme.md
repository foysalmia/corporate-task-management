<h1 align="center" id="title">Corporate Assets Management</h1>

<p align="center"><img src="https://i.ibb.co/HCmKbwt/Capture.png" alt="project-image"></p>

<p id="description">Simple Django app to track corporate assets such as phones tablets laptops and other gears handed out to employees.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Create Company Profile
*   Add Employees to the Company
*   Create Device and distribute to the employees
*   Device logs by employees
*   User Authentication with JWT
*   Specific HTTP Methods for Admin and other users

<h2>🛠️ Installation Steps:</h2>

<p>1. Create Virtual Env</p>

```
python -m venv venv
```

<p>2. Activate Virtual Env [ Windows ]</p>

```
venv\Scripts\activate
```

<p>3. Install necessary packages</p>

```
pip install -r requirements.txt
```

<p>4. Create a .env file in the root directory and add values</p>

```
SECRET_KEY=
```

```
DEBUG=
```

<p>6. Don't forget to db.sqlite3 for the database</p>

<p>7. Migrate the database</p>

```
python manage.py migrate
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Django
*   Django Rest Framework
*   Djoser
*   Simple JWT