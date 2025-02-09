---
categories: [Programming, Python]      # 카테고리 설정
description: ""
date: 2025-02-07 18:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [overriding, overloading, oop, 다형성, multipledispatch]  # 태그 설정
---

- [Overriding](#overriding)
  - [Overriding 효과](#overriding-효과)
  - [Overriding 강제](#overriding-강제)
- [Overloading](#overloading)
  - [Overloading 효과](#overloading-효과)
  - [Overloading 예제](#overloading-예제)
    - [한 클래스 내에서 동일한 함수명을 사용한다면?](#한-클래스-내에서-동일한-함수명을-사용한다면)
    - [자료형에 따른 분기 처리로 해결](#자료형에-따른-분기-처리로-해결)
    - [외부 패키지 `multipledispatch` 사용](#외부-패키지-multipledispatch-사용)


## Overriding
> 오버라이딩은 부모 클래스에서 정의한 메소드를 자식 클래스에서 재정의(덮어쓰기)하는 것 
{: .prompt-info }
> - [x] Overriding
> - [x] OOP
> - [x] 다형성 예제


### Overriding 효과
1. 서브클래스(자식)에서 슈퍼클래스(부모)를 호출 후 사용
    > super().메소드명()    
2. 코드의 재사용성 증가
3. 부모 클래스의 메소드를 추상화 후 사용 가능(구조적 접근)
4. 유지보수성과 확장성 향상
5. 가독성 증가, 오류가능성 감소, 메소드 이름 절약, 유지보수성 증가 등

**<u>Example</u>**
```python
# 부모 클래스
class Notifier:
    def notify(self, message):
        print(f"Notification: {message}")

# 자식 클래스
class EmailNotifier(Notifier):
    def notify(self, message):
        formatted_msg = f"[EMAIL] {message}"
        super().notify(formatted_msg)  # 부모 클래스 메소드 호출

class SMSNotifier(Notifier):
    def notify(self, message):
        formatted_msg = f"[SMS] {message}"
        super().notify(formatted_msg)

class PushNotifier(Notifier):
    def notify(self, message):
        formatted_msg = f"[PUSH] {message}"
        super().notify(formatted_msg)

# 객체 생성 및 테스트
notifier = Notifier()
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
push_notifier = PushNotifier()

notifier.notify("System maintenance at midnight.")
email_notifier.notify("You have a new email.")
sms_notifier.notify("Your OTP code is 123456.")
push_notifier.notify("New friend request received.")

```

**<u>Output</u>**
```terminal
Notification: System maintenance at midnight.
Notification: [EMAIL] You have a new email.
Notification: [SMS] Your OTP code is 123456.
Notification: [PUSH] New friend request received.
```


### Overriding 강제

**<u>Example</u>**
```python
from abc import ABC, abstractmethod

# 추상 클래스 선언
class Parent(ABC):
    @abstractmethod
    def must_override(self):
        """반드시 오버라이딩해야 하는 메서드"""
        pass

# 자식 클래스에서 반드시 오버라이딩해야 함
class Child(Parent):
    def must_override(self):
        print("자식 클래스에서 구현한 메서드")

# 정상적인 사용
child = Child()
child.must_override()  # 출력: 자식 클래스에서 구현한 메서드

# 아래 코드 실행 시 오류 발생 (오버라이딩하지 않음)
class InvalidChild(Parent):
    pass

invalid_child = (
    InvalidChild()
)  # TypeError: Can't instantiate abstract class InvalidChild
```

**<u>Output</u>**
```terminal
자식 클래스에서 구현한 메서드
Traceback (most recent call last):
    File "overriding.py", line 25, in <module>
        InvalidChild()
TypeError: Can't instantiate abstract class InvalidChild with abstract method must_override
```

## Overloading
> 오버로딩은 같은 이름의 메소드를 매개변수의 개수 또는 타입에 따라 다르게 정의하는 것을 의미
{: .prompt-info }

### Overloading 효과
> - [x] 동일 메소드 재정의
> - [x] 네이밍으로 기능 예측
> - [x] 코드 절약, 가독성 향상
> - [x] 메소드 파라미터 기반 호출 방식


### Overloading 예제
#### 한 클래스 내에서 동일한 함수명을 사용한다면?
```python

class SampleA(object):

    def add(self, x, y):
        return x + y

    def add(self, x, y, z):  # add 함수가 덮어씌워짐
        return x + y + z


a = SampleA()
# print(a.add(2, 3))  # TypeError: SampleA.add() missing 1 required positional argument: 'z'
```

#### 자료형에 따른 분기 처리로 해결

```python
class SampleB(object):
    def add(self, data_type, *args):
        if data_type == "int":
            return sum(args)
        if data_type == "str":
            return "".join([x for x in args])
```

#### 외부 패키지 `multipledispatch` 사용
- `pip install multipledispatch`
- Annotation을 사용하여 메소드 오버로딩 가능
- 인수 개수에 따라 해당 메소드 호출

```python
from multipledispatch import dispatch

class SampleC(object):
    @dispatch(int, int)  # Annotation
    def add(self, x, y):
        print("- Called int add")
        return x + y

    @dispatch(int, int, int)
    def add(self, x, y, z):
        print("- Called int add with 3 params")
        return x + y + z

    @dispatch(str, str, str)
    def add(self, x, y, z):
        print("- Called str add")
        return x + y + z

c = SampleC()
print(c.add(1, 2))
print(c.add(1, 2, 3))
print(c.add("Hello", "World", "Python"))
```

**<u>Output</u>**
```terminal
- Called int add
3
- Called int add with 3 params
6
- Called str add
HelloWorldPython
```