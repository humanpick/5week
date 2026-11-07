import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="디지털 상품 5주 로드맵 - Humanpick",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 맨 처음 오리지널 디자인 시스템 CSS 이식
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif !important;
    }

    .stApp {
        background-color: #0B1120 !important;
        color: #FFFFFF !important;
    }

    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1450px !important;
    }

    /* 메인 타이틀 */
    .hero-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 50%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #94A3B8;
        font-weight: 500;
        margin-bottom: 2rem;
    }

    /* 상단 핵심 흐름 바 (원본 이미지 스타일 100% 구현) */
    .flow-pill-box {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(56, 189, 248, 0.3);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.1);
        backdrop-filter: blur(12px);
        border-radius: 40px;
        padding: 12px 24px;
        text-align: center;
        margin-bottom: 3rem;
        font-size: 0.95rem;
        font-weight: 600;
        color: #E2E8F0;
    }
    .flow-badge-tag {
        background: rgba(56, 189, 248, 0.15);
        color: #38BDF8;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
        margin-right: 10px;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }
    .flow-arrow {
        color: #10B981;
        font-weight: 800;
        margin: 0 8px;
    }

    /* 5주차 글래스 카드 (오리지널 디자인) */
    .roadmap-glass-card {
        background: rgba(17, 28, 51, 0.75);
        border: 1.5px solid rgba(16, 185, 129, 0.3);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-radius: 20px;
        padding: 22px 18px;
        height: 100%;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.3s ease;
    }
    .roadmap-glass-card:hover {
        border-color: rgba(16, 185, 129, 0.7);
        transform: translateY(-5px);
    }

    /* 주차별 뱃지 */
    .week-pill {
        background: linear-gradient(135deg, #0D9488 0%, #10B981 100%);
        color: #FFFFFF;
        font-weight: 800;
        font-size: 0.85rem;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }

    .card-heading-text {
        font-size: 1.1rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 16px;
        line-height: 1.35;
        min-height: 48px;
    }

    .checklist-row {
        font-size: 0.85rem;
        color: #CBD5E1;
        line-height: 1.6;
        margin-bottom: 8px;
    }

    /* 이번 주 목표 박스 */
    .goal-inner-box {
        background: #0B1120;
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 12px;
        padding: 12px;
        margin-top: 16px;
    }
    .goal-inner-title {
        color: #10B981;
        font-size: 0.75rem;
        font-weight: 800;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .goal-inner-desc {
        color: #F1F5F9;
        font-size: 0.85rem;
        font-weight: 600;
    }

    /* 하단 핵심 원칙 그리드 카드 */
    .principle-box-item {
        background: rgba(17, 28, 51, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border-radius: 14px;
        padding: 18px 14px;
        text-align: center;
        height: 100%;
    }

    /* 불필요한 UI 숨김 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. 헤더 섹션
st.markdown('<div class="hero-title">디지털 상품을 통한 5주 로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">아이디어를 수익으로 바꾸는 5단계 시스템[cite: 1]</div>', unsafe_allow_html=True)

# 4. 상단 핵심 흐름 바 (원본 이미지와 완벽히 일치하는 화살표 흐름)
st.markdown("""
<div class="flow-pill-box">
    <span class="flow-badge-tag">🎯 핵심 흐름</span> 
    주제 선정 <span class="flow-arrow">➔</span> 제품 설계 <span class="flow-arrow">➔</span> 페이지 제작 <span class="flow-arrow">➔</span> 자동화 구축 <span class="flow-arrow">➔</span> 오픈 & 개선[cite: 1]
</div>
""", unsafe_allow_html=True)

# 5. 5주차 데이터 구성 (원본 내용 100% 유지)
weeks = [
    {
        "week": "WEEK 1",
        "title": "주제 선정 &<br>고객 문제 찾기",
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
        "title": "제품 구조 설계<br>+ MVP 제작",
        "items": [
            "• 판매할 디지털 상품 구성하기[cite: 1]",
            "• 축소 상품 기획 및 AI를 통해 만들어보기[cite: 1]",
            "• 고객의 '작은 성공, 성과'가 나오게 설계 <b>*중요*</b>[cite: 1]"
        ],
        "goal": "최소 기능 서비스 및 상품 구성 완료하기"
    },
    {
        "week": "WEEK 3",
        "title": "랜딩페이지 &<br>원라이너 작성",
        "items": [
            "• 랜딩페이지 원라이너 만들기 (존재 ➔ 해결 ➔ 성공)[cite: 1]",
            "• 리드 제너레이터 제작 (무료 자료 / 체크리스트 만들기)[cite: 1]",
            "• Before/After 시각화 (가능하면!)[cite: 1]",
            "• 랜딩페이지 초안 완성[cite: 1]",
            "• 판매할 디지털 상품 지속적으로 업데이트[cite: 1]"
        ],
        "goal": "사람들이 “사고 싶게 만드는” 페이지 완성"
    },
    {
        "week": "WEEK 4",
        "title": "자동화 + 마케팅<br>시스템 구축",
        "items": [
            "• DB 수집 자동화 만들기 (타입폼, 자피어, make, 스티비, 소셜비즈, 카카오톡)[cite: 1]",
            "• 콘텐츠 시작하기 ➔ 첫 시작 플랫폼 추천 (인스타, 유튜브, 블로그, 틱톡, X ...)[cite: 1]"
        ],
        "goal": "“자동으로 팔리는 구조” 세팅 완료"
    },
    {
        "week": "WEEK 5",
        "title": "오픈 ➔ 피드백 ➔<br>최종 개선",
        "items": [
            "• 첫 구매자 5명 확보 목표[cite: 1]",
            "• 빠르게 피드백 수집[cite: 1]",
            "• 제일 많이 묻는 5가지 ➔ FAQ 제작[cite: 1]",
            "• 문제 발견하면 즉시 업데이트[cite: 1]",
            "• 추가 3개 확보 ➔ 랜딩페이지 추가[cite: 1]"
        ],
        "goal": "자동화 시스템으로 확장 확인"
    }
]

# 6. 5열 격자 배치
cols = st.columns(5)

for idx, data in enumerate(weeks):
    with cols[idx]:
        items_html = "".join([f'<div class="checklist-row">{item}</div>' for item in data["items"]])
        
        st.markdown(f"""
        <div class="roadmap-glass-card">
            <div>
                <div><span class="week-pill">{data['week']}</span></div>
                <div class="card-heading-text">{data['title']}</div>
                <div>{items_html}</div>
            </div>
            <div class="goal-inner-box">
                <div class="goal-inner-title">💡 이번 주 목표</div>
                <div class="goal-inner-desc">{data['goal']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 7. 하단 핵심 원칙 섹션
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: #FFFFFF; font-weight: 700; margin-bottom: 20px;'>💎 핵심 원칙</h3>", unsafe_allow_html=True)

p_cols = st.columns(4)
principles = [
    ("👤 고객 중심", "#38BDF8", "모든 진척은 고객의 문제와 성장에 집중합니다.[cite: 1]"),
    ("💎 가치 우선", "#10B981", "진짜 가치를 제공하고 성장을 추구합니다.[cite: 1]"),
    ("📈 지속적 개선", "#EC4899", "데이터 피드백을 기반으로 계속 개선합니다.[cite: 1]"),
    ("⚙️ 자동화", "#8B5CF6", "시스템으로 확장하고 자동화합니다.[cite: 1]")
]

for idx, (title, color, desc) in enumerate(principles):
    with p_cols[idx]:
        st.markdown(f"""
        <div class="principle-box-item">
            <div style="color: {color}; font-weight: 700; font-size: 1rem; margin-bottom: 8px;">{title}</div>
            <div style="font-size: 0.8rem; color: #94A3B8; line-height: 1.4;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# 8. 푸터
st.markdown("""
<div style="text-align: center; color: #475569; margin-top: 50px; padding-bottom: 20px; font-size: 0.75rem;">
    © 2022 Upnomad. All rights reserved. 이 로드맵은 디지털 상품으로 수익을 만들기 위한 일반적인 가이드입니다.[cite: 1]
</div>
""", unsafe_allow_html=True)
