<h1 align='center' style='text-decoration:underline'>EduFlash</h1>
<h3>Project Name:</h3> <p style='color:blue'><em>Educational Flashcard App (EduFlash)</em></p>

Tagline: Active Learning Through AI-Powered Flashcards

### Team (Contributors):

<a href="https://github.com/Samfrodo9">Adeyemi Samuel</a>
<br>
<a href="https://github.com/De-Chetachi/">Onyenze Chetachi Divine</a>
<br>
<a href="https://github.com/Mimifresh/">Chukwu Miracle</a>


### Description:

EduFlash is a web application that uses AI to help users learn more effectively. Users can paste text directly into the app, and EduFlash will analyze the text and automatically generate flashcards highlighting the key points. This saves time and effort compared to manually creating flashcards.

### Technologies:

*Frontend:* HTML, CSS and Javascript

*Backend:* Django



### Features:

*AI-powered text summarization:* Automatically generate flashcards from lengthy texts.
*Focus on factual information:* Prioritizes extracting factual information, minimizing risks associated with subjective interpretations.
*User-friendly interface:* Easy to use and navigate.
*Multiple learning modes:* Choose from different flashcard viewing options for optimal learning.
*Accessibility:* Web-based solution accessible on various devices and browsers.

### Target Audience:

1. Students preparing for exams or tests
2. Teachers seeking efficient study materials
3. Anyone interested in active learning and self-assessment
Benefits:

### Future Development:

* Integration with external data sources (e.g., educational articles, research papers)
* Mobile app development
* Advanced learning features like spaced repetition algorithms
* Text-to-speech functionality for accessibility

### Getting Started:
#### Prerequisites
- Virtual Env
- Django
- MySQL

#### Installation
1. Clone the repository: git clone <repository_url>
2. Set up a Virtual Environment: python -m venv virtual_env; source virtual_env/bin/activate
3. Install dependencies: pip install Django
4. Set up database
4. Run the server: python3 manage.py runserver

The server will start on port 8000 by default. You can change the port if neccesary.

#### Database Setup
Create a MySQL database with the following credentials:

	Database name: eduflash
	Username: edu_dev
	Password: edu_pass
	Host: Localhost

Ensure that your MySQL server is running, and update the database configuration in .env with your database credentials.


#### API Endpoints
POST /sign_up: Create a new user
POST log_in: Log a user in
POST /log_out: Log a user out
POST profile/<int:pk>: Get a User profile
POST upload_resource: Upload a resource
GET /get_resource/id/create_flashcards: Create and view Flashcards created from a resorce
GET /get_resource/<int:fk>/view_flashcards: View all flashcards from a particular resource
PATCH update_resource/<int:pk>: Delete and Update a resource
DELETE delete_resource/<int:pk>: Delete a particular resource