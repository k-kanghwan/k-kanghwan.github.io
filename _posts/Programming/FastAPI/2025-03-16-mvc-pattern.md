---
title: MVC 패턴을 활용한 FastAPI 프로젝트 구조
categories: [Programming, FastAPI]      # 카테고리 설정
description: ""
date: 2025-07-31 18:00:00 +0900    # 날짜를 정확하게 기록하기 위해
# image:                             # 포스트 이미지 설정
#     path: ""
#     alt: ""
tags: [mvc, mvc_pattern, python, fastapi]  # 태그 설정
---

> - [x] FastAPI에서 MVC 패턴을 적용한 프로젝트 구조를 이해하고 구현하기

### MVC 패턴을 활용한 FastAPI 프로젝트 구조

```plaintext
📁 project/
├── 📂 templates/                 # 🔖 HTML 템플릿 파일들
│   ├── 🏠 home.html              # 메인 페이지
│   ├── 📝 memos.html             # 메모 페이지
│   └── 🔐 login.html             # 로그인 페이지
│
├── 📂 static/                    # 🎨 정적 파일 (CSS, JS)
│   ├── 📂 css/
│   │   └── 🎨 styles.css         # 스타일 시트
│   └── 📂 js/
│       └── ⚙️ scripts.js         # 자바스크립트
│
├── 🧭 controllers.py             # 🌐 라우팅 및 API 요청 처리 (router 역할)
├── 🛢️ database.py                # 🧩 DB 연결, 세션 관리 (engine, SessionLocal, Base)
├── 🔧 dependencies.py            # 🛡️ 의존성 주입 및 인증 관련 함수 (e.g. password_hash, get_db)
├── 🚀 main.py                    # 🎯 FastAPI 앱 실행, 라우터 등록, 미들웨어 설정
├── 🧬 models.py                  # 🗃️ SQLAlchemy 모델 정의 (User, Memo 등)
└── 📦 schemas.py                 # 🧾 Pydantic 스키마 정의 (UserCreate, MemoResponse 등)
```