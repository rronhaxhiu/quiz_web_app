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

## Development

The application runs in debug mode by default, which means:
- The server will automatically reload when code changes are detected
- An interactive debugger will appear in the browser if errors occur
- Detailed error messages will be shown

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

