from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Child.html")

project_proposals = [
 {
     "netid": "abc123",
     "title": "Pizza on U",
     "description": "A site that adds a slice of pizza to images",
     "modules": ["flask", "pil"]
 },
 {
     "netid": "xyz789",
     "title": "Catfinity",
     "description": "Creates a collage of random cat images",
     "modules": ["pil", "requests"]
 },
 {
     "netid": "ynot42",
     "title": "hippost",
     "description": "An image board for hippo enthusiasts",
     "modules": ["flask", "pil"]
 }
]


@app.route("/projects", methods=["POST", "GET"])
def projects_add():
    if request.method == "POST":
        modules = request.form["Modules"].split(",")
        project_proposals.insert(0, {"netid":request.form["NetID"]
                                  ,"title":request.form["Title"]
                                  ,"description":request.form["Description"]
                                  ,"modules":modules})
        return redirect('/projects')
    elif request.method == "GET":
        return render_template("Projects.html", projects=project_proposals)


@app.route("/report")
def reprot():
    module_count = {}
    for item in project_proposals:
        for x, y in item.items():
            if x == "modules":
                for module in y:
                    try:
                        module_count[module] += 1
                    except KeyError:
                        module_count[module] = 1
    return render_template("Report.html", modules=module_count)

if __name__ == '__main__':
    app.run(debug=True)