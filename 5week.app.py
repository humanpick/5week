import streamlit as st

# 1. 페이지 설정 (와이드 모드)
st.set_page_config(
    page_title="디지털 상품을 통한 5주 로드맵",
    page_icon="🚀",
    layout="wide",
)

# 2. 오리지널 이미지 스타일 반영 CSS (사이버펑크 다크 + 에메랄드/그린 테마 포인트)
st.markdown(
    """
    <style>
    /* 전체 배경 및 폰트 설정 */
    .stApp {
        background-color: #0B1120;
        color: #FFFFFF;
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 상단 타이틀 스타일 */
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 0.3rem;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #94A3B8;
        margin-bottom: 1.5rem;
    }

    /* 상단 핵심 흐름 바 (초록빛 포인트) */
    .flow-bar {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 12px;
        padding: 12px 20px;
        text-align: center;
        margin-bottom: 35px;
        font-size: 1rem;
        color: #E2E8F0;
    }

    /* 주차별 카드 컨테이너 (초록빛 에메랄드 테두리 & 글래스모피즘) */
    .roadmap-card {
        background: #111C33;
        border: 2px solid #0D9488;
        border-radius: 20px;
        padding: 20px;
        height: 100%;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        position: relative;
    }

    /* WEEK 뱃지 (초록빛 그라데이션) */
    .week-badge {
        display: block;
        text-align: center;
        padding: 8px 0;
        border-radius: 30px;
        font-weight: 800;
        font-size: 0.95rem;
        margin-bottom: 15px;
        background: linear-gradient(135deg, #0D9488, #10B981);
        color: #FFFFFF;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }

    /* 카드 내부 타이틀 */
    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 15px;
        text-align: center;
        line-height: 1.4;
        min-height: 50px;
    }

    /* 리스트 항목 스타일 */
    .card-list {
        font-size: 0.85rem;
        color: #CBD5E1;
        margin-bottom: 20px;
        line-height: 1.6;
    }
    .card-list p {
        margin-bottom: 8px;
    }

    /* 이번 주 목표 박스 */
    .goal-box {
        background: #0B1120;
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 10px;
        padding: 12px;
        text-align: center;
    }
    .goal-title {
        font-size: 0.75rem;
        color: #10B981;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .goal-content {
        font-size: 0.85rem;
        color: #F1F5F9;
        font-weight: 600;
    }

    /* 하단 핵심 원칙 카드 스타일 */
    .principle-box {
        background: #111C33;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. 타이틀 섹션
st.markdown('<div class="main-title">디지털 상품을 통한 5주 로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">아이디어를 수익으로 바꾸는 5단계 시스템[cite: 1]</div>', unsafe_allow_html=True)

# 4. 핵심 흐름 바 (주제 선정 -> 제품 설계 -> 페이지 제작 -> 자동화 구축 -> 오픈 & 개선)
st.markdown(
    """
    <div class="flow-bar">
        <span style="color: #10B981; font-weight: bold;">🎯 핵심 흐름</span> &nbsp;|&nbsp; 
        주제 선정 &nbsp;➔&nbsp; 제품 설계 &nbsp;➔&nbsp; 페이지 제작 &nbsp;➔&nbsp; 자동화 구축 &nbsp;➔&nbsp; 오픈 & 개선[cite: 1]
    </div>
    """,
    unsafe_allow_html=True,
)

# 5. 5주차 데이터 정의 (원본 이미지 내용 100% 반영)
weeks_data = [
    {
        "week": "WEEK 1",
        "title": "주제 선정 & 고객 문제 찾기",
        "items": [
            "• 누구에게 왠지 꽝치의 칭하기 (예: 작은 가게 사장님, 프랑스어를 공부하는 한국 남성)[cite: 1]",
            "• 네 노라이 릴제 좀 해설해올 수 있는 문제 1개 고르고[cite: 1]",
            "• 이 고객이 되어 그들의 하루, 감정, 불편함 정리[cite: 1]",
            "• 고객을 위한 사업 예시 10개 설계[cite: 1]",
            "• 디지털 상품 종류 결정 (eBook / PDF / Checklist / Notion / 코칭 등)[cite: 1]"
        ],
        "goal": "판매가능성 높은 주제 1개 확정[cite: 1]"
    },
    {
        "week": "WEEK 2",
        "title": "제품 구조 설계 + MVP 제작",
        "items": [
            "• 판매할 디지털 상품 구성하기[cite: 1]",
            "• 축소 상품 기획 및 AI를 통해 만들어보기[cite: 1]",
            "• 고객의 '작은 성공, 성과'가 나오게 설계 <b>*중요*</b>[cite: 1]"
        ],
        "goal": "최소 기능 서비스 및 상품 구성 완료하기"
    },
    {
        "week": "WEEK 3",
        "title": "랜딩페이지 & 원리이너 작성",
        "items": [
            "• 랜딩페이지 원라이너 만들기 (존재 -> 해결 -> 성공)[cite: 1]",
            "• 리드 제너레이터 제작 (무료 자료 / 체크리스트 만들기)[cite: 1]",
            "• Before/After 시각화 (가능하면!)[cite: 1]",
            "• 랜딩페이지 초안 완성[cite: 1]",
            "• 판매할 디지털 상품 지속적으로 업데이트[cite: 1]"
        ],
        "goal": "사람들이 “사고 싶게 만드는” 페이지 완성"
    },
    {
        "week": "WEEK 4",
        "title": "자동화 + 마케팅 시스템 구축",
        "items": [
            "• DB 수집 자동화 만들기 (타입폼, 자피어, make, 스티비, 소셜비즈, 카카오톡)[cite: 1]",
            "• 컨텐츠 시작하기 -> 첫 시작 플랫폼 추천 (인스타, 유튜브, 블로그, 틱톡, X ...)[cite: 1]"
        ],
        "goal": "“자동으로 팔리는 구조” 세팅 완료"
    },
    {
        "week": "WEEK 5",
        "title": "오픈 ➔ 피드백 ➔ 최종 개선",
        "items": [
            "• 첫 구매자 5명 확보 목표[cite: 1]",
            "• 빠르게 피드백 수집[cite: 1]",
            "• 제일 많이 묻는 5가지 -> FAQ 제작[cite: 1]",
            "• 문제 발견하면 즉시 업데이트[cite: 1]",
            "• 추가 3개 확보 -> 랜딩페이지 추가[cite: 1]"
        ],
        "goal": "자동화 시스템으로 확장 확인"
    }
]

# 6. 5개의 컬럼으로 나누어 카드 배치
cols = st.columns(5)

for idx, data in enumerate(weeks_data):
    with cols[idx]:
        st.markdown('<div class="roadmap-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="week-badge">{data["week"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{data["title"]}</div>', unsafe_allow_html=True)
        
        # 리스트 렌더링
        list_html = '<div class="card-list">'
        for item in data["items"]:
            list_html += f"<p>{item}</p>"
        list_html += "</div>"
        st.markdown(list_html, unsafe_allow_html=True)
        
        # 이번 주 목표 렌더링
        st.markdown(
            f"""
            <div class="goal-box">
                <div class="goal-title">💡 이번 주 목표</div>
                <div class="goal-content">{data['goal']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

# 7. 하단 핵심 원칙 섹션 (원본 이미지 하단 내용 100% 반영)
st.markdown("<br><br>", unsafe_allow_html=True)

p_cols = st.columns(4)
principles = [
    ("👤 고객 중심", "모든 진척은 고객의 문제와 성장에 집중합니다[cite: 1]."),
    ("💎 가치 우선", "인치 가치를 제공하고 산학을 참습니다[cite: 1]."),
    ("📈 지속적 개선", "테이터터 피트랙을 기반으로 계속 개선합니다[cite: 1]."),
    ("⚙️ 자동화", "시스템으로 확장합니다[cite: 1].")
]

for idx, (p_title, p_desc) in enumerate(principles):
    with p_cols[idx]:
        st.markdown(
            f"""
            <div class="principle-box">
                <div style="color: #10B981; font-weight: 700; margin-bottom: 8px; font-size: 1rem;">{p_title}</div>
                <div style="font-size: 0.8rem; color: #94A3B8; line-height: 1.4;">{p_desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# 8. 푸터
st.markdown(
    """
    <div style="text-align: center; color: #64748B; margin-top: 40px; font-size: 0.75rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 20px;">
        © 2022 Upnomad. All rights reserved. 이 로드맵은 디지털 상품으로 수익을 만들기 위한 일반적인 가이드입니다[cite: 1].
    </div>
    """,
    unsafe_allow_html=True,
)
