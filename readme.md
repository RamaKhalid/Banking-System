# 🏦Banking System

A simple banking application that demonstrates account management, transactions, and reporting using Object-Oriented Programming (OOP) and Test-Driven Development (TDD).

## Description

This project simulates a small-scale banking system where customers can open and manage checking and savings accounts. Users can deposit, withdraw, and transfer money, while the system enforces overdraft protection and logs all transactions. Account statements can be generated in text format, and a reward system highlights the top-performing customers.

The project is built with at least three core classes (plus test classes) and makes use of the provided `bank.csv` file to store customer and account data. Additional classes may be added for better design and modularity. All functionality is implemented following a **TDD approach**, ensuring reliability and maintainability.

## 💰Features 

* Add new customers with checking and/or savings accounts
* Strong password validation for new customers
* Deposits, withdrawals, and transfers (between own accounts or to other customers)
* Overdraft protection with fees, withdrawal limits, and account deactivation/reactivation
* Transaction history tracking and retrieval
* Generate account statements as `.txt` reports
* Custom overdraft limits per customer
* Top 3 customers reward system with bonus
* Fully tested with unit tests under TDD

