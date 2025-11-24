from flask import (
    Flask,
    render_template,
    redirect,
    request
)
import sqlite3

app = Flask(__name__)

@app.route("/tasks", methods = ["GET", "POST", "DELETE"])
def index():
    if request.method == "POST":
        try:
            con = sqlite3.connect("db/tasks.db")
            cur = con.cursor()
            print("Connection successful")

            sql = """
            INSERT INTO tasks (task_name, priority, date)
            VALUES (?, ?, ?);
            """

            task_name = request.form.get("task_name");
            task_priority = request.form.get("task_priority");
            task_date = request.form.get("task_date");

            cur.execute(sql, (task_name, task_priority, task_date))
            con.commit()
            con.close()
        except Exception as e:
            print(e)
        return redirect("/tasks")
    # dzēš ierakstu
    elif request.method == "DELETE":
        id_to_delete = request.form.get("id_to_delete")
        print(id_to_delete)

        try:
            sql = "DELETE FROM tasks WHERE task_id = ?;"
            con = sqlite3.connect("db/tasks.db")
            cur = con.cursor()
            cur.execute(sql, (int(id_to_delete), ))
            con.commit()
            con.close()
        except Exception as e:
            print(e)
        return redirect("/tasks")


    try:
        con = sqlite3.connect("db/tasks.db")
        cur = con.cursor()
        sql = "SELECT task_id, task_name, priority, date FROM tasks;"
        data = cur.execute(sql)
        data = data.fetchall()
        con.close()
        #print(data)
    except Exception as e:
        print(e)

    return render_template("index.html", data=data)


app.run(debug=True)