Construction Spend Management & Payroll Platform

A full-stack application designed to help construction businesses manage workers, track attendance, automate payroll, and execute bulk payments — all in one system.

This project is inspired by real-world inefficiencies in how contractors manage labor and payments, and aims to provide a simple, cost-effective, and scalable solution.

---
 Problem

Small and medium-sized contractors often rely on:

- Manual payroll calculations (spreadsheets or paper)
- Individual mobile money payments (time-consuming)
- Multiple disconnected tools for tracking workers and expenses

This leads to:

- Errors in payroll
- Time wasted on repetitive tasks
- Poor visibility of project costs

---

 Solution

This platform combines:

- Workforce management (CRM)
- Payroll automation
- Bulk payment processing
- Project-based cost tracking

All within a single system.

---

Core Features

 Worker Management

- Add and manage workers
- Store roles, skills, and daily rates

 Attendance Tracking

- Record daily attendance
- Track presence per worker

 Payroll Engine

- Automatically calculate wages based on attendance
- Generate payroll previews
- Run payroll in one click

 Bulk Payments

- Pay multiple workers simultaneously
- Simulate transaction-based payment flow

 Project-Based Structure (In Progress)

- Organize workers and payments by construction site
- Track labor costs per project

---

 Tech Stack

- Frontend: React (Vite)
- Backend: FastAPI (Python)
- Database: SQLite
- Architecture: REST API + Component-based frontend

---

 System Design

The platform is structured into key modules:

- CRM: Workers, attendance, and project tracking
- Payroll: Wage calculation and automation
- Payments: Bulk disbursement and transaction tracking
- Dashboard: Financial summaries and insights

---

 Current Status

This project is actively in development.

 Completed:

- Worker management system
- Attendance tracking
- Payroll calculation logic
- Bulk payment functionality
- Transaction tracking

 In Progress:

- Project-based data structuring
- Payroll execution per project
- Usage-based pricing model (per transaction)

---

 Vision

To build a lightweight, usage-based financial operating system for SMEs that eliminates the need for expensive subscriptions and fragmented tools.

---

 Getting Started

Backend

cd backend
uvicorn main:app --reload

Frontend

cd frontend
npm install
npm run dev

---

 Future Improvements

- M-Pesa / payment API integration
- Approval workflows (request → approve → pay)
- Receipt capture and expense categorization
- Multi-user roles (admin, project manager)

---

 Author

Faith Nyambura
Aspiring Fintech Software Engineer

---

 Why This Project Matters

This project demonstrates:

- Full-stack development skills
- Real-world problem solving
- Understanding of fintech and SME workflows
- Ability to design scalable, modular systems

---