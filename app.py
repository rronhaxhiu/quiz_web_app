from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime
import random

app = Flask(__name__)

# Load questions from quiz.json
def load_questions():
    with open('quiz.json', 'r') as f:
        questions = json.load(f)['questions']
        for question in questions:
            options = question['options']
            random.shuffle(options)
        return questions

# Load or create scores.json
def load_scores():
    try:
        with open('scores.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Load or create question_stats.json
def load_stats():
    try:
        with open('question_stats.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"questions": {}}

def save_stats(stats):
    with open('question_stats.json', 'w') as f:
        json.dump(stats, f, indent=4)

# Save scores to scores.json
def save_score(correct_answers):
    scores = load_scores()
    score_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": correct_answers,
        "total": 10
    }
    scores.append(score_entry)
    with open('scores.json', 'w') as f:
        json.dump(scores, f, indent=4)

def update_question_stats(question, is_correct):
    stats = load_stats()
    
    # Use question text as key
    q_key = question['question']
    
    if q_key not in stats['questions']:
        stats['questions'][q_key] = {
            'times_seen': 0,
            'times_correct': 0,
            'last_seen': None,
            'mastered': False
        }
    
    stats['questions'][q_key]['times_seen'] += 1
    if is_correct:
        stats['questions'][q_key]['times_correct'] += 1
    stats['questions'][q_key]['last_seen'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Consider a question mastered if answered correctly at least 3 times with >80% success rate
    times_seen = stats['questions'][q_key]['times_seen']
    times_correct = stats['questions'][q_key]['times_correct']
    if times_seen >= 3 and (times_correct / times_seen) >= 0.8:
        stats['questions'][q_key]['mastered'] = True
    
    save_stats(stats)

@app.route('/')
def index():
    questions = load_questions()
    stats = load_stats()
    
    # Add statistics to each question
    for q in questions:
        q_stats = stats['questions'].get(q['question'], {
            'times_seen': 0,
            'times_correct': 0,
            'mastered': False
        })
        q['stats'] = q_stats
    
    # Prioritize unmastered questions in selection
    unmastered = [q for q in questions if not q['stats']['mastered']]
    mastered = [q for q in questions if q['stats']['mastered']]
    
    # Select questions prioritizing unmastered ones
    selected_questions = []
    if len(unmastered) >= 10:
        selected_questions = random.sample(unmastered, 10)
    else:
        selected_questions = unmastered + random.sample(mastered, 10 - len(unmastered))
    
    return render_template('quiz.html', questions=selected_questions)

@app.route('/submit', methods=['POST'])
def submit():
    correct_answers = 0
    questions = []
    
    for i in range(10):
        question = {
            'question': request.form.get(f'question_text_{i}'),
            'options': request.form.getlist(f'options_{i}[]'),
            'correct_answer': request.form.get(f'correct_{i}'),
            'user_answer': request.form.get(f'question_{i}'),
            'explanation': request.form.get(f'explanation_{i}')
        }
        is_correct = question['user_answer'] == question['correct_answer']
        if is_correct:
            correct_answers += 1
        
        # Update statistics for this question
        update_question_stats(question, is_correct)
        questions.append(question)

    return render_template('result.html', score=correct_answers, total=10, questions=questions)

@app.route('/stats')
def stats():
    stats = load_stats()
    questions = load_questions()
    
    # Combine question text with stats
    questions_with_stats = []
    for q in questions:
        q_stats = stats['questions'].get(q['question'], {
            'times_seen': 0,
            'times_correct': 0,
            'last_seen': None,
            'mastered': False  # Make sure this is a boolean
        })
        
        # Ensure mastered is a boolean
        if isinstance(q_stats.get('mastered'), str):
            q_stats['mastered'] = q_stats['mastered'].lower() == 'true'
        
        questions_with_stats.append({
            'question': q['question'],
            'stats': q_stats
        })
    
    # Debug print
    print(f"Total questions: {len(questions_with_stats)}")
    print(f"Mastered questions: {len([q for q in questions_with_stats if q['stats']['mastered']])}")
    
    return render_template('stats.html', questions=questions_with_stats)

if __name__ == '__main__':
    app.run(debug=True) 