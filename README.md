# FeedBack Scoring MBTI AI

피드백 스코어링 및 MBTI 기반 피드백 개선 AI 프로젝트

## 프로젝트 개요

이 프로젝트는 매니저가 제공한 피드백을 AI가 분석하고 개선하여, 받는 사람의 MBTI 유형에 맞게 조정하는 시스템을 구현합니다. 또한 피드백의 품질을 객관적인 기준에 따라 점수화합니다.

### 주요 기능

1. **피드백 개선**: 매니저가 제공한 원본 피드백을 더 효과적이고 구체적인 피드백으로 개선
2. **MBTI 맞춤화**: 피드백 수신자의 MBTI 유형에 맞게 커뮤니케이션 스타일 조정
3. **피드백 점수화**: 피드백의 품질을 여러 기준(구체성, 균형, 성장 지향성 등)에 따라 평가

## 프로젝트 구조

```
.
├── src/                    # 소스 코드
│   ├── data/               # 데이터 처리 모듈
│   ├── models/             # AI 모델 관련 코드
│   ├── utils/              # 유틸리티 함수
│   ├── api/                # API 엔드포인트
│   ├── config/             # 설정 파일
│   ├── tests/              # 테스트 코드
│   ├── feedback_generator/ # 피드백 생성 모듈
│   ├── mbti_adapter/       # MBTI 적응 모듈
│   └── scoring_engine/     # 점수화 엔진
├── .env                    # 환경 변수 (API 키 등)
├── .gitignore              # Git 무시 파일 목록
├── pyproject.toml          # 프로젝트 의존성 관리
└── README.md               # 프로젝트 문서
```

## 설치 및 실행

### 필수 요구사항

- Python 3.11 이상
- Poetry (의존성 관리)
- OpenAI API 키

### 설치 방법

```bash
# 저장소 복제
git clone https://github.com/jo-on-hee/FeedBack_Scoring_MBTI_AI.git
cd FeedBack_Scoring_MBTI_AI

# 의존성 설치
poetry install

# 환경 변수 설정
cp .env.example .env
# .env 파일에 API 키 등 필요한 정보 입력
```

### 실행 방법

```bash
poetry run python src/main.py
```

## 협업 가이드라인

### 브랜치 전략

- `main`: 안정적인 릴리스 버전
- `develop`: 개발 중인 코드 통합
- 기능 브랜치: `feature/기능명`
- 버그 수정: `bugfix/버그명`

### 개발 워크플로우

1. 이슈 생성 및 할당
2. 기능 브랜치 생성 (`git checkout -b feature/기능명`)
3. 코드 개발 및 테스트
4. Pull Request 생성
5. 코드 리뷰 및 승인
6. `develop` 브랜치에 병합
7. 정기적으로 `develop`에서 `main`으로 병합

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새 브랜치를 생성합니다 (`git checkout -b feature/기능명`).
3. 변경사항을 커밋합니다 (`git commit -m '새로운 기능 추가'`).
4. 브랜치를 푸시합니다 (`git push origin feature/기능명`).
5. Pull Request를 생성합니다.

## 라이센스

MIT
