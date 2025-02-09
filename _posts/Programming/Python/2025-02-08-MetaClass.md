---
title: 클래스 동적 생성(MetaClass)
categories: [Programming, Python]      # 카테고리 설정
description: ""
date: 2025-02-08 18:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [type, metaclass, custom, 클래스동적생성]  # 태그 설정
---

- [메타클래스란](#메타클래스란)
- [클래스 동적 생성](#클래스-동적-생성)
  - [클래스 동적생성 + 상속](#클래스-동적생성--상속)
  - [클래스 동적생성 + 메소드](#클래스-동적생성--메소드)
- [메타 클래스 상속](#메타-클래스-상속)
  - [커스텀 메타클래스 생성(Type 상속 X)](#커스텀-메타클래스-생성type-상속-x)
  - [커스텀 메타클래스 생성(Type 상속 O)](#커스텀-메타클래스-생성type-상속-o)


## 메타클래스란
> - [x] 클래스를 만드는 "틀"
> - [x] 클래스가 생성될 때(`__new__` → `__init__` → `__call__` 순서) 동작을 제어
> - [x] 클래스 속성/메서드 자동 추가, 네이밍 규칙 강제, 특정 부모 클래스 강제 상속 등 다양한 기능을 수행할 수 있음
> - [x] type 클래스를 상속하여 사용자 정의 메타클래스 생성

## 클래스 동적 생성
### 클래스 동적생성 + 상속
**<u>Example</u>**
```python
class ParentClass:
    pass

s_class = type(
    "Sample",
    (ParentClass,),  # 상속
    dict(attr1=1000, attr2="hi"),  # 클래스 속성
)

print(s_class)
print(type(s_class))
print(s_class.__base__)
print(s_class.__dict__)
print(s_class.attr1, s_class.attr2)
```
**<u>Output</u>**
```terminal
<class '__main__.Sample'>
<class 'type'>
<class '__main__.ParentClass'>
{'__module__': '__main__', 'attr1': 1000, 'attr2': 'hi', '__doc__': None}
```

### 클래스 동적생성 + 메소드
**<u>Example</u>**
```python
# 정적 생성(일반적인 클래스 생성)
class SampleEx(object):  
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n

    def mul(self, m, n):
        return m * n


ex = SampleEx()

print("정적 생성 클래스 : ", ex.attr1)
print("정적 생성 클래스 : ", ex.attr2)
print("정적 생성 클래스 : ", ex.add(100, 200))
print("정적 생성 클래스 : ", ex.mul(100, 200))

# ------------------------------------------------
# 동적 생성
s_class = type( 
    "Sample",
    (object,),
    dict(
        attr1=30,
        attr2=100,
        add=lambda m, n: m + n,
        mul=lambda m, n: m * n,
    ),
)


print("동적 생성 클래스 : ", s_class.attr1)
print("동적 생성 클래스 : ", s_class.attr2)
print("동적 생성 클래스 : ", s_class.add(100, 200))
print("동적 생성 클래스 : ", s_class.mul(100, 200))

```

**<u>Output</u>**
```terminal
<!-- 정적 생성 클래스 -->
정적 생성 클래스 :  30
정적 생성 클래스 :  100
정적 생성 클래스 :  300
정적 생성 클래스 :  20000

<!-- 동적 생성 클래스 -->
동적 생성 클래스 :  30
동적 생성 클래스 :  100
동적 생성 클래스 :  300
동적 생성 클래스 :  20000
```

## 메타 클래스 상속
### 커스텀 메타클래스 생성(Type 상속 X)

**<u>Example</u>**
```python
def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


# list를 상속받음, 메소드 2개 추가
CustomList1 = type(
                'CustomList1', 
                (list, ), 
                { 
                    'desc': '커스텀 리스트1', 
                    'cus_mul': cus_mul, 
                    'cus_replace': cus_replace
                }
            )

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9])
c1.cus_mul(1000)
c1.cus_replace(1000, 7777)

print('Ex1 > ', c1)    
print('Ex1 > ', c1.desc)   

print()
```

**<u>Output</u>**
```terminal
Ex1 >  [1, 2, 3, 4, 5, 6, 7, 8, 9]
Ex1 >  커스텀 리스트1
```

### 커스텀 메타클래스 생성(Type 상속 O)

**<u>Example</u>**
```python
def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new

# type 상속
# new -> init -> call 순서
class CustomListMeta(type):
    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__(metacls, name, bases, namespace):
        # 
        print("__new__ -> ", metacls, name, bases, namespace)
        namespace["desc"] = "커스텀 리스트2"
        namespace["cus_mul"] = cus_mul
        namespace["cus_replace"] = cus_replace

        return type.__new__(metacls, name, bases, namespace)

    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print("__init__ -> ", self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)

    # 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print("__call__ -> ", self, args, kwargs)

        return super().__call__(*args, **kwargs)


CustomList2 = CustomListMeta("CustomList2", (list,), {})

c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)

print("Ex2 > ", c2)
print("Ex2 > ", c2.desc)

# 상속 확인
print(CustomList2.__mro__)
```

**<u>Output</u>**
```terminal
__new__ ->  <class '__main__.CustomListMeta'> CustomList2 (<class 'list'>,) {}
__init__ ->  <class '__main__.CustomList2'> CustomList2 (<class 'list'>,) {'desc': '커스텀 리스트2', 'cus_mul': <function cus_mul at 0x104b14860>, 'cus_replace': <function cus_replace at 0x104b156c0>}
__call__ ->  <class '__main__.CustomList2'> ([1, 2, 3, 4, 5, 6, 7, 8, 9],) {}
Ex2 >  [7777, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
Ex2 >  커스텀 리스트2
(<class '__main__.CustomList2'>, <class 'list'>, <class 'object'>)
```
