# Agency-Website-Blogs

# RMVKY - Full Stack Django Project

RMVKY is a full-stack Django web application showed for empowering success and inspiring growth through various services like website development, mobile development, IT consulting, and app development. The platform allows users to explore these services, read testimonials, check frequently asked questions (FAQ), and read recent blog posts. It also provides a contact form for reaching out to the agency.

## Features
- *Home Page: A welcoming page with a mission statement - *Empowering Success, Inspiring Growth: Your Vision, Our Expertise.
- *Services*: Sections detailing the core services offered: Website Development, Mobile Development, IT Consulting, and App Development.
- *Testimonials*: Feedback from satisfied clients highlighting the agency’s success and service excellence.
- *FAQ*: A frequently asked questions section to assist visitors with common inquiries.
- *Blog*: Recent blog posts covering various topics related to sports and politics.
- *Contact Page*: Contact details including location, email, phone, and working hours, along with a form for users to reach out.

## Project Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django 5.x
- Sqlite3

### Installation

1. *Clone the repository*:
    bash
    git clone https://github.com/Vignesh21J/Agency-Website-Blogs
    

2. *Create a virtual environment*:
    bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    

3. *Install dependencies*:
    bash
    pip install -r requirements.txt
    

4. *Apply migrations*:
    bash
    python manage.py migrate
    

5. *Create a superuser*:
    bash
    python manage.py createsuperuser
    

6. *Run the development server*:
    bash
    python manage.py runserver
    
    Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the app in action.

## Project Structure

```markdown
Full-Agency-Website-Project/
├── manage.py
├── company/
│   ├── _init_.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/
│   ├── _init_.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
└── requirements.txt
