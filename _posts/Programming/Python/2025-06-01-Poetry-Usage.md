---
title: Poetry 사용법
categories: [Programming, Python]      # 카테고리 설정
description: ""
date: 2025-06-01 18:00:00 +0900
image:                             # 포스트 이미지 설정
    path: "assets/img/Git-Blog/post_poetry_resized.png"
    alt: "Poetry 사용법"
tags: [python, pypi, pyproject.toml, poetry]  # 태그 설정
---

> - [x] PyPI Package Deploy

- [Poetry 기본 사용법](#poetry-기본-사용법)
  - [Installation](#installation)
  - [프로젝트 생성](#프로젝트-생성)
    - [Poetry 기본 구조](#poetry-기본-구조)
    - [생성된 pyproject.toml 예시](#생성된-pyprojecttoml-예시)
  - [(참고)기존 프로젝트에 Poetry 적용](#참고기존-프로젝트에-poetry-적용)
- [Dependencies 설정](#dependencies-설정)
  - [terminal 명령어로 추가](#terminal-명령어로-추가)
  - [pyproject.toml 에 직접 기입](#pyprojecttoml-에-직접-기입)
  - [GitHub Repository Dependencies 설정 방법](#github-repository-dependencies-설정-방법)
  - [Local Dependencies 설정 방법](#local-dependencies-설정-방법)
- [Poetry로 PyPI Package Deploy](#poetry로-pypi-package-deploy)
  - [준비사항](#준비사항)
  - [`pyproject.toml` 설정](#pyprojecttoml-설정)
  - [PyPI 토큰 정보 저장](#pypi-토큰-정보-저장)
  - [PyPI Package Deploy](#pypi-package-deploy)


## Poetry 기본 사용법

### Installation

```terminal 
pip install poetry
```
### 프로젝트 생성

```terminal
cd C:\Users\kh.Cha\Documents\poetry-test
poetry new my_package
```

#### Poetry 기본 구조

```plaintext 
└─my_package
    │  pyproject.toml
    │  README.md
    │
    ├─src
    │  └─my_package
    │          __init__.py
    │
    └─tests
            __init__.py
```

#### 생성된 pyproject.toml 예시

```toml
[project]
name = "my-package"
version = "0.1.0"
description = ""
authors = [
    {name = "author",email = "author@example.com"}
]
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
]

[tool.poetry]
packages = [{include = "my_package", from = "src"}]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

### (참고)기존 프로젝트에 Poetry 적용

```terminal
cd {your_project_directory}
poetry init
```

## Dependencies 설정

### terminal 명령어로 추가
```terminal 
poetry add requests beautifulsoup4 numpy pandas
```

### pyproject.toml 에 직접 기입
- `>=2.25.1,<3.0.0`: 이 버전 범위는 `2.25.1` 이상 `3.0.0` 미만의 버전을 의미

```toml     
[project]
dependencies = [
    "requests (>=2.25.1,<3.0.0)",
    "beautifulsoup4 (>=4.9.3,<5.0.0)",
    "numpy (>=1.19.5,<2.0.0)",
    "pandas (>=1.1.5,<2.0.0)"
]
```

### GitHub Repository Dependencies 설정 방법
- GitHub에서 호스팅되는 패키지를 의존성으로 추가
- 이 경우, `@` 기호를 사용하여 Git URL을 지정

```toml
[project]
# ...
dependencies = [
    "requests @ git+https://github.com/requests/requests.git",
]
```

### Local Dependencies 설정 방법
- 로컬 디렉토리에 있는 패키지를 의존성으로 추가
```toml
[project]
# ...   
dependencies = [
    "my-local-package @ file:///path/to/my-local-package"
]
```

## Poetry로 PyPI Package Deploy
### 준비사항
1. poetry 설치
2. PyPI 계정 생성 
3. 패키지명 중복 확인

### `pyproject.toml` 설정

```toml
[project]
name = "my-package"
version = "0.1.1"
description = "My Python Package"
authors = [
    {name = "kh.cha",email = "example@example.com"}
]
license = "MIT"
readme = "README.md"
# homepage = ""
# repository = ""
requires-python = ">=3.9"
dependencies = [
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

### PyPI 토큰 정보 저장

```terminal
poetry config pypi-token.pypi <your-pypi-token>
```

### PyPI Package Deploy
- `toml`의 패키지이름과 src 폴더의 패키지 이름이 일치해야 함

```terminal
poetry build
poetry publish --build
```