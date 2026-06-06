import oracledb

# Database connection setup
conn = oracledb.connect(
    user="system",
    password="Oracle@123",  # Replace with your actual password
    dsn="localhost/XE"
)
cursor = conn.cursor()

def issue_book():
    print("\n--- Issue a Book ---")
    try:
        sid = int(input("Enter Student ID: "))
        bid = int(input("Enter Book ID: "))
        
        # Check if book is available
        cursor.execute("SELECT quantity FROM books WHERE book_id = :1", (bid,))
        result = cursor.fetchone()
        
        if not result:
            print("❌ Book ID not found in inventory.")
            return
        
        available_qty = result[0]
        if available_qty <= 0:
            print("❌ Copy unavailable. All units are currently issued.")
            return
            
        # Log allocation history workflow
        cursor.execute(
            "INSERT INTO library_transactions (student_id, book_id) VALUES (:1, :2)",
            (sid, bid)
        )
        
        # Real-time inventory adjustment (Decrease book count)
        cursor.execute(
            "UPDATE books SET quantity = quantity - 1 WHERE book_id = :1",
            (bid,)
        )
        
        conn.commit()
        print("✅ Book Issued Successfully and Inventory Adjusted!")
    except Exception as e:
        print(f"❌ Transaction failed: {e}")

def return_book():
    print("\n--- Return a Book ---")
    try:
        tx_id = int(input("Enter Transaction ID: "))
        
        # Verify transaction status
        cursor.execute("SELECT book_id, status FROM library_transactions WHERE transaction_id = :1", (tx_id,))
        result = cursor.fetchone()
        
        if not result:
            print("❌ Invalid Transaction ID.")
            return
        if result[1] == 'RETURNED':
            print("ℹ️ This book has already been marked returned.")
            return
            
        bid = result[0]
        
        # Update transaction log entry
        cursor.execute(
            "UPDATE library_transactions SET return_date = SYSDATE, status = 'RETURNED' WHERE transaction_id = :1",
            (tx_id,)
        )
        
        # Real-time inventory adjustment (Increase book count)
        cursor.execute(
            "UPDATE books SET quantity = quantity + 1 WHERE book_id = :1",
            (bid,)
        )
        
        conn.commit()
        print("✅ Book Returned Successfully and Inventory Replenished!")
    except Exception as e:
        print(f"❌ Operation failed: {e}")

def view_records():
    print("\n--- Active Allocation Logs ---")
    cursor.execute("SELECT transaction_id, student_id, book_id, issue_date, status FROM library_transactions")
    rows = cursor.fetchall()
    for row in rows:
        print(f"TxID: {row[0]} | StudentID: {row[1]} | BookID: {row[2]} | Date: {row[3]} | Status: {row[4]}")

# Insert mock inventory books if tables are empty
cursor.execute("SELECT COUNT(*) FROM books")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO books VALUES (501, 'Core Python Programming', 'R. Nageswara', 5)")
    cursor.execute("INSERT INTO books VALUES (502, 'Database System Concepts', 'Korth', 3)")
    conn.commit()

# Main Application Menu Loop
while True:
    print("\n===== Library Management System =====")
    print("1. Issue Book (Log Transaction)")
    print("2. Return Book (Replenish Stock)")
    print("3. View History Records")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    if choice == "1":
        issue_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        view_records()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")

cursor.close()
conn.close()