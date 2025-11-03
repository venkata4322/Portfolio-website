from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)

    print("\n" + "="*70)
    print("🚀 CREATIVE PORTFOLIO WEBSITE IS RUNNING!")
    print("="*70)
    print("📍 LOCAL: http://127.0.0.1:5000")
    print("📍 HOSTING: Deploy on Render.com, PythonAnywhere, or Heroku")
    print("="*70 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
