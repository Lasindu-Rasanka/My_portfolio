from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Add a simple route to test if Flask is working
@app.route('/')
def home():
    return jsonify({'message': 'Flask server is running!', 'status': 'success'})

# Enhanced AI responses for portfolio
ai_responses = {
    'hello': 'Hello! I\'m Lasindu\'s AI assistant. You can ask me about his skills, projects, education, or experience.',
    'hi': 'Hi there! What would you like to know about Lasindu?',
    'who are you': 'I\'m an AI assistant created by Lasindu to help you learn more about his skills and experience.',
    'what can you do': 'I can tell you about Lasindu\'s technical skills, projects, education, and professional experience. Try asking about his React skills or any of his projects!',
    
    # Skills responses
    'skill': 'Lasindu has expertise in Frontend (React, JavaScript, TypeScript, HTML, CSS, Tailwind), Backend (Python, Node.js, Express, Spring Boot, PHP), and Databases (MongoDB, MySQL).',
    'frontend': 'Lasindu\'s frontend skills include React.js, JavaScript, TypeScript, HTML, CSS, and Tailwind CSS.',
    'backend': 'Lasindu works with Python, Node.js, Express.js, Spring Boot, PHP, and builds RESTful APIs.',
    'database': 'Lasindu has experience with MongoDB and MySQL databases.',
    'react': 'Lasindu has React.js experience and has used it in projects like the Task Manager Web App and Skill Sharing Platform.',
    'python': 'Lasindu uses Python for backend development and has implemented projects like the AI-Powered Portfolio using Flask.',
    
    # Projects responses
    'project': 'Lasindu has worked on several projects including: Task Manager Web App, Smart Academic Scheduler, Skill Sharing Platform, To-Do Android App, AI-Powered Portfolio, and Handmade Goods E-Commerce App.',
    'task manager': 'The Task Manager Web App was built with Flask, React TypeScript, MySQL, and Tailwind CSS. It includes authentication, filtering, and analytics features.',
    'academic scheduler': 'The Smart Academic Scheduler helps automate timetable planning and optimize study routines. It was built with the MERN stack.',
    'skill sharing': 'The Skill Sharing Platform connects learners with mentors and was built with React, Spring Boot, and MongoDB.',
    'todo app': 'The Android To-Do app was built with Kotlin in Android Studio and includes task management with reminders.',
    'ai portfolio': 'This AI-Powered Portfolio was built with Python, Flask, HTML, CSS, and JavaScript to showcase skills interactively.',
    'ecommerce': 'The Handmade Goods E-Commerce Web App is a full-stack application built with the MERN stack (MongoDB, Express, React, Node).',
    
    # Education responses
    'education': 'Lasindu is a Third Year Undergraduate at Sri Lanka Institute of Information Technology (SLIIT), studying BSc (Hons) in Information Technology. He expects to graduate in December 2026.',
    'sliit': 'SLIIT is the Sri Lanka Institute of Information Technology where Lasindu is pursuing his degree in Information Technology.',
    
    # Experience responses
    'experience': 'Lasindu is currently seeking internship opportunities to enhance his frontend, backend, or full stack development skills.',
    'internship': 'Lasindu is looking for internship opportunities in growth-oriented companies where he can contribute effectively while developing his skills.',
    
    # Contact responses
    'contact': 'You can contact Lasindu via email at lasindu5909@gmail.com, phone at +94 740 551 961, or through his LinkedIn profile.',
    'email': 'Lasindu\'s email address is lasindu5909@gmail.com.',
    'phone': 'You can reach Lasindu at +94 740 551 961.',
    'linkedin': 'You can find Lasindu on LinkedIn at https://www.linkedin.com/in/Lasindu-Rasanka',
    'github': 'Check out Lasindu\'s GitHub projects at https://github.com/Lasindu-Rasanka',
    
    'default': "I'm not sure I understand. You can ask about Lasindu's skills, projects, education, or how to contact him. Try phrases like 'What are your skills?' or 'Tell me about your projects'."
}

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower().strip()
    
    if not user_input:
        return jsonify({'response': 'Please provide a message.'})
    
    # Help command
    if user_input in ['help', '?']:
        return jsonify({'response': "I can answer questions about: skills, projects, education, experience, and contact info. Try asking: 'What frontend skills do you have?' or 'Tell me about your projects'."})
    
    # Check for specific terms first
    if 'task manager' in user_input:
        response = ai_responses['task manager']
    elif 'academic scheduler' in user_input:
        response = ai_responses['academic scheduler']
    elif 'skill sharing' in user_input:
        response = ai_responses['skill sharing']
    elif 'todo app' in user_input or 'to-do app' in user_input:
        response = ai_responses['todo app']
    elif 'ai portfolio' in user_input or 'ai-powered' in user_input:
        response = ai_responses['ai portfolio']
    elif 'ecommerce' in user_input or 'e-commerce' in user_input:
        response = ai_responses['ecommerce']
    else:
        # General keyword matching
        response = ai_responses['default']
        for keyword in ai_responses:
            if keyword != 'default' and keyword in user_input:
                response = ai_responses[keyword]
                break
    
    # Make response more conversational
    if user_input.startswith('what') and not response.startswith('Lasindu') and not response.startswith('He'):
        response = 'Lasindu ' + response.lower()
    
    if user_input.startswith('do you') and response.startswith('Lasindu'):
        response = 'Yes, ' + response.lower()
    
    return jsonify({'response': response})

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    
    # Here you would typically save the contact form data to a database
    # For this example, we'll just log it and return a success message
    print("Contact form submission:")
    print(f"Name: {data.get('name')}")
    print(f"Email: {data.get('email')}")
    print(f"Subject: {data.get('subject')}")
    print(f"Message: {data.get('message')}")
    
    return jsonify({'message': 'Thank you for your message! I will get back to you soon.'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)