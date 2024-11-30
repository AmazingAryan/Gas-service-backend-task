# Gas Utility Service Request Management System

This project is a web-based service request management system for a gas utility company. It allows staff members to manage customer service requests, track their statuses, and update them. Customers can submit and track their requests through the system.

## Features
- **Customer Dashboard:** Submit and track service requests.
- **Staff Dashboard:** View, update, and manage requests in the assigned city.
- **Status Management:** Requests are marked as `Pending`, `Processing`, or `Resolved`.
- **Authentication:** Secure login/logout functionality.
- **Responsive Design:** Clean and user-friendly interface.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django templates
- **Database:** SQLite (default Django DB) or MongoDB (custom setup)
- **Authentication:** Django's built-in user authentication
- **Deployment:** Locally or on platforms like Heroku/Render

---

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-directory
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   - Staff/Admin Dashboard: `http://127.0.0.1:8000/staff/`
   - Customer Dashboard: `http://127.0.0.1:8000/customer`

---

## Usage

### Customer View
1. Submit service requests.
2. Track the status of submitted requests.

### Staff/Admin View
1. View service requests assigned to your city.
2. Update the status of requests.
3. Manage customer and request data via the Django admin panel.

---

## Folder Structure
```
project-root/
├── core/                  # Core application logic
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── templates/         # HTML templates
├── static/                # CSS, JavaScript, and images
├── db.sqlite3             # SQLite database (default)
├── manage.py              # Django CLI entry point
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## How to Customize

### Color Coding for Status
You can customize the status colors in the CSS file:
```css
.status.pending {
    background-color: #ff4d4d; /* Red for Pending */
}
.status.processing {
    background-color: #ffd633; /* Yellow for Processing */
}
.status.resolved {
    background-color: #4caf50; /* Green for Resolved */
}
```



