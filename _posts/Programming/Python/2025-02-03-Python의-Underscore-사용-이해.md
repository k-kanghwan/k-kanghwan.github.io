---
categories: [Programming, Python]      # 카테고리 설정
description: ""
date: 2025-02-03 18:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [Python, underscore]  # 태그 설정
---

> 📌 **목표** : Python의 undersocre 사용 의미에 대해 학습
{: .prompt-info }

> - [x] Python Underscore
> - [x] 다양한 언더스코어 사용
> - [x] 접근지정자 이해

## underscore
1. 인터프리터
2. 네이밍(국제화, 자릿수)
3. 값 무시

    **<u>Example</u>**
    ```python
    # Unpacking
    x, _, y = (1, 2, 3)
    print(x, y)
    # >> 1 3
    
    a, *_, b = (1, 2, 3, 4, 5)
    print(a, b)
    # >> 1 5

    for _ in range(10):
        pass
    ```

4. 접근 지정자 <sup>feat. Naming Mangling</sup>
    1. `var` : Public, 읽기 쓰기 허용
    2. `_var` : Protected, 읽기 쓰기 제한
    3. `__var` : Private, 읽기 쓰기 제한(Naming Mangling)

    **<u>Example</u>**
    ```python
    
    class SampleA:
        def __init__(self):
            self.x = 0  # Public
            self.__y = 0  # Private
            self._z = 0  # Protected


    a = SampleA()
    a.x = 1

    print(f"{a.x}")
    # >> 1
    # print(a.__y)  # AttributeError: 'SampleA' object has no attribute '__y'
    print(dir(a))
    # >> ['_SampleA__y', ..., '_z', 'x']
    ``` 
    
    >  - 언더스코어를 2개 사용하면 python 내부적으로 `_SampleA__y`로 변환하여 접근 제한
    >  - `SampleA._SampleA__y`로 접근하면 접근 가능하지만 **권장 X**
    {: .prompt-tip }