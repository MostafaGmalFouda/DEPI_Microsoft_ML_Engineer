from flask import Flask, render_template, request, redirect, url_for, flash
from Hospital import Hospital
from Department import Department
from Patient import Patient
from Staff import Staff

app = Flask(__name__)
app.secret_key = "supersecretkey"

hospital = Hospital("General Hospital", "Cairo")

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect(url_for("dashboard"))
        else:
            flash("Incorrect username or password!", "danger")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", hospital=hospital)


@app.route("/add_department", methods=["POST"])
def add_department():
    dept_name = request.form.get("dept_name")
    if dept_name:
        new_dept = Department(dept_name)
        hospital.add_department(new_dept)
        flash(f"Department '{dept_name}' has been added.", "success")
    return redirect(url_for("dashboard"))


@app.route("/add_patient", methods=["POST"])
def add_patient():
    dept_name = request.form.get("dept_name")
    patient_name = request.form.get("patient_name")
    age = int(request.form.get("age", 0))
    record = request.form.get("record")
    
    if dept_name and patient_name and record:
        department = next((d for d in hospital.departments if d.name == dept_name), None)
        if department:
            new_patient = Patient(patient_name, age, record)
            department.add_patient(new_patient)
            flash(f"Patient '{patient_name}' has been added to {dept_name}.", "success")
        else:
            flash("Department not found!", "danger")
    return redirect(url_for("dashboard"))


@app.route("/add_staff", methods=["POST"])
def add_staff():
    dept_name = request.form.get("dept_name")
    staff_name = request.form.get("staff_name")
    age = int(request.form.get("age", 0))
    position = request.form.get("position")
    
    if dept_name and staff_name and position:
        department = next((d for d in hospital.departments if d.name == dept_name), None)
        if department:
            new_staff = Staff(staff_name, age, position)
            department.add_staff(new_staff)
            flash(f"Staff member '{staff_name}' has been added to {dept_name}.", "success")
        else:
            flash("Department not found!", "danger")
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
