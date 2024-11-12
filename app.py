import os
import time
import platform
import psutil
from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the system info
    user_name = "NayanSethiya"
    server_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the top process information
    top_process = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
    top_output = ""
    for proc in top_process:
        top_output += f"PID: {proc.info['pid']} - Name: {proc.info['name']} - CPU: {proc.info['cpu_percent']}% - Memory: {proc.info['memory_percent']}%\n"
    
    return f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> Nayan Sethiya</p>
            <p><strong>Username:</strong> {user_name}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Top Process Info</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
