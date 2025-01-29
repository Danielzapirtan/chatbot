# app.py
from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

def get_bot_response(prompt):
    try:
        # Run the bot executable with the prompt as input
        process = subprocess.Popen(['./bot'], 
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 text=True)
        
        # Send the prompt and get the response
        output, error = process.communicate(input=prompt)
        
        if error:
            return f"Error: {error}"
        
        return output.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({'response': 'Error: Empty prompt'})
    
    response = get_bot_response(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5089, debug=True)
  
