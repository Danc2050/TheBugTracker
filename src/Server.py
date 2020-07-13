import src.AutoBugTracker as autoBugTracker
from flask import Flask

app = Flask(__name__)


@app.route("/submitBug", methods=["POST"])
def issueBug():
    execute = autoBugTracker.AutoBugTracker()
    execute.issueBugReport()
    return "200"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
