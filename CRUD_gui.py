from flask import Flask, render_template_string, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["crime_tracker_db"]

PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Crime Tracker - MongoDB CRUD</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 950px;
      margin: 30px auto;
      padding: 20px;
      background: #f0f2f5;
    }
    h1 {
      color: #1a1a2e;
      border-bottom: 4px solid #c8a600;
      padding-bottom: 12px;
      margin-bottom: 25px;
    }
    h2 { color: #1a1a2e; font-size: 17px; margin-bottom: 12px; }
    .card {
      background: white;
      padding: 20px 24px;
      border-radius: 10px;
      margin-bottom: 24px;
      box-shadow: 0 1px 5px rgba(0,0,0,0.1);
    }
    table { width: 100%; border-collapse: collapse; }
    th {
      background: #1a1a2e;
      color: white;
      padding: 10px 14px;
      text-align: left;
      font-size: 13px;
    }
    td { padding: 9px 14px; border-bottom: 1px solid #eee; font-size: 13px; }
    tr:hover td { background: #fafafa; }
    input, select {
      padding: 8px 12px;
      border: 1px solid #ccc;
      border-radius: 6px;
      font-size: 13px;
      margin: 4px 4px 4px 0;
      width: 220px;
    }
    .btn {
      padding: 7px 16px;
      border-radius: 6px;
      border: none;
      font-size: 12px;
      cursor: pointer;
      text-decoration: none;
      display: inline-block;
    }
    .btn-gold { background: #c8a600; color: white; }
    .btn-blue { background: #185FA5; color: white; }
    .btn-red  { background: #c0392b; color: white; }
    .badge {
      padding: 2px 10px;
      border-radius: 10px;
      font-size: 11px;
      font-weight: bold;
    }
    .open                { background: #d4edda; color: #155724; }
    .closed              { background: #f8d7da; color: #721c24; }
    .under_investigation { background: #fff3cd; color: #856404; }
    .dismissed           { background: #e2e3e5; color: #383d41; }
    .msg {
      background: #d4edda;
      color: #155724;
      padding: 10px 16px;
      border-radius: 6px;
      margin-bottom: 16px;
      font-size: 13px;
    }
  </style>
</head>
<body>

<h1>Crime and Legal Case Tracking System - MongoDB CRUD GUI</h1>

{% if message %}
<div class="msg">{{ message }}</div>
{% endif %}

<div class="card">
  <h2>Add New Case (CREATE)</h2>
  <form method="POST" action="/add_case">
    <input name="case_number" placeholder="Case Number e.g. CASE-2024-010" required>
    <input name="title" placeholder="Case Title" required>
    <input name="crime_type" placeholder="Crime Type" required>
    <select name="status">
      <option value="open">Open</option>
      <option value="under_investigation">Under Investigation</option>
      <option value="closed">Closed</option>
      <option value="dismissed">Dismissed</option>
    </select>
    <input name="judge_name" placeholder="Judge Name" required>
    <br><br>
    <button type="submit" class="btn btn-gold">Add Case</button>
  </form>
</div>

<div class="card">
  <h2>All Cases (READ)</h2>
  <table>
    <tr>
      <th>Case Number</th><th>Title</th><th>Crime Type</th>
      <th>Status</th><th>Judge</th><th>Hearings</th><th>Actions</th>
    </tr>
    {% for c in cases %}
    <tr>
      <td>{{ c.case_number }}</td>
      <td>{{ c.title }}</td>
      <td>{{ c.crime_type }}</td>
      <td><span class="badge {{ c.status }}">{{ c.status }}</span></td>
      <td>{{ c.get("judge_name", "N/A") }}</td>
      <td>{{ c.get("hearings", []) | length }}</td>
      <td>
        <a href="/close_case/{{ c._id }}" class="btn btn-blue">Close (UPDATE)</a>
        &nbsp;
        <a href="/delete_case/{{ c._id }}" class="btn btn-red"
           onclick="return confirm('Are you sure?')">Delete</a>
      </td>
    </tr>
    {% endfor %}
  </table>
</div>

<div class="card">
  <h2>All Persons (READ)</h2>
  <table>
    <tr>
      <th>Full Name</th><th>Roles</th><th>Gender</th>
      <th>Phone</th><th>National ID</th>
    </tr>
    {% for p in persons %}
    <tr>
      <td>{{ p.full_name }}</td>
      <td>{{ ", ".join(p.get("roles", [])) }}</td>
      <td>{{ p.get("gender", "N/A") }}</td>
      <td>{{ p.get("phone", "N/A") }}</td>
      <td>{{ p.national_id }}</td>
    </tr>
    {% endfor %}
  </table>
</div>

<div class="card">
  <h2>All Evidence (READ)</h2>
  <table>
    <tr>
      <th>Type</th><th>Description</th><th>Case</th>
      <th>Collected Date</th><th>Collected By</th>
    </tr>
    {% for e in evidence %}
    <tr>
      <td>{{ e.evidence_type }}</td>
      <td>{{ e.description }}</td>
      <td>{{ e.get("case_number", "N/A") }}</td>
      <td>{{ e.collected_date }}</td>
      <td>{{ e.get("collected_by", "N/A") }}</td>
    </tr>
    {% endfor %}
  </table>
</div>

</body>
</html>
"""

@app.route("/")
def index():
    cases    = list(db.cases.find())
    persons  = list(db.persons.find())
    evidence = list(db.evidence.find())
    msg = request.args.get("msg", "")
    return render_template_string(PAGE, cases=cases, persons=persons,
                                  evidence=evidence, message=msg)

@app.route("/add_case", methods=["POST"])
def add_case():
    db.cases.insert_one({
        "case_number":       request.form["case_number"],
        "title":             request.form["title"],
        "status":            request.form["status"],
        "crime_type":        request.form["crime_type"],
        "judge_name":        request.form["judge_name"],
        "filed_date":        "2024-01-01",
        "closed_date":       None,
        "hearings":          [],
        "verdict":           None,
        "lead_investigator": "Zafar Iqbal",
        "suspects":          []
    })
    return redirect("/?msg=New case added successfully")

@app.route("/close_case/<id>")
def close_case(id):
    db.cases.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"status": "closed"}}
    )
    return redirect("/?msg=Case status updated to closed")

@app.route("/delete_case/<id>")
def delete_case(id):
    db.cases.delete_one({"_id": ObjectId(id)})
    return redirect("/?msg=Case deleted successfully")

if __name__ == "__main__":
    app.run(debug=True)