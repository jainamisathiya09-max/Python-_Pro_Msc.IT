from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add_task", methods=["POST"])
def add_task():

    task_name = request.form.get("task_name")
    task_date = request.form.get("task_date")
    status = request.form.get("status")

    task = {
        "task_name": task_name,
        "task_date": task_date,
        "status": status
    }

    tasks.append(task)

    return jsonify({
        "message": "Task added successfully",
        "task": task
    })


@app.route("/get_tasks")
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True)
