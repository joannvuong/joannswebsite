from flask import Flask
from flask import send_file
from flask import jsonify
import os
from database import get_database_connection

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)


@app.route('/')
def main():
    html = """
    
    <html>
<head>
</head>
<body>
    <h1>Joann Vuong, data scientist</h1>
    <p> this is a paragraph </p>
    <img src="/images/mainphoto.jpg"/>
</body>
</html>
    
    
    """
    return html

@app.route('/images/<imagename>')
def images(imagename):
    filename = 'images/' + imagename
    return send_file(filename)

@app.route('/api/skills')
def skills():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('select * from skills')
    skills_list = []
    for row in cursor:
        skills_list.append(row)
    return jsonify(skills_list)


if __name__ == "__main__":
    app.run(port=port)