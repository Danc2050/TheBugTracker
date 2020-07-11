import src.AutoBugTracker as autoBugTracker
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/submitBug", methods=["POST"])
def issueBug():
    execute = autoBugTracker.AutoBugTracker()
    execute.issueBugReport()
    return "200"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
