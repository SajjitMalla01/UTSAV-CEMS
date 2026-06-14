# UTSAV - College Event Management System

## About
UTSAV is a multitenant SaaS platform designed to help colleges manage their events efficiently. The core idea is that multiple colleges can use the same application deployment, but each college gets completely isolated data. It handles everything from event creation and approval workflows to ticketing and analytics.

## Features
- **Multitenancy Architecture:** Uses custom middleware for subdomain and URL path routing to keep data completely separate between colleges.
- **Event Approval Workflow:** Events follow a structured lifecycle (Pending → Approved → Published) to maintain quality control.
- **Secure Registrations:** QR code ticket generation for smooth check-ins at the venue.
- **Verification:** Built-in OTP email verification to ensure valid users.
- **Event Management:** Real-time capacity tracking so events don't overbook.
- **Data & Insights:** Analytics dashboard with visual charts and easy CSV participant export.
- **Social Sharing:** Quick WhatsApp event sharing integration.

## User Roles
The system is built around three main user roles with distinct permissions:
- **Student:** Can browse published events, register for them, and view their generated QR code tickets.
- **Staff:** Can create event proposals, manage their own events, and scan QR codes for check-ins.
- **Admin:** Manages the entire college portal, approves/rejects event proposals, and has access to full analytics and participant exports.

## Tech Stack
- **Backend:** Python, Django
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS, JavaScript, Tailwind CSS
- **Libraries/Integrations:** Chart.js (Analytics), QRCode.js (Ticketing), FullCalendar.js (Event Calendars)

## How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/utsav.git
   cd utsav
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional but recommended)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.0:8000` in your web browser to view the application.

## Screenshots

*(Add screenshots of your application here)*

- **Admin Dashboard**
  ![Admin Dashboard](docs/images/placeholder-dashboard.png)

- **Event Registration Page**
  ![Event Registration](docs/images/placeholder-registration.png)

- **QR Ticket Scanner**
  ![QR Ticket Scanner](docs/images/placeholder-scanner.png)
