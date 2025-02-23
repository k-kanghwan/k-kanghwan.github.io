---
title: PyPI 배포
categories: [Programming, Python]      # 카테고리 설정
description: ""
date: 2025-02-23 18:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [python, pypi, pyproject.toml]  # 태그 설정
---

> - [x] PyPI Package Deploy

- [패키지 디렉토리 구성](#패키지-디렉토리-구성)
- [패키지 배포 순서(PyPI) ⭐️](#패키지-배포-순서pypi-️)
- [setup.py -\> pyproject.toml(최신 반영)](#setuppy---pyprojecttoml최신-반영)
- [pyproject.toml vs setup.py](#pyprojecttoml-vs-setuppy)


### 패키지 디렉토리 구성

- Python 패키지를 배포하기 위해 다음과 같은 디렉토리를 구성

```
├── package_name  # 배포하고자 하는 패키지의 이름 (실제 코드가 포함됨)
│   ├── __init__.py  # 패키지 초기화 파일 (해당 디렉토리를 패키지로 인식하게 함)
├── .gitignore  # Git에 포함하지 않을 파일 목록 (예: .pyc, __pycache__/ 등)
├── LICENSE  # 라이선스 파일 (MIT, Apache 2.0, GPL 3.0 등)
├── MANIFEST.in  # 배포 시 포함할 추가 파일을 지정하는 설정 파일
├── README.md  # 프로젝트 설명 및 사용 방법을 포함하는 파일
├── requirements.txt  # 프로젝트에서 필요한 패키지 목록
├── setup.cfg  # setup.py를 보완하는 설정 파일 (선택 사항)
├── setup.py  # 패키지 배포 설정 파일 (패키지 메타데이터 및 설치 정보 포함)
```

### 패키지 배포 순서(PyPI) ⭐️

1. PyPI 회원가입 및 ***API 토큰*** 생성 
    [https://pypi.org](https://pypi.org)
2. 프로젝트 구조 확인
    앞서 설명한 디렉토리 구조에 맞게 프로젝트를 구성
3. __init__.py 작성
    패키지 디렉토리 내부에 `__init__.py` 파일을 생성, ***Python이 해당 디렉토리를 패키지로 인식***
4. 프로젝트 루트파일 작성
    - README.md → 프로젝트 설명 (마크다운 문법 지원)
    - setup.py → 패키지 설정 및 배포 정보 포함
    - setup.cfg → setup.py의 보완 설정 파일 (선택 사항)
    - LICENSE → 라이선스 정보 포함
    - MANIFEST.in → 배포 시 포함할 추가적인 파일 명시
5. 패키지 빌드(설치 패키지 생성)
    패키지 배포를 위해 빌드(`setuptools`, `wheel`) 
    1. 필수 패키지 설치

        ```terminal
        python -m pip install setuptools wheel
        ```

        또는 
        ```terminal
        python -m pip install --user --upgrade setuptools wheel
        ```
    
    2. 패키지 빌드 실행
        ```terminal
        python setup.py sdist bdist_wheel
        ```

        📌 실행 후 생성되는 디렉토리
        - build/ → 빌드 관련 임시 파일 저장
        - dist/ → 배포할 .tar.gz 및 .whl 파일 저장
        - package_name.egg-info/ → 패키지 메타데이터 저장

        📌 빌드 옵션
        - sdist → Source Distribution (소스 코드 압축본)
        - bdist_wheel → Binary Distribution (바이너리 실행 파일)

6. PyPI 업로드
    패키지를 PyPI에 업로드 하기위해 twine 패키지 설치
    1. Twine 설치

        ```terminal
        python -m pip install twine
        ```

    2. 패키지 업로드

        ```terminal
        python -m twine upload dist/*
        ```

6. 패키지 설치 확인
    배포된 패키지를 정상적으로 설치하고 사용할 수 있는지 확인

    1. PyPI에서 설치

        ```terminal
        pip install package_name
        ```

    2. Github에서 설치

        ```terminal
        pip install git+https://www.github.com/...
        ```
    
    3. 패키지 정상 동작 확인

        ```python
        from package_name import module_name
        ``` 

### setup.py -> pyproject.toml(최신 반영)

- 최근 setup.py 대신 pyproject.toml 파일 사용을 권고함으로써 toml 사용법 정리

1. pyproject.toml 기본 구조
    - [build-system] → 패키지 빌드를 위해 필요한 라이브러리 (setuptools, wheel 등)
    - [project] → 패키지 메타데이터 (name, version, description 등)
    - dependencies → 패키지 설치 시 필요한 의존성 목록 (pip install 시 자동 설치됨)

    ```toml
    [build-system]
    requires = ["setuptools", "wheel"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "mypackage"
    version = "0.1.0"
    description = "This is a sample Python package."
    authors = [{ name = "Your Name", email = "your.email@example.com" }]
    license = { text = "MIT" }
    readme = "README.md"
    dependencies = [
        "requests",
        "numpy>=1.21.0",
    ]
    ...
    ```

2. `setup.py`없이 패키지 빌드하기
    1. 빌드 도구
        
        ```terminal
        pip install build
        ```

    2. 빌드 실행

        ```terminal
        python -m build
        ```
    
    📌 실행 후 dist/ 폴더에 .tar.gz 및 .whl 파일 생성됨.

### pyproject.toml vs setup.py

|             | pyproject.toml           | setup.py                          |
| ----------- | ------------------------ | --------------------------------- |
| 파일 형식   | TOML (설정 전용)         | Python 코드                       |
| 가독성      | 직관적이고 단순          | Python 코드 작성 필요             |
| 의존성 관리 | dependencies에 직접 정의 | install_requires 사용             |
| 빌드 실행   | python -m build          | python setup.py sdist bdist_wheel |
