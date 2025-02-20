# Operating Systems Quiz App

A web application built with Flask for study purposes.

Author: Rron Haxhiu

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/study_web_app.git
   cd study_web_app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated

2. Run the Flask application:
   ```bash
   python app.py
   ```

   The application will run in debug mode as specified in:
```python:app.py
startLine: 156
endLine: 157
```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Quiz Management

The application allows you to manage quiz questions through the `quiz.json` file:
- Add new questions with multiple choice answers
- Modify existing questions and their answers
- Delete questions that are no longer needed
- All changes are saved automatically

## Project Structure

- `/venv`: Virtual environment directory (excluded from git)
- `app.py`: Main application file containing Flask routes and configurations
- `requirements.txt`: List of Python dependencies

## Dependencies

The project uses the following main dependencies:

- Flask 3.1.0: A lightweight WSGI web application framework
- Werkzeug 3.1.3: A comprehensive WSGI web application library
- Jinja2: A modern and designer-friendly templating language for Python
- Additional dependencies are listed in requirements.txt

## Development

The application runs in debug mode by default, which means:
- The server will automatically reload when code changes are detected
- An interactive debugger will appear in the browser if errors occur
- Detailed error messages will be shown

## Notes

- This is a development server and should not be used in production
- The application uses Flask's built-in server which is suitable for development but not for production deployment
- For production deployment, consider using production-grade servers like Gunicorn or uWSGI

## License

[Add your license information here]

