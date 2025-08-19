document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const navUl = document.querySelector('nav ul');
    
    menuToggle.addEventListener('click', function() {
        navUl.classList.toggle('active');
    });
    
    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navUl.classList.remove('active');
        });
    });
    
    // Header scroll effect
    const header = document.querySelector('header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    
    // AI Assistant functionality
    const aiButton = document.getElementById('aiButton');
    const aiChat = document.getElementById('aiChat');
    const closeChat = document.getElementById('closeChat');
    const aiMessages = document.getElementById('aiMessages');
    const aiInput = document.getElementById('aiInput');
    const aiSend = document.getElementById('aiSend');
    
    aiButton.addEventListener('click', function() {
        aiChat.classList.toggle('active');
    });
    
    closeChat.addEventListener('click', function() {
        aiChat.classList.remove('active');
    });
    
    // Sample responses for the AI assistant
    const aiResponses = {
        'hello': 'Hello there! How can I help you today?',
        'hi': 'Hi! What would you like to know about Lasindu?',
        'skills': 'Lasindu has skills in Frontend (React, JavaScript, TypeScript), Backend (Python, Node.js, Spring Boot), and Databases (MongoDB, MySQL).',
        'projects': 'Lasindu has worked on several projects including a Task Manager Web App, Smart Academic Scheduler, and an AI-Powered Portfolio Web Application.',
        'contact': 'You can contact Lasindu via email at lasindu5909@gmail.com or phone at +94 740 551 961.',
        'education': 'Lasindu is a Third Year Undergraduate at SLIIT, studying BSc (Hons) in Information Technology, expected to graduate in December 2026.',
        'default': "I'm sorry, I didn't understand that. You can ask about Lasindu's skills, projects, education, or how to contact him."
    };
    
    function addMessage(message, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        if (isUser) {
            messageDiv.classList.add('user-message');
            messageDiv.innerHTML = `<strong>You:</strong> ${message}`;
        } else {
            messageDiv.classList.add('ai-message');
            messageDiv.innerHTML = `<strong>AI:</strong> ${message}`;
        }
        aiMessages.appendChild(messageDiv);
        aiMessages.scrollTop = aiMessages.scrollHeight;
    }
    
    function processInput() {
        const userInput = aiInput.value.toLowerCase().trim();
        if (!userInput) return;
        
        addMessage(userInput, true);
        aiInput.value = '';
        
        // Simple response logic - in a real app, you'd connect to an AI API
        let response = aiResponses.default;
        
        if (userInput.includes('hello') || userInput.includes('hi')) {
            response = aiResponses.hello;
        } else if (userInput.includes('skill')) {
            response = aiResponses.skills;
        } else if (userInput.includes('project')) {
            response = aiResponses.projects;
        } else if (userInput.includes('contact')) {
            response = aiResponses.contact;
        } else if (userInput.includes('educat') || userInput.includes('study')) {
            response = aiResponses.education;
        }
        
        // Simulate typing effect
        setTimeout(() => {
            addMessage(response);
        }, 500);
    }
    
    aiSend.addEventListener('click', processInput);
    
    aiInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            processInput();
        }
    });
    
    // Contact form submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;
            
            // Here you would typically send the form data to a server
            // For this example, we'll just show an alert
            alert(`Thank you, ${name}! Your message has been received. I'll get back to you soon at ${email}.`);
            
            // Reset form
            contactForm.reset();
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
});