# Corporate Asset Tracking App
<p>The Corporate Asset Tracking App is a web-based application built using the Django 
framework that allows companies to track their corporate assets, such as phones, tablets, 
laptops, and other gear, that are handed out to employees.</p>

<h3>Features</h3>
<li>Companies can add all or some of their employees to the system.</li>
<li>Each company and its staff can delegate one or more devices to employees for a certain period of time.</li>
<li>Each device has a log of its check-out and return dates, as well as its condition at the time of check-out and return.</li>
<li>The system provides a RESTful API for creating, reading, updating, and deleting records for each entity in the database schema.</li>
<li>The web-based user interface allows companies and their employees to view and interact with the device tracking system.</li>
<li>Comprehensive tests have been written for each component of the system, including the database models, REST API, and user interface.</li>

<h3>Installation</h3>
 <li>Clone the repository:</li>
    git bash command: git clone https://github.com/your-username/corporate-asset-tracking.git
 <li>Create a virtual environment:</li>
    cmd command: python -m venv env
 <li>Activate the virtual environment:</li>
    cmd command: ./env/bin/activate
  <li> Install the dependencies:</li>
      cmd command: pip install -r requirements.txt
  <li> Go project directory </li>
      cmd command: cd demo_file
  <li>Create the database:</li>
    cmd command: python manage.py migrate
  <li> Run the development server:</li>
    cmd commad: python manage.py runserver
<h3>Usage</h3>
<p> To use the Corporate Asset Tracking App, open your web browser and navigate to 
http://localhost:8000. You can log in using your company account or your employee 
account. Once logged in, you can view and manage your company's devices and assign them to your employees.</p>
