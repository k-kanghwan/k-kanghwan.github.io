---
title: 파이썬코드에서 SQL 파라미터 바인딩
categories: [Programming, Database]      # 카테고리 설정
description: ""
date: 2025-03-29 09:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [db, database, sql, python, sql-injection]  # 태그 설정
---

> - [x] sql injection 방지를 위한 파라미터 바인딩

### 기존 SQL 쿼리문
```python
sql = "SELECT * FROM user_info WHERE USER_ID = '" + str(user_id) + "'"
```

- `user_id = "1; DROP TABLE user_info"` 이와 같은 방식으로 SQL Injection 공격이 가능

### 파라미터 바인딩
```python
sql = """
SELECT * FROM user_info
WHERE USER_ID = %s
"""
params = (user_id,)  # 튜플로 묶어줌
db_cursor.execute(sql, params)  # SQL 쿼리문과 파라미터를 함께 전달
```

- SQL Injection 공격을 방지하기 위해 **파라미터 바인딩**을 사용
    - 장점
        - SQL Injection 공격 방지
        - 코드 가독성 향상
    - 단점
        - DBMS나 라이브러리에 따라 `?` 또는 `%s`를 사용해야 함
            - `?`는 SQLite, `%s`는 MySQL, PostgreSQL 등에서 사용
        - 디버깅 시 실제 쿼리 확인이 어려움
        - WHERE 절이 여러조건이거나, 동적조건일때 파라미터 바인딩을 사용하기 어려움
 

