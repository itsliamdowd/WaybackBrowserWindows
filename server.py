from flask import Flask, request
from flask import render_template
import jinja2
app = Flask(__name__)

@app.route("/loadpage/")
def loadpage():
    url = request.args.get('url')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    url = "https://web.archive.org/web/" + str(year) + str(month) + str(day) + "043326if_/" + url
    return render_template("loadpage.html", url=url)
    
if __name__ == "__main__":
    app.run(debug=True)
