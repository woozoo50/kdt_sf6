# 사원 관리 - 조회(전체, 1건), 삽입, 수정, 삭제
import sqlite3

# 조회
def select_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')  # db에 연결
    cur = conn.cursor()  # 작업 객체 생성
    sql = "SELECT * FROM employee"
    cur.execute(sql)
    rs = cur.fetchall()  # db에 있는 자료를 모두 가져옴
    '''
    print(rs)
    print(rs[0])
    print(rs[-1])
    '''
    # 전체 조회
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = sqlite3.connect('c:/pydb/mydb.db')  # db에 연결
    cur = conn.cursor()  # 작업 객체 생성
    # 이름에 신입 포함된 사원의 정보를 검색하시오
    sql = "SELECT * FROM employee WHERE name LIKE '%신입%'"
    cur.execute(sql)
    rs = cur.fetchone()  # db에 있는 자료를 하나 가져옴
    print(rs)

# 삽입
def insert_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')  # db에 연결
    cur = conn.cursor()  # 작업 객체 생성
    sql = "INSERT INTO employee VALUES ('e105', '조대리', 4500000)"
    cur.execute(sql)
    conn.commit()  # 자료 삽입, 수정, 삭제 후에는 반드시 commit() 명시
    conn.close()

# 수정
def update_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')  # db에 연결
    cur = conn.cursor()
    # 고신입의 급여를 2500000으로 수정
    sql = "UPDATE employee SET salary = 2500000 WHERE emp_id = 'e104'"
    cur.execute(sql)
    conn.commit()
    conn.close()

# 삭제
def delete_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')  # db에 연결
    cur = conn.cursor()
    # 삭제
    sql = "DELETE FROM employee WHERE emp_id = 'e102'"
    cur.execute(sql)
    conn.commit()
    conn.close()

# 함수 호출
delete_emp()
update_emp()
# insert_emp()  # 한번 실행하면 , 다음부터 오류발생함
select_emp()  # db브라우저를 닫아야함 .. 안그러면 locked 오류 발생
select_one()
