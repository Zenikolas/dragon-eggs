from flask import Flask
from worker import tasks
app = Flask(__name__)


@app.route("/")
def hello():
    ret = tasks.count.delay()
    return ret.get()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
