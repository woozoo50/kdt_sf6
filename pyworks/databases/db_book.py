# 도서 관리 db
# 방식 - 동적 바인딩 방식('?' 기호 사용)
# DB의 레코드(행)의 자료형은 튜플 '()'
# 요소가 1개일때 (a, ) - 콤마를 찍어야 함

import sqlite3

#테이블 생성 - book

def getconn():
    conn = sqlite3.connect('./output/bookdb.db')
    return conn

def create_book():
    # db가 없으면 생성되고 있으면 연결됨
    conn = getconn()
    cursor = conn.cursor() # 작업 객체
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """
    cursor.execute(sql)
    conn.commit() # 파이썬에서는 commit 해줘야함
    conn.close()

def insert_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? - 동적 바인딩 기호
    sql = "INSERT INTO book (title, author, price) VALUES (?, ?, ?)"
    cursor.execute(sql, ("점프 투 파이썬", "박응용", 19800))  # 자료 구조는 튜플로
    conn.commit()
    conn.close()

def select_book():
    conn = getconn()
    cursor = getconn().cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    conn.close()

def select_one():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"  # 동적
    cursor.execute(sql, (2,))  # 요소가 1개일때 (a, ) - 콤마를 찍어야 함
    rs = cursor.fetchone()
    print(rs)
    conn.close()

def update_book():
    conn = getconn()
    cursor = conn.cursor()
    sql = "UPDATE book SET price = ? WHERE title = ?"  # 동적
    cursor.execute(sql, (15000, "천개의 파랑"))  # 순서 맞추는것 주의
    conn.commit()
    conn.close()

def delete_book():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"  # 동적
    cursor.execute(sql, (1, ))  # 요소가 1개일때 (a, ) - 콤마를 찍어야 함
    conn.commit()
    conn.close()

# 실행 영역
# create_book()
# insert_book()
# update_book()
# delete_book()
select_book()
# select_one()
