import streamlit as st

# 1. 페이지 설정 (와이드 모드)
st.set_page_config(
    page_title="디지털 상품 5주 로드맵",
    page_icon="🚀",
    layout="wide",
)

# 2. 휴먼픽 디자인 시스템 표준 (다크 모드, 글래스모피즘, 커스텀 CSS)
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
        background: linear-gradient(135deg, #8B5CF6, #EC4899, #38BDF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #94A3B8;
        margin-bottom: 2rem;
    }

    /* 글래스 카드 스타일 */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        border-color: rgba(139, 92, 246, 0.4);
    }

    /* 주차별 헤더 뱃지 */
    .week-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 12px;
        background: linear-gradient(135deg, #8B5CF6, #EC4899);
        color: #FFFFFF;
    }

    /* 입력창 글씨 검은색 강제 (휴먼픽 표준) */
    input, select, textarea {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background: linear-gradient(135deg, #8B5CF6, #6366F1);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(139, 92, 246, 0.4);
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. 메인 타이틀 및 소개
st.markdown('<div class="main-title">디지털 상품을 통한 5주 로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">아이디어를 수익으로 바꾸는 5단계 시스템[cite: 1]</div>', unsafe_allow_html=True)

# 4. 핵심 흐름 요약 배너
st.markdown(
    """
    <div style="background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 12px; padding: 15px; text-align: center; margin-bottom: 30px;">
        <strong style="color: #38BDF8;">🔥 핵심 흐름:</strong> 주제 선정 ➔ 제품 설계 ➔ 페이지 제작 ➔ 자동화 구축 ➔ 오픈 & 개선[cite: 1]
    </div>
    """,
    unsafe_allow_html=True,
)

# 5. 5주차 로드맵 카드 구성 (5개 컬럼 또는 탭 레이아웃)
weeks_data = [
    {
        "week": "WEEK 1",
        "title": "주제 선정 & 고객 문제 찾기",
        "items": [
            "누구에게 왠지 꽝치의 칭하기 (예: 작은 가게 사장님, 프랑스어를 공부하는 한국 남성)",
            "네 노라이 릴제 좀 해설해올 수 있는 문제 1개 고르고",
            "이 고객이 되어 그들의 하루, 감정, 불편함 정리",
            "고객을 위한 사업 예시 10개 설계",
            "디지털 상품 종류 결정 (eBook / PDF / Checklist / Notion / 코칭 등)",
        ],
        "goal": "판매가능성 높은 주제 1개 확정",
    },
    {
        "week": "WEEK 2",
        "title": "제품 구조 설계 + MVP 제작",
        "items": [
            "판매할 디지털 상품 구성하기",
            "축소 상품 기획 및 AI를 통해 만들어보기",
            "고객의 '작은 성공, 성과'가 나오게 설계 *중요*",
        ],
        "goal": "최소 기능 서비스 및 상품 구성 원료하기",
    },
    {
        "week": "WEEK 3",
        "title": "랜딩페이지 & 원리이너 작성",
        "items": [
            "랜딩페이지 원라이너 만들기 (존재 -> 해결 -> 성공)",
            "리드 제너레이터 제작 (무료 자료 / 체크리스트 안들기)",
            "Before/After 시각화 (가능하면!)",
            "랜딩페이지 초안 완성",
            "판매할 디지털 상품 지속적으로 업데이트",
        ],
        "goal": "사람들이 “사고 싶게 만드는” 페이지 완성",
    },
    {
        "week": "WEEK 4",
        "title": "자동화 + 마케팅 시스템 구축",
        "items": [
            "DB 수집 자동화 만들기 (타입폼, 자피어, make, 스티비, 소셜비즈, 카카오톡)",
            "콘텐츠 시작하기 -> 첫 시작 플랫폼 추천 (인스타, 유튜브, 블로그, 틱톡, X ...)",
        ],
        "goal": "“자동으로 팔리는 구조” 세팅 완료",
    },
    {
        "week": "WEEK 5",
        "title": "오픈 ➔ 피드백 ➔ 최종 개선",
        "items": [
            "첫 구매자 5명 확보 목표",
            "빠르게 피드백 수집",
            "제일 많이 묻는 5가지 -> FAQ 제작",
            "문제 발견하면 즉시 업데이트",
            "추가 3개 확보 -> 랜딩페이지 추가",
        ],
        "goal": "자동화 시스템으로 확장 확인",
    },
]

# 화면을 5개의 열로 나누어 주차별 카드 배치 (모바일 호환성을 위해 탭 또는 2단으로 구성할 수도 있으나 넓은 화면용 컬럼 활용)
cols = st.columns(5)

for idx, data in enumerate(weeks_data):
    with cols[idx]:
        st.markdown(f'<div class="week-badge">{data["week"]}</div>', unsafe_allow_html=True)
        st.markdown(f"### {data['title']}")
        
        # 상세 체크리스트 항목들
        for item in data["items"]:
            st.markdown(f"- {item}")
            
        st.markdown(f"💡 **이번 주 목표:**<br>`{data['goal']}`", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 6. 하단 핵심 원칙 섹션
st.markdown("---")
st.markdown("### 💎 핵심 원칙")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("**👤 고객 중심**\n\n모든 진척은 고객의 문제와 성작에 집중합니다[cite: 1].")
with c2:
    st.markdown("**💎 가치 우선**\n\n인치 가치를 제공하고 산학을 참습니다[cite: 1].")
with c3:
    st.markdown("**📈 지속적 개선**\n\n테이터터 피트랙을 기반으로 계속 개선합니다[cite: 1].")
with c4:
    st.markdown("**⚙️ 자동화**\n\n시스템으로 확장합니다[cite: 1].")

st.markdown(
    '<div style="text-align: center; color: #64748B; margin-top: 40px; font-size: 0.85rem;">© 2026 Upnomad. All rights reserved. 이 로드맵은 디지털 상품으로 수익을 만들기 위한 일반적인 가이드입니다[cite: 1].</div>',
    unsafe_allow_html=True,
)
