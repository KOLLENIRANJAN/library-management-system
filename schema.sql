CREATE TABLE books (
    book_id NUMBER PRIMARY KEY,
    title VARCHAR2(100),
    author VARCHAR2(100),
    quantity NUMBER
);

CREATE TABLE library_transactions (
    transaction_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    student_id NUMBER,
    book_id NUMBER,
    issue_date DATE DEFAULT SYSDATE,
    return_date DATE,
    status VARCHAR2(20) DEFAULT 'ISSUED'
);