---
categories: [Python, Basic]      # 카테고리 설정
description: ""
date: 2025-02-01 18:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [Python, Filter, Reduce, Map, Lambda]  # 태그 설정
---

> Lambda, Reduce, Map, Filter 에 대해 학습합니다.
{: .prompt-info }

> - [x] Lambda
> - [x] Reduce
> - [x] Map
> - [x] Filter

1. Lambda
    - `lambda` : 익명 함수, 한 줄로 함수를 표현
        - 사용 즉시 소멸
        - 파이썬 가비지 컬렉션에 의해 메모리 관리 용이
        - 일반 함수 : 재사용성을 위해 메모리 저장
        - 시퀀스형 전처리에 주로 사용

    ```python
    # 일반 함수
    def mul_10(num: int) -> int:
        return num * 10

    # Lambda 함수
    lambda_mul_10 = lambda num: num * 10
    ```

2. map
    - `map(func, iterable)` : iterable의 모든 요소에 func 적용

    ```python
    # 일반 함수
    def mul_10(num: int) -> int:
        return num * 10

    # Lambda 함수
    lambda_mul_10 = lambda num: num * 10

    # map
    map_ex = map(lambda_mul_10, [1, 2, 3, 4, 5])
    print(list(map_ex))

    # map 모듈화
    def mul_10(nums: list(int)) -> object:
        def mul(num: int) -> int:
            return num * 10
        return map(mul, nums)
    
    print(list(mul_10([1, 2, 3, 4, 5])))
    ```

    **<u>Output</u>**
    ```
    [10, 20, 30, 40, 50]
    [10, 20, 30, 40, 50]
    ```

3. filter
    - `filter(func, iterable)` : iterable의 모든 요소에 func 적용 후 True인 요소만 반환

    ```python
    # filter
    filter_ex = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
    print(list(filter_ex))

    # filter 모듈화
    def filter_even(nums: list(int)) -> object:
        def even(num: int) -> bool:
            return num % 2 == 0
        return filter(even, nums)

    print(list(filter_even([1, 2, 3, 4, 5])))
    ```

    **<u>Output</u>**
    ```
    [2, 4]
    [2, 4]
    ```

4. reduce
    - `reduce(func, iterable)` : iterable의 모든 요소에 func 적용 후 누적

    ```python
    from functools import reduce

    # reduce
    reduce_ex = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
    print(reduce_ex)

    # reduce 모듈화
    def reduce_sum(nums: list(int)) -> object:
        def add(x, y) -> int:
            return x + y
        return reduce(add, nums)

    print(reduce_sum([1, 2, 3, 4, 5]))
    ```

    **<u>Output</u>**
    ```
    15
    15
    ```