from flask import Flask
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


# port = os.environ.get('port')
# host = os.environ.get('host')
# data= os.environ.get('data')

@app.route("/")
def hello():
    return f"<h1>Hello World! deployed to AWS {os.getenv('data')}</h1>"

if __name__ == '__main__':
    app.run(host=os.getenv('host'), port=os.getenv('port'), debug=False)