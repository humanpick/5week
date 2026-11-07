import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="디지털 상품 5주 로드맵 - Humanpick",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 맨 처음 HTML 디자인 시스템 1:1 이식 (Cyberpunk Glassmorphism CSS)
st.markdown("""
<style>
    /* Pretendard 폰트 불러오기 및 기본 스타일 초기화 */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;
    }

    .stApp {
        background-color: #0B1120 !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(236, 72, 153, 0.15) 0px, transparent 50%);
        color: #FFFFFF !important;
    }

    /* 패딩 최적화 */
    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1400px !important;
    }

    /* 메인 히어로 타이틀 */
    .hero-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #FFFFFF 0%, #38BDF8 50%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1.15rem;
        color: #94A3B8;
        font-weight: 500;
        margin-bottom: 2rem;
    }

    /* 핵심 흐름 네온 캡슐 */
    .flow-container {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(139, 92, 246, 0.3);
        box-shadow: 0 0 20px rgba(139, 92, 246, 0.15);
        backdrop-filter: blur(12px);
        border-radius: 50px;
        padding: 14px 28px;
        text-align: center;
        margin-bottom: 2.5rem;
        font-size: 1rem;
        font-weight: 600;
    }
    .flow-highlight {
        color: #38BDF8;
        font-weight: 700;
    }

    /* 글래스모피즘 메인 5주차 카드 */
    .glass-card-box {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-radius: 20px;
        padding: 24px 20px;
        height: 100%;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .glass-card-box:hover {
        transform: translateY(-6px);
        border-color: rgba(139, 92, 246, 0.5);
        box-shadow: 0 12px 40px 0 rgba(139, 92, 246, 0.25);
    }

    /* 주차 헤더 뱃지 */
    .week-header-badge {
        background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%);
        color: #FFFFFF;
        font-weight: 800;
        font-size: 0.85rem;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3);
    }

    .card-heading {
        font-size: 1.15rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 16px;
        line-height: 1.35;
        min-height: 48px;
    }

    /* 체크리스트 스타일 */
    .checklist-item {
        font-size: 0.88rem;
        color: #CBD5E1;
        line-height: 1.6;
        margin-bottom: 10px;
        padding-left: 4px;
    }

    /* 이번 주 목표 박스 (글로우 서식) */
    .goal-banner {
        background: rgba(56, 189, 248, 0.08);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 12px;
        padding: 12px 14px;
        margin-top: 16px;
    }
    .goal-banner-title {
        color: #38BDF8;
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .goal-banner-desc {
        color: #F1F5F9;
        font-size: 0.85rem;
        font-weight: 600;
        line-height: 1.3;
    }

    /* 하단 핵심 원칙 그리드 바 */
    .principle-card-v2 {
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border-radius: 14px;
        padding: 18px 14px;
        text-align: center;
        height: 100%;
        transition: border-color 0.2s;
    }
    .principle-card-v2:hover {
        border-color: rgba(56, 189, 248, 0.4);
    }
    .principle-icon-title {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .principle-desc {
        font-size: 0.82rem;
        color: #94A3B8;
        line-height: 1.4;
    }

    /* 상하단 메뉴 영구 숨김 (Humanpick 스타일) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. 헤더 섹션
st.markdown('<div class="hero-title">디지털 상품을 통한 5주 로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">아이디어를 수익으로 바꾸는 5단계 시스템[cite: 1]</div>', unsafe_allow_html=True)

# 4. 핵심 흐름 라인
st.markdown("""
<div class="flow-container">
    <span class="flow-highlight">🎯 핵심 흐름</span> &nbsp;&nbsp;|&nbsp;&nbsp; 
    주제 선정 &nbsp;➔&nbsp; 제품 설계 &nbsp;➔&nbsp; 페이지 제작 &nbsp;➔&nbsp; 자동화 구축 &nbsp;➔&nbsp; 오픈 & 개선[cite: 1]
</div>
""", unsafe_allow_html=True)

# 5. 5주차 데이터 구성 (원본 원문 100% 유지)
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

# 6. 5열 격자 배치 (글래스모피즘 네온 스타일 반영)
cols = st.columns(5)

for idx, data in enumerate(weeks):
    with cols[idx]:
        items_html = "".join([f'<div class="checklist-item">{item}</div>' for item in data["items"]])
        
        st.markdown(f"""
        <div class="glass-card-box">
            <div>
                <div><span class="week-header-badge">{data['week']}</span></div>
                <div class="card-heading">{data['title']}</div>
                <div>{items_html}</div>
            </div>
            <div class="goal-banner">
                <div class="goal-banner-title">🎯 이번 주 목표</div>
                <div class="goal-banner-desc">{data['goal']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 7. 하단 핵심 원칙 섹션
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: #F8FAFC; font-weight: 700; margin-bottom: 20px;'>💎 핵심 원칙</h3>", unsafe_allow_html=True)

p_cols = st.columns(4)
principles = [
    ("👤 고객 중심", "#38BDF8", "모든 진척은 고객의 문제와 성장에 집중합니다.[cite: 1]"),
    ("💎 가치 우선", "#8B5CF6", "진짜 가치를 제공하고 성장을 추구합니다.[cite: 1]"),
    ("📈 지속적 개선", "#EC4899", "데이터 피드백을 기반으로 계속 개선합니다.[cite: 1]"),
    ("⚙️ 자동화", "#10B981", "시스템으로 확장하고 자동화합니다.[cite: 1]")
]

for idx, (title, color, desc) in enumerate(principles):
    with p_cols[idx]:
        st.markdown(f"""
        <div class="principle-card-v2">
            <div class="principle-icon-title" style="color: {color};">{title}</div>
            <div class="principle-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# 8. 푸터
st.markdown("""
<div style="text-align: center; color: #475569; margin-top: 60px; padding-bottom: 20px; font-size: 0.8rem;">
    © 2026 Upnomad. All rights reserved. 이 로드맵은 디지털 상품으로 수익을 만들기 위한 가이드입니다.[cite: 1]
</div>
""", unsafe_allow_html=True)
