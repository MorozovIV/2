from flask import Flask, render_template
from flask_restful import Resource, Api
from time_now import time

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    time()
    time.current
    return render_template('index.html')

# class HelloWorld(Resource):
#     def get(self):
#         return render_template('index.html')
#
# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)