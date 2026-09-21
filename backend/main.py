from datetime import datetime, timezone, timedelta

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="이강병 개인 과제 API",
    description="개인 소개 페이지와 연동되는 FastAPI 백엔드입니다.",
    version="1.0.0",
)

# 프론트엔드(Vercel)에서 호출할 수 있도록 CORS 허용
# 배포 후에는 ["https://내-프로젝트.vercel.app"]처럼 좁혀도 됩니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

KST = timezone(timedelta(hours=9))


@app.get("/", tags=["기본"])
def root():
    """서버가 동작 중인지 확인합니다."""
    return {"status": "ok", "docs": "/docs"}


@app.get("/api/health", tags=["기본"])
def health():
    """서버 상태와 현재 시각(한국 시간)을 돌려줍니다."""
    return {
        "status": "ok",
        "server_time": datetime.now(KST).strftime("%Y-%m-%d %H:%M:%S"),
    }


@app.get("/api/hello", tags=["연동 실습"])
def hello(name: str = "방문자"):
    """이름을 받아 인사말을 돌려줍니다."""
    name = name.strip() or "방문자"
    return {"message": f"안녕하세요, {name}님! 이강병의 API에 오신 것을 환영합니다."}


@app.get("/api/profile", tags=["연동 실습"])
def profile():
    """개인 소개 정보를 돌려줍니다."""
    return {
        "name": "이강병",
        "role": "웹 개발 학습자",
        "stack": {
            "frontend": ["HTML", "CSS", "JavaScript"],
            "backend": ["Python", "FastAPI"],
            "deploy": ["Vercel", "Render", "GitHub"],
        },
    }
