from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

menu_options = [
    "1. About",
    "2. Contact Information",
    "3. Skills",
    "4. Certificate's",
    "5. Projects"
]

chatbot = {
    "1": """Hi I'm G Pavan Kumar, a 4th year Computer Science student specializing in AIML.
I'm passionate about building intelligent systems using Python, exploring ML, and creating real-world solutions.
Looking for internships where I can grow professionally.""",
    "2": """Mail: pavanreddygunata@gmail.com
Ph.no: +91 6845*****
Address: 23-338/2, Vidhyanagar Colony, K R Palli, Chittoor, Andhra Pradesh""",
    "3": """Skills: Python, HTML, CSS, JavaScript, React JS, NumPy, Pandas""",
    "4": """Certificates: Data Analytics Job Simulation,
Google AI Essentials,
Analyzing Data with R,
Vusualyzing Data with R""",
    "5": """Projects: Portfolio website with personal chatbot which gives info about me."""
}

def get_response(user_query):
    user_query = user_query.lower()

    if "about" in user_query or "yourself" in user_query:
        return chatbot["1"]
    elif "contact" in user_query or "email" in user_query or "phone" in user_query:
        return chatbot["2"]
    elif "skills" in user_query:
        return chatbot["3"]
    elif "certificate" in user_query or "certification" in user_query:
        return chatbot["4"]
    elif "project" in user_query:
        return chatbot["5"]
    elif "menu" in user_query or "options" in user_query:
        return "\n".join(menu_options)
    else:
        return "I'm sorry, I didn't understand that. Try asking about my skills, projects, or type 'menu'."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    response = get_response(message.strip())
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
