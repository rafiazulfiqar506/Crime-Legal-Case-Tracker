# Criminal Case Management System

A JSON-based Criminal Case Management System designed to store, manage, and track information related to criminal investigations, legal proceedings, evidence records, and individuals involved in the justice process.

The project combines structured JSON datasets with a Flask-based CRUD interface and MongoDB integration to simulate a real-world criminal justice information system.

---

## Overview

The Criminal Case Management System provides a centralized platform for managing criminal cases and their associated entities. It demonstrates how NoSQL databases and JSON documents can be used to model complex legal relationships while providing an easy-to-use web interface for performing database operations.

The system supports managing:

* Criminal cases
* Persons involved in investigations and trials
* Evidence records
* Court proceedings
* Multiple participant roles

This project was developed primarily for educational and academic purposes to demonstrate database concepts, NoSQL modeling, and web application development.

---

## Features

### Case Management

* Create new criminal case records
* View all registered cases
* Update case status
* Close active cases
* Delete case records

### Person Management

* Centralized person records
* Multi-role support for individuals
* Role-specific information storage
* Flexible JSON representation

### Evidence Management

* Track evidence linked to cases
* Maintain chain of custody
* Support multiple evidence types
* Associate evidence with investigators

### Web-Based Interface

* Flask-powered CRUD dashboard
* Simple and user-friendly interface
* Real-time MongoDB interaction

### Database Integration

* MongoDB support using PyMongo
* JSON datasets for easy import/export
* NoSQL document modeling

---

## System Roles

A person in the system may have one or multiple roles.

Example:

```json
"roles": ["suspect", "witness"]
```

Supported roles include:

* Suspect
* Witness
* Lawyer
* Judge
* Investigator

---

## Person Data Structure

Each person record stores common information and role-specific details.

### Basic Information

* Full Name
* National ID
* Date of Birth
* Gender
* Phone Number
* Email Address
* Residential Address

---

## Role-Specific Information

### Suspect Details

```json
{
  "risk_level": "high",
  "status": "arrested",
  "arrest_date": "2024-01-10",
  "criminal_record": "Prior theft 2019"
}
```

### Witness Details

```json
{
  "protection_status": true,
  "statement": "Witness statement",
  "credibility_score": 8
}
```

### Lawyer Details

```json
{
  "bar_number": "BAR-2024-001",
  "specialization": "Criminal Defense",
  "firm_name": "Justice and Partners LLP",
  "years_experience": 15
}
```

### Judge Details

```json
{
  "court_name": "Islamabad High Court",
  "appointment_date": "2015-06-01",
  "jurisdiction": "Federal Crimes"
}
```

### Investigator Details

```json
{
  "badge_number": "FIA-001",
  "rank": "Senior Inspector",
  "department": "Federal Investigation Agency"
}
```

---

## Evidence Management

The system supports three major evidence categories.

### Digital Evidence

Examples include:

* CCTV footage
* Emails
* Server logs
* Multimedia files

Stored information:

* File Type
* File Size
* Hash Value
* Device Type

### Physical Evidence

Examples include:

* Fingerprints
* Weapons
* Documents
* Biological samples

Stored information:

* Location Found
* Weight
* Dimensions
* Laboratory Results

### Testimonial Evidence

Examples include:

* Witness statements
* Recorded testimonies

Stored information:

* Witness Name
* Sworn Status
* Statement Date
* Transcript

---

## Technologies Used

* Python
* Flask
* MongoDB
* PyMongo
* JSON
* HTML
* CSS

Optional integrations:

* JavaScript
* Node.js
* REST APIs

---

## Project Structure

```text
Criminal-Case-Management-System/
│
├── CRUD_gui.py          # Flask CRUD application
├── persons.json         # Person records
├── cases.json           # Criminal case records
├── evidence.json        # Evidence records
├── courts.json          # Court information
├── README.md
└── Additional files...
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Criminal-Case-Management-System
```

### Install Dependencies

```bash
pip install flask pymongo
```

### Start MongoDB

Ensure MongoDB is running locally:

```text
mongodb://localhost:27017/
```

### Run the Application

```bash
python CRUD_gui.py
```

### Access the System

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## CRUD Functionalities

### Create

Add new criminal cases through the web interface.

### Read

View:

* Cases
* Persons
* Evidence records

### Update

Modify case status by closing active cases.

### Delete

Remove case records permanently.

---

## Example Use Cases

* Criminal Case Tracking
* Court Record Management
* Investigation Management
* Evidence Tracking
* Database Design Practice
* NoSQL Learning Projects
* Flask and MongoDB Integration
* Academic Semester Projects

---

## Future Enhancements

* User authentication and authorization
* Role-based access control
* Advanced search and filtering
* Court scheduling module
* Case assignment system
* REST API support
* Dashboard analytics and reporting
* Evidence file uploads
* Notification system

---

## Disclaimer

This project is intended solely for educational and learning purposes. Any names, identifiers, or personal information contained within the sample datasets are fictional and used only to demonstrate system functionality and database design concepts.

---

## Author

Developed as an academic project to demonstrate JSON modeling, MongoDB integration, Flask-based CRUD operations, and criminal case management concepts.
