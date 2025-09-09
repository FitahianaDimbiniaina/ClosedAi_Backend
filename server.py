# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# import os
# from gemini_setup import get_gemini_response

# app = Flask(__name__, static_folder="../frontend/dist", static_url_path="")
# CORS(app)

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     user_message = data.get('message', '')
#     response = get_gemini_response(user_message)
#     return jsonify({'response': response})

# @app.route('/')
# def serve_index():
#     return send_from_directory(app.static_folder, 'index.html')

# @app.route('/<path:path>')
# def serve_static(path):
#     return send_from_directory(app.static_folder, path)

# if __name__ == '__main__':
#     app.run(debug=False)from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from flask import Flask, request, jsonify, redirect
from gemini_setup import get_gemini_response

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    history = data.get('history', [])
    user_message = history[-1]['text'] if history else ''

    system_instruction = (
        "You are an AI chatbot based on Gemini 2.5, integrated into this app by Dimbiniaina Fitahiana. "
        "If the user asks about your identity, origin, you must always include this information "
        "in your answer. After that, continue with your usual reasoning and response as you normally would. "
        "For all other queries, answer normally."
    )
    
    response = get_gemini_response(user_message, system_instruction)
    return jsonify({'response': response})

@app.route('/')
def redirect_to_vite():
    return redirect("http://localhost:5173", code=302)

if __name__ == '__main__':
    app.run(debug=False, port=5000)