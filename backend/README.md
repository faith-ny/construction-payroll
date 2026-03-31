# Construction Payroll System

A mobile-first web application designed to help construction contractors manage daily laborers, track attendance, and automate payroll.

## Problem

Construction contractors often:

* Pay workers in cash daily
* Struggle to track attendance across multiple sites
* Lose time calculating wages manually
* Have no record of worker history or reliability

## Solution

This system provides:

* Worker registration and management
* Daily attendance tracking
* Automated payroll calculation (coming soon)
* Future integration with mobile money for bulk payments

## Tech Stack

* **Backend:** FastAPI
* **Language:** Python
* **Database:** SQLite
* **API Docs:** Swagger UI

## Features Implemented

* Add new workers
* View all registered workers

## Features Coming Next

* Attendance tracking
* Payroll calculation
* Bulk payment simulation
* Contractor dashboard

## How to Run Locally

1. Clone the repository
2. Install dependencies:

   ```
   pip install fastapi uvicorn
   ```
3. Run the server:

   ```
   uvicorn backend.main:app --reload
   ```
4. Open API docs:

   ```
   http://127.0.0.1:8000/docs
   ```

## Author

Faith Nyambura
Aspiring Fintech & SaaS Developer
