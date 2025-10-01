# MAG Database Project

This project contains SQL and NoSQL scripts developed for a university assignment related to the **Monash Art Gallery (MAG)** database.  
The tasks cover schema creation, data manipulation, relational algebra, advanced SQL queries, JSON output, and MongoDB implementation.

---

## Contents

### Task 1 – Schema (`T1-mag-schema.sql`)
- Defines the missing tables:
  - **AW_DISPLAY**
  - **AW_STATUS**
  - **SALE**
- Includes constraints:
  - Primary keys
  - Unique constraints
  - Check constraints
  - Foreign keys to `artist`, `artwork`, `customer`, and `gallery` tables:contentReference[oaicite:0]{index=0}.

---

### Task 2 – Insert Data (`T2-mag-insert.sql`)
- Populates **AW_DISPLAY**, **AW_STATUS**, and **SALE** tables.
- Provides 10 display entries and 4+ sales.
- Includes artwork transit and gallery status events:contentReference[oaicite:1]{index=1}.

---

### Task 3 – DML (`T3-mag-dml.sql`)
- Sequence creation for IDs.
- Insert a new artwork and record its statuses.
- Demonstrates transit, display, and sale lifecycle.
- Updates display end dates when artworks are sold.
- Includes delete operations with proper rollback handling:contentReference[oaicite:2]{index=2}.

---

### Task 4 – Modifications (`T4-mag-mods.sql`)
- Creates **TOTAL_ARTWORKS** table to track artwork counts per artist.
- Creates **CUSTOMER_PURCHASE** table to track purchases by customer per artist.
- Inserts data into these tables using queries with joins and groupings:contentReference[oaicite:3]{index=3}.

---

### Task 5 – SQL Queries (`T5-mag-select.sql`)
- Complex SELECT statements:
  - Artists without phone numbers in certain regions.
  - Customer purchases in specific galleries.
  - Artworks returned after 60+ days.
  - Sale benefits and commission calculations.
  - Revenue percentage of galleries with “most/least profitable” markers:contentReference[oaicite:4]{index=4}.

---

### Task 6 – JSON & MongoDB
- **SQL JSON (`T6-mag-json.sql`)**  
  - Generates JSON objects per artist with nested artworks and details:contentReference[oaicite:5]{index=5}.  

- **MongoDB (`T6-mag-mongo.mongodb.js`)**  
  - Creates a collection `monashart`.
  - Inserts multiple artist documents with embedded artworks.
  - Queries artists with certain artwork counts or price conditions.
  - Demonstrates updates using `$push` and `$set`:contentReference[oaicite:6]{index=6}.

---

### Task 7 – Relational Algebra (`T7-mag-ra.pdf`)
- Provides algebraic solutions to relational queries such as:
  - Customers living in specific regions.
  - Artworks displayed in certain galleries within given dates:contentReference[oaicite:7]{index=7}.

---

## Requirements
- **Oracle SQL** (for schema, insert, DML, mods, selects, JSON SQL).
- **MongoDB** (for NoSQL operations).
- PDF reader (for relational algebra write-up).

---

## How to Run
1. Run `T1-mag-schema.sql` in Oracle SQL Developer to create schema.
2. Execute `T2-mag-insert.sql` to populate initial data.
3. Use `T3-mag-dml.sql` for additional inserts and DML operations.
4. Apply `T4-mag-mods.sql` to create extra analytic tables.
5. Run queries in `T5-mag-select.sql` for analysis.
6. Use `T6-mag-json.sql` to test SQL JSON functions.
7. Use `T6-mag-mongo.mongodb.js` in MongoDB shell for NoSQL tasks.
8. Refer to `T7-mag-ra.pdf` for relational algebra query explanations.

---

## Author
- **Name**: Robiatul Adawiyah Al-Qosh

