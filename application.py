from flask import Flask, jsonify

application = Flask(__name__)

@application.route('/')
def hello():
    return '<h1>Hello from CI/CD, Mardonkulov for remodule and others as well!</h1>', 200

@application.route('/health')
def health():
    return jsonify(status='ok'), 200

if __name__ == 'main':
    application.run()