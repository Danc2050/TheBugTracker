import src.AutoBugTracker as autoBugTracker
import src.ReadConfig as readConfig
from flask import Flask

app = Flask(__name__)


@app.route("/submitBug", methods=["POST"])
def issueBug():
    execute = autoBugTracker.AutoBugTracker()
    execute.issueBugReport()
    return "200"


if __name__ == '__main__':
    readConfig.readConfig().createDefault()
    app.run(host='127.0.0.1', debug=True, port=80)
