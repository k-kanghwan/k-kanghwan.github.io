---
categories: [Programming, Python]      # 카테고리 설정
description: ""
date: 2025-02-03 19:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [Python, contextmanager, decorator, with구현]  # 태그 설정
---

> 📌 **목표** : contextmanager의 with문을 이해하고, 데코레이터를 사용해 함수형태로 구현하는 방법에 대해
{: .prompt-info }

> - [x] Contextlib
> - [x] With 기능 직접 구현
>     - [x] __enter__
>     - [x] __exit__
> - [x] 타이머 클래스 구현
>     - [x] Contextlib 구현
> - [x] Decorator 사용
> - [x] Contextlib.contextmanager 사용
> - [x] With 비교

## 1. Context Manager
<sup>context: 맥락, 문맥</sup>
- 원하는 타이밍에 정확하게 리소스를 할당, 제공 및 반환하는 역할
- 가장 대표적인 with 구문 이해
- 정확한 이해 후 사용이 프로그래밍 개발에 중요(문제 발생 요소 인식)
- **파일 핸들링, DB 커넥션, 소켓 처리** 등에 활용

```python
class MyWithClass(object):
    def __init__(self, ...):
        ...

    def __enter__(self): # 리소스를 할당하거나 리소스를 제공
        ...

    def __exit__(self, exc_type, exc_value, traceback): # 리소스를 반환
        # exc_type : 예외 타입
        # exc_value : 예외 값
        # traceback : 예외 발생 위치
        ...
```

   
## 2. 타이머 클래스 구현
> [ 참고 ]
> - 예외는 <u>예측 가능한 오류</u>
> - 에러는 <u>예측 불가능한 오류</u>
> - `time.monotonic` : python 3.9 이상에서 나노초 단위의 정밀도를 제공

**<u>Example</u>**
```python
import time

class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg
        self._start = None

    def __enter__(self):
        self._start = time.monotonic()  # 나노초 단위의 정밀도를 제공
        return self._start

    def __exit__(self, exc_type, value, traceback):
        if exc_type:
            print(f"Logging exception {(exc_type, value, traceback)}")
        else:
            print(f"{self._msg} : {time.monotonic() - self._start}")
        return True  # 문제없이 실행됐음을 반환하기 위해


with ExcuteTimer("Something job") as v:
    print(f"Recieved start monotonic: {v}")  # __enter__ 함수의 반환값
    # Excute job
    for i in range(10_000_000):
        pass

    # raise Exception(
    #     "Raise Exception!"
    # )  # Logging exception (<class 'Exception'>, Exception('Raise Exception!'), <traceback object at 0x104f5cbc0>)
```

## 3. contextmanager 함수 형태로 구현

```python
from contextlib import contextmanager

@contextmanager
def my_timer(msg):
    start = time.monotonic()
    try:
        yield start
    except Exception as e:
        print(f"Logging exception {e}")
    finally:
        print(f"{msg} : {time.monotonic() - start}")
```

**<u>Example</u>**
```python
with my_timer("Something job") as v:
    print(f"Recieved start monotonic: {v}")  # __enter__ 함수의 반환값
    # Excute job
    for i in range(10_000_000):
        pass

    # raise Exception(
    #     "Raise Exception!"
    # )  # Logging exception Raise Exception!
```