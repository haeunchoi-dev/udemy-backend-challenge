import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect("book.db")

# 열 정의
columns = [
    "id INTEGER PRIMARY KEY",
    "title VARCHAR",
    "author VARCHAR",
    "publishedDate VARCHAR",
    "publisher VARCHAR",
    "price INTEGER",
    "genre VARCHAR",
    "description VARCHAR"
]

# 테이블 생성 SQL 명령어 작성
create_table_cmd = f"CREATE TABLE book ({','.join(columns)})"
conn.execute(create_table_cmd)

# 삽입할 책 데이터 (예시 데이터)
books = [
    "NULL, 'Java Book', 'Author A', '20241013', 'Publisher A', 25000, 'Programming', 'Java programming guide'",
    "NULL, 'Python Book', 'Author B', '20231013', 'Publisher B', 30000, 'Programming', 'Python for beginners'"
]

# 각 책 데이터를 테이블에 삽입
for book in books:
    insert_cmd = f"INSERT INTO book VALUES ({book})"
    conn.execute(insert_cmd)

# 변경 사항 커밋
conn.commit()

# 테이블에서 모든 데이터 선택
cur = conn.cursor()
cur.execute("SELECT * FROM book")

# 결과 가져오기 및 출력
books = cur.fetchall()
for book in books:
    print(book)

# 연결 종료
conn.close()
