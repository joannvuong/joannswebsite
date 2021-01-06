from flask import Flask
from flask import send_file

app = Flask(__name__)


@app.route('/')
def main():
    html = """
    
    <html>
<head>
</head>
<body>
    <h1>Joann Vuong, data scientist</h1>
    <img src="/images/mainphoto.jpg"/>
</body>
</html>
    
    
    """
    return html
@app.route('/images/<imagename>')

def images(imagename):
    filename = 'images/' + imagename
    return send_file(filename)

if __name__ == "__main__":
    app.run()