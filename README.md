# Restaurant Reservation Management System - Database Project

## **Project Overview**

This project implements a **Restaurant Reservation Management System** using **MS SQL Server**. The system is designed to help a group of restaurants transition from a traditional ordering and reservation process to a robust digital platform. It manages restaurants, menu items, orders, employees, customers, tables, and reservations, while providing complex querying, reporting, and analysis functionalities.

---

## **Objectives**

- Design a relational database that models restaurant operations.
- Implement key database functionalities including views, functions, stored procedures, triggers, and complex queries.
- Enable efficient reporting and analytics for restaurant management.

---

## **Database Design**

### **Entity Relationship Model (ERM)**

The database contains the following entities:

| Entity       | Description                                  |
|-------------|----------------------------------------------|
| Restaurants  | Stores restaurant information                |
| MenuItems    | Menu items offered by restaurants           |
| Orders       | Customer orders linked to reservations      |
| OrderItems   | Items in each order                          |
| Employees    | Staff working in restaurants                |
| Customers    | Registered customers                        |
| Tables       | Restaurant tables                            |
| Reservations | Customer reservations at restaurants        |

**Relationships & Keys:**

- Primary keys (PK) and foreign keys (FK) are implemented to maintain referential integrity.
- ER Diagram available in the `/ERD` folder (created using ERDPlus/Lucidchart).

---

## **Relational Schema**

**Tables and Key Columns:**

- **Restaurants**: `RestaurantId (PK), Name, Address, PhoneNumber, OpeningHours`
- **MenuItems**: `ItemId (PK), RestaurantId (FK), Name, Description, Price`
- **Orders**: `OrderId (PK), ReservationId (FK), EmployeeId (FK), OrderDate, TotalAmount`
- **OrderItems**: `OrderItemId (PK), OrderId (FK), ItemId (FK), Quantity`
- **Employees**: `EmployeeId (PK), RestaurantId (FK), FirstName, LastName, Position`
- **Customers**: `CustomerId (PK), FirstName, LastName, Email, PhoneNumber`
- **Tables**: `TableId (PK), RestaurantId (FK), Capacity`
- **Reservations**: `ReservationId (PK), CustomerId (FK), RestaurantId (FK), TableId (FK), ReservationDate, PartySize`

---

## **Database Setup**

1. **Create Database**: Execute the `CreateDatabase.sql` script to create all tables and constraints.
2. **Seed Data**: Use `SeedData.sql` to populate:
   - 50 Restaurants  
   - 1000 Menu Items  
   - 500 Orders, 1500 Order Items  
   - 100 Employees  
   - 500 Reservations  
   - 400 Customers  
   - 100 Tables  

*(Fictional, consistent, and meaningful data generated using scripts.)*

---

## **Functionalities Implemented**

### **Queries & Reports**

1. Retrieve all reservations for a specific customer.
2. Retrieve all employees holding the `Manager` position.
3. List orders and associated menu items for a given reservation.
4. List menu items ordered by a specific reservation.
5. Calculate the average order amount made through a specific employee.
6. View to list all reservations with restaurant and customer info.
7. View to list all employees with their restaurant details.
8. Identify reservations with 2 or more orders using CTEs.
9. Rank restaurants by reservation frequency.
10. Identify the most popular menu item per restaurant for a given month using window functions.

### **Functions**

- **`fn_CalculateRevenue(RestaurantId)`**: Computes total revenue for a restaurant.
- **`fn_CalculateEmployeeSalary(EmployeeId)`**: Computes salary for an employee based on orders and rank.

### **Stored Procedures**

- **`sp_ResrvedTablesReport(StartDate, EndDate)`**: Report of tables reserved within a date range.
- **`sp_AddNewOrder(ReservationId, EmployeeId, OrderDate, TotalAmount)`**: Adds a new order after validation.
- **`sp_FutureReservedTables`**: Retrieves all tables with future reservations using a temp table.

### **Trigger**

- **`trg_LogTableReservation`**: Logs entries into `AuditLog` table when a reservation is created.

---

## **Performance and Optimization**

- Query plans examined for complex queries.
- Indexes applied to optimize performance for frequently queried columns.

---

## **Folder Structure**

/DatabaseProject
├── /ERD # ER Diagrams
├── /Scripts
│ ├── CreateDatabase.sql
│ ├── SeedData.sql
│ ├── Queries
│ ├── Functions
│ ├── Procedures
│ ├── Triggers
│ └── Indexes.sql
├── README.md



---

## **Technologies Used**

- **Database**: MS SQL Server  
- **Tools**: SQL Server Management Studio (SSMS), ERDPlus/Lucidchart  

---

## **Instructions to Run**

1. Open SSMS and connect to your SQL Server instance.
2. Execute `CreateDatabase.sql` to create the schema.
3. Run `SeedData.sql` to populate tables with sample data.
4. Explore queries, views, functions, and stored procedures as needed.

---

## **Author**

- **Ahmed Ghannam** 
---



