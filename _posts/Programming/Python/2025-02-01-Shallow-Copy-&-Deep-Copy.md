---
categories: [Programming, Python]      # 카테고리 설정
description: ""
date: 2025-02-01 19:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [python, shallow, deep, copy, shallow-copy, deep-copy]  # 태그 설정
---

> Shallow Copy 와 Deep Copy 에 대해 
{: .prompt-info }

> - [x] Shallow Copy
> - [x] Deep Copy   

## 가변 / 불변 타입
    - **mutable : list, dict, set**
    - immutable : int, float, str, tuple
<br>

## Copy 종류
### 1. **Reference Copy** : 주소값 복사
```python
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print(id(a_list))
print(id(b_list))

b_list[2] = 100
print(a_list)
print(b_list)
```

**<u>Output</u>**
```terminal
4380083712
4380083712

[1, 2, 100, [4, 5, 6], [7, 8, 9]]  # b_list 수정 시 a_list 도 수정됨
[1, 2, 100, [4, 5, 6], [7, 8, 9]]
```

### 2. **Shallow Copy** : 가변형 <u>객체 안의 객체는 같은 주소값</u>을 참조

```python
import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print(id(c_list))
print(id(d_list))
d_list[2] = 100
d_list[3][1] = 1000
d_list[4][1] = 1000

print(c_list)
print(d_list)
```

**<u>Output</u>**
```terminal
4380083712
4380083840

# ⭐️ 객체 안의 객체는 같은 주소값을 참조
[1, 2, 3, [4, 1000, 6], [7, 1000, 9]]
[1, 2, 100, [4, 1000, 6], [7, 1000, 9]]
```

### 3. **Deep Copy** : 값 복사

```python
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

print(id(e_list))
print(id(f_list))

f_list[3].append(100)
f_list[4][1] = 100000

print(e_list)
print(f_list)
```

**<u>Output</u>**
```terminal
4380083712
4380083840

# ⭐️ 객체 안의 객체는 다른 주소값을 참조
[1, 2, 3, [4, 5, 6], [7, 8, 9]]
[1, 2, 3, [4, 5, 6, 100], [7, 100000, 9]]
```



> 📖 Summary
> - Copy 의 종류에 대해 이해하지 못한다면 디버깅이 힘들어질 수 있음
{: .prompt-warning }
