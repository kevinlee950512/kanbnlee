# 이강병 개인 소개 페이지 & 프론트엔드·백엔드 연동

개인 소개 페이지를 HTML로 만들고, FastAPI로 구현한 백엔드 API를 프론트엔드에서 호출해 결과를 보여 주는 개인 과제입니다.

## 배포 주소

| 구분 | 주소 |
| --- | --- |
| 개인 소개 페이지 (Vercel) | https://your-project.vercel.app |
| API 연동 실습 페이지 (Vercel) | https://your-project.vercel.app/api.html |
| 백엔드 Swagger UI (Render) | https://your-backend.onrender.com/docs |

> Render 무료 플랜은 한동안 요청이 없으면 잠들기 때문에, 첫 호출에 30초~1분 정도 걸릴 수 있습니다.

## 주요 구성

```
.
├── README.md
├── backend/              # Render 배포
│   ├── main.py           # FastAPI 앱
│   └── requirements.txt
└── frontend/             # Vercel 배포
    ├── index.html        # 개인 소개 페이지
    └── api.html          # API 연동 실습 페이지
```

| 영역 | 사용 기술 | 배포 |
| --- | --- | --- |
| 프론트엔드 | HTML, CSS, JavaScript (fetch) | Vercel |
| 백엔드 | Python, FastAPI, Uvicorn | Render |
| 소스 관리 | Git, GitHub | GitHub |

두 페이지는 서로 링크로 연결되어 있어, 소개 페이지의 "API 연동 실습 보기" 버튼으로 실습 페이지에 들어가고 실습 페이지 상단 링크로 돌아올 수 있습니다.

## API 목록

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| GET | `/api/health` | 서버 상태와 현재 시각(한국 시간) |
| GET | `/api/hello?name=이름` | 입력한 이름으로 인사말 반환 |
| GET | `/api/profile` | 이강병의 소개 정보 반환 |

## 로컬 실행

```bash
# 백엔드
cd backend
pip install -r requirements.txt
uvicorn main:app --reload        # http://127.0.0.1:8000/docs

# 프론트엔드 (다른 터미널)
cd frontend
python -m http.server 5500       # http://127.0.0.1:5500
```

로컬에서 테스트할 때는 `frontend/api.html`의 `API_BASE`를 `http://127.0.0.1:8000`으로 바꿔 주세요.

## 배포 설정

**Render (백엔드)**
- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Vercel (프론트엔드)**
- Root Directory: `frontend`
- Framework Preset: `Other`
