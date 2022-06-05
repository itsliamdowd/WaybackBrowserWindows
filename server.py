from flask import Flask, request
from flask import render_template
import jinja2
app = Flask(__name__)

@app.route("/loadpage/")
def loadpage():
    url = request.args.get('url')
    print(url)
    year = request.args.get('year')
    print(year)
    month = request.args.get('month')
    print(month)
    day = request.args.get('day')
    print(day)
    #url = "https://web.archive.org/web/" + str(year) + "07" + "11" + "043326if_/" + url
    url = "https://web.archive.org/web/" + str(year) + str(month) + str(day) + "043326if_/" + url
    return render_template("loadpage.html", url=url)
    
if __name__ == "__main__":
    app.run(debug=True)