from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="dss_db",
    user="Fuga",
    password="admin"
)
cursor = conn.cursor()

# Routes and Logic for Each Sector
@app.route("/")
def index():
    return render_template("index.html")

# Logistics
@app.route("/logistics", methods=["GET", "POST"])
def logistics():
    if request.method == "POST":
        item = request.form["item"]
        quantity = request.form["quantity"]
        status = request.form["status"]
        cursor.execute("INSERT INTO logistics (item, quantity, status) VALUES (%s, %s, %s)", (item, quantity, status))
        conn.commit()
        return redirect(url_for("logistics"))
    cursor.execute("SELECT * FROM logistics")
    data = cursor.fetchall()
    return render_template("logistics.html", data=data)

# Retail
@app.route("/retail", methods=["GET", "POST"])
def retail():
    if request.method == "POST":
        product = request.form["product"]
        sales = request.form["sales"]
        stock = request.form["stock"]
        cursor.execute("INSERT INTO retail (product, sales, stock) VALUES (%s, %s, %s)", (product, sales, stock))
        conn.commit()
        return redirect(url_for("retail"))
    cursor.execute("SELECT * FROM retail")
    data = cursor.fetchall()
    return render_template("retail.html", data=data)

# Production
@app.route("/production", methods=["GET", "POST"])
def production():
    if request.method == "POST":
        product_name = request.form["product_name"]
        units_produced = request.form["units_produced"]
        production_cost = request.form["production_cost"]
        cursor.execute(
            "INSERT INTO production (product_name, units_produced, production_cost) VALUES (%s, %s, %s)",
            (product_name, units_produced, production_cost)
        )
        conn.commit()
        return redirect(url_for("production"))
    cursor.execute("SELECT * FROM production")
    data = cursor.fetchall()
    return render_template("production.html", data=data)

# Healthcare
@app.route("/healthcare", methods=["GET", "POST"])
def healthcare():
    if request.method == "POST":
        department = request.form["department"]
        patients_treated = request.form["patients_treated"]
        staff_count = request.form["staff_count"]
        cursor.execute(
            "INSERT INTO healthcare (department, patients_treated, staff_count) VALUES (%s, %s, %s)",
            (department, patients_treated, staff_count)
        )
        conn.commit()
        return redirect(url_for("healthcare"))
    cursor.execute("SELECT * FROM healthcare")
    data = cursor.fetchall()
    return render_template("healthcare.html", data=data)

# Education
@app.route("/education", methods=["GET", "POST"])
def education():
    if request.method == "POST":
        course_name = request.form["course_name"]
        enrollment = request.form["enrollment"]
        graduation_rate = request.form["graduation_rate"]
        cursor.execute(
            "INSERT INTO education (course_name, enrollment, graduation_rate) VALUES (%s, %s, %s)",
            (course_name, enrollment, graduation_rate)
        )
        conn.commit()
        return redirect(url_for("education"))
    cursor.execute("SELECT * FROM education")
    data = cursor.fetchall()
    return render_template("education.html", data=data)

# Hospitality
@app.route("/hospitality", methods=["GET", "POST"])
def hospitality():
    if request.method == "POST":
        facility_name = request.form["facility_name"]
        rooms_available = request.form["rooms_available"]
        occupancy_rate = request.form["occupancy_rate"]
        cursor.execute(
            "INSERT INTO hospitality (facility_name, rooms_available, occupancy_rate) VALUES (%s, %s, %s)",
            (facility_name, rooms_available, occupancy_rate)
        )
        conn.commit()
        return redirect(url_for("hospitality"))
    cursor.execute("SELECT * FROM hospitality")
    data = cursor.fetchall()
    return render_template("hospitality.html", data=data)

# Employee Management
@app.route("/employee_management", methods=["GET", "POST"])
def employee_management():
    if request.method == "POST":
        employee_name = request.form["employee_name"]
        position = request.form["position"]
        department = request.form["department"]
        cursor.execute(
            "INSERT INTO employee_management (employee_name, position, department) VALUES (%s, %s, %s)",
            (employee_name, position, department)
        )
        conn.commit()
        return redirect(url_for("employee_management"))
    cursor.execute("SELECT * FROM employee_management")
    data = cursor.fetchall()
    return render_template("employee_management.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
