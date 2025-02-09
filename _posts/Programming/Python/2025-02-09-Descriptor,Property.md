---
title: Descriptor vs Property
categories: [Programming, Python]      # 카테고리 설정
description: ""
date: 2025-02-09 15:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [python, descriptor, set, get, del, property]  # 태그 설정
---

> - [x] Decriptor, Property
> - [x] Get, Set, Del 구현

- [프로퍼티 클래스 - 사용 클래스 별도 구현](#프로퍼티-클래스---사용-클래스-별도-구현)
- [Property 사용해서 Descriptor 직접 구현](#property-사용해서-descriptor-직접-구현)
- [Descriptor 사용 예제 (1) - non-data descriptor](#descriptor-사용-예제-1---non-data-descriptor)
- [Descriptor 사용 예제 (2) - data descriptor](#descriptor-사용-예제-2---data-descriptor)


### Descriptor란?
1. 객체에서 ***다른 객체를 속성값으로 가지는 것***
2. 특정 클래스의 ***속성을 관리하고 제어하는 특별한 객체***
3. Read(`__get__`), Write(`__set__`), Delete(`__delete__`) 등을 미리 정의 가능
4. ★data descriptor(*set **or** del* 구현된 객체), non-data descriptor(*get*만 구현된 객체)
5. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능

## 프로퍼티 클래스 - 사용 클래스 별도 구현

**<u>Example</u>**
```python
class DescriptorEx1(object):
    def __init__(self, name="Default"):
        self.name = name

    def __get__(self, obj, obj_type):
        return f"Get method called. -> self : {self}, obj : {obj}, obj_type : {obj_type}, name: {self.name}"

    def __set__(self, obj, name):
        print("Set method called.")
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string.")

    def __delete__(self, obj):
        print("Delete Method called.")
        self.name = None

class Sample1(object):
    name = DescriptorEx1()

s1 = Sample1()

# __set__ 호출
s1.name = "Descriptor Test1"

# 예외 발생 - __set__ 메소드의 제약조건으로 인해
# s1.name = 10  # TypeError: Name should be string.

# attr 확인
# __get__ 호출
print(s1.name)

# __delete__ 호출
del s1.name

# 재확인
# __get__ 호출
print(s1.name)
```

**<u>Output</u>**
```terminal
Set method called.
Get method called. -> self : <__main__.DescriptorEx1 object at 0x102316ad0>, obj : <__main__.Sample1 object at 0x1023179d0>, obj_type : <class '__main__.Sample1'>, name: Descriptor Test1
Delete Method called.
Get method called. -> self : <__main__.DescriptorEx1 object at 0x102316ad0>, obj : <__main__.Sample1 object at 0x1023179d0>, obj_type : <class '__main__.Sample1'>, name: None
```

## Property 사용해서 Descriptor 직접 구현
- ***Descriptor vs Property***
    1. Descriptor : 더 유연하지만 복잡한 방식(커스텀 로직 구현 가능)
        - `__get__`, `__set__`, `__delete__` 메소드 구현
    2. **<u>Property </u> : 더 간단한 방식(`property()`로 쉽게 속성 관리 가능)**
        - `property(fget, fset, fdel, doc)` 메소드 구현
- 프로퍼티 클래스와 사용 클래스가 동일 클래스 안에 존재
- class property : `property(fget, fset, fdel, doc)`
    - `fget` : get method
    - `fset` : set method
    - `fdel` : delete method
    - `doc` : docstring

**<u>Example</u>**
```python
class DescriptorEx2(object):
    def __init__(self, value):
        self._name = value

    def getVal(self):
        return f"Get method called. -> self : {self}, name : {self._name}"

    def setVal(self, value):
        print("Set method called.")
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Value shold be string.")

    def delVal(self):
        print("Delete method called.")
        self._name = None

    # property(fget=None, fset=None, fdel=None, doc)
    name = property(getVal, setVal, delVal, "Property Method Example")  #

s2 = DescriptorEx2("Descriptor Test2")
print(s2.name)

# setVal 호출
s2.name = "Changed - Descript test2 Method."

# 예외 발생 - __set__ 메소드의 제약조건으로 인해
# s2.name = 10  # TypeError: Value shold be string.

# delVal 호출
del s2.name
print(s2.name)

# Doc 호출
print(DescriptorEx2.name.__doc__)
```

**<u>Output</u>**
```terminal
Get method called. -> self : <__main__.DescriptorEx2 object at 0x1031d3ad0>, name : Descriptor Test2
Set method called.
Delete method called.
Get method called. -> self : <__main__.DescriptorEx2 object at 0x1031d3ad0>, name : None
Property Method Example
```


## Descriptor 사용 예제 (1) - non-data descriptor

**<u>Example</u>**
```python
import os

class DirectoryFileCount:  # `__get__`만 구현한 경우는 Non-data descriptor
    def __get__(self, obj, obj_type=None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))

class DirectoryPath:
    # Descriptor instance
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname

# 현재 경로
s = DirectoryPath("./")

# 이전 경로
g = DirectoryPath("../")

print(f"s.size : {s.size}")
print(f"g.size : {g.size}")
```

**<u>Output</u>**
```terminal
<!-- DirectoryFileCount 의 __get__ method 내용 -->
[current_file1.txt, current_file2.txt, ...]
s.size : 11

[parent_file1.txt, parent_file2.txt, ...]
g.size : 3
```

## Descriptor 사용 예제 (2) - data descriptor

**<u>Example</u>**
```python
import logging
import inspect

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

class LoggedScoreAccess:
    """학생 점수를 관리하는 디스크립터"""

    def __get__(self, obj, obj_type=None):
        if obj:
            value = getattr(obj, "_score", 50)  # 기본값 50
            logging.info("Accessing 'score' of %r, current value: %r", obj.name, value)
            return value
        return self  # 클래스 레벨 접근 방지

    def __set__(self, obj, value):
        """교사만 학생 점수를 변경할 수 있도록 제한"""
        stack = inspect.stack()
        caller_names = [frame.function for frame in stack]

        if "update_score" not in caller_names:
            raise PermissionError("Only teachers can modify scores!")

        prev_value = getattr(obj, "_score", 50)
        setattr(obj, "_score", value)
        logging.info("Updated 'score' of %r from %r to %r", obj.name, prev_value, value)

class Student:
    score = LoggedScoreAccess()

    def __init__(self, name):
        self.name = name

class Teacher:
    def update_score(self, student, value):
        """교사만 학생 점수를 변경할 수 있도록 보장"""
        if not isinstance(student, Student):
            raise ValueError("Invalid student instance")

        prev_value = student.score  # 현재 점수 가져오기
        student.score = value  # 점수 업데이트
        logging.info(
            "Teacher updated 'score' of %r from %r to %r",
            student.name,
            prev_value,
            value,
        )

# --테스트 코드--
s1 = Student("L")
s2 = Student("H")
teacher = Teacher()

# 학생 점수 조회
print(f"조회 s1 : {s1.score}")  # 50
print(f"조회 s2 : {s2.score}")  # 50

# 교사가 점수 수정
teacher.update_score(s1, 80)
teacher.update_score(s2, 90)

# 수정된 점수 확인
print(f"수정 s1 : {s1.score}")  # 80
print(f"수정 s2 : {s2.score}")  # 90

# 학생 수정 방지 테스트
try:
    s1.score = 100  # 학생이 직접 수정 시도할 경우 예외 발생
except PermissionError as e:
    print(f"예외 발생: {e}")
```

**<u>Output</u>**
```terminal
2025-02-09 15:02:22 [INFO] Accessing 'score' of 'L', current value: 50
조회 s1 : 50
2025-02-09 15:02:22 [INFO] Accessing 'score' of 'H', current value: 50
조회 s2 : 50
2025-02-09 15:02:22 [INFO] Accessing 'score' of 'L', current value: 50
2025-02-09 15:02:22 [INFO] Updated 'score' of 'L' from 50 to 80
2025-02-09 15:02:22 [INFO] Teacher updated 'score' of 'L' from 50 to 80
2025-02-09 15:02:22 [INFO] Accessing 'score' of 'H', current value: 50
2025-02-09 15:02:22 [INFO] Updated 'score' of 'H' from 50 to 90
2025-02-09 15:02:22 [INFO] Teacher updated 'score' of 'H' from 50 to 90
2025-02-09 15:02:22 [INFO] Accessing 'score' of 'L', current value: 80
수정 s1 : 80
2025-02-09 15:02:22 [INFO] Accessing 'score' of 'H', current value: 90
수정 s2 : 90
예외 발생: Only teachers can modify scores!
```

