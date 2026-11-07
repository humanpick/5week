import streamlit as st

# 1. 페이지 설정 (와이드 모드)
st.set_page_config(
    page_title="디지털 상품을 통한 5주 로드맵",
    page_icon="🚀",
    layout="wide",
)

# 2. 휴먼픽 디자인 시스템 표준 반영 (다크 모드, 글래스모피즘, 커스텀 CSS)
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

    /* 핵심 흐름 배너 */
    .flow-banner {
        background: rgba(139, 92, 246, 0.1);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        margin-bottom: 30px;
        font-size: 1.05rem;
    }

    /* 글래스 카드 스타일 (주차별 컨테이너) */
    .glass-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        height: 100%;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        border-color: rgba(139, 92, 246, 0.5);
    }

    /* 주차별 뱃지 */
    .week-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
        margin-bottom: 12px;
        background: linear-gradient(135deg, #8B5CF6, #EC4899);
        color: #FFFFFF;
        text-align: center;
    }

    /* 카드 내부 제목 */
    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 15px;
        line-height: 1.4;
    }

    /* 리스트 스타일 */
    .card-list {
        font-size: 0.9rem;
        color: #CBD5E1;
        margin-bottom: 20px;
        line-height: 1.6;
    }

    /* 이번 주 목표 박스 */
    .goal-box {
        background: rgba(56, 189, 248, 0.1);
        border-left: 3px solid #38BDF8;
        padding: 10px 12px;
        border-radius: 6px;
        font-size: 0.85rem;
        color: #E2E8F0;
    }

    /* 하단 핵심 원칙 카드 */
    .principle-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        height: 100%;
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
    <div class="flow-banner">
        <strong style="color: #38BDF8;">🔥 핵심 흐름 :</strong> 
        주제 선정 &nbsp;➔&nbsp; 제품 설계 &nbsp;➔&nbsp; 페이지 제작 &nbsp;➔&nbsp; 자동화 구축 &nbsp;➔&nbsp; 오픈 & 개선[cite: 1]
    </div>
    """,
    unsafe_allow_html=True,
)

# 5. 5주차 로드맵 데이터 정의
weeks_data = [
    {
        "week": "WEEK 1",
        "title": "주제 선정 & 고객 문제 찾기",
        "items": [
            "• 누구에게 왠지 꽝치의 칭하기 (예: 작은 가게 사장님, 프랑스어를 공부하는 한국 남성)",
            "• 네 노라이 릴제 좀 해설해올 수 있는 문제 1개 고르고",
            "• 이 고객이 되어 그들의 하루, 감정, 불편함 정리",
            "• 고객을 위한 사업 예시 10개 설계",
            "• 디지털 상품 종류 결정 (eBook / PDF / Checklist / Notion / 코칭 등)"
        ],
        "goal": "판매가능성 높은 주제 1개 확정[cite: 1]"
    },
    {
        "week": "WEEK 2",
        "title": "제품 구조 설계 + MVP 제작",
        "items": [
            "• 판매할 디지털 상품 구성하기",
            "• 축소 상품 기획 및 AI를 통해 만들어보기",
            "• 고객의 '작은 성공, 성과'가 나오게 설계 <b>*중요*</b>"
        ],
        "goal": "최소 기능 서비스 및 상품 구성 완료하기"
    },
    {
        "week": "WEEK 3",
        "title": "랜딩페이지 & 원리이너 작성",
        "items": [
            "• 랜딩페이지 원라이너 만들기 (존재 -> 해결 -> 성공)",
            "• 리드 제너레이터 제작 (무료 자료 / 체크리스트 만들기)",
            "• Before/After 시각화 (가능하면!)",
            "• 랜딩페이지 초안 완성",
            "• 판매할 디지털 상품 지속적으로 업데이트"
        ],
        "goal": "사람들이 “사고 싶게 만드는” 페이지 완성"
    },
    {
        "week": "WEEK 4",
        "title": "자동화 + 마케팅 시스템 구축",
        "items": [
            "• DB 수집 자동화 만들기 (타입폼, 자피어, make, 스티비, 소셜비즈, 카카오톡)",
            "• 컨텐츠 시작하기 -> 첫 시작 플랫폼 추천 (인스타, 유튜브, 블로그, 틱톡, X ...)"
        ],
        "goal": "“자동으로 팔리는 구조” 세팅 완료"
    },
    {
        "week": "WEEK 5",
        "title": "오픈 ➔ 피드백 ➔ 최종 개선",
        "items": [
            "• 첫 구매자 5명 확보 목표",
            "• 빠르게 피드백 수집",
            "• 제일 많이 묻는 5가지 -> FAQ 제작",
            "• 문제 발견하면 즉시 업데이트",
            "• 추가 3개 확보 -> 랜딩페이지 추가"
        ],
        "goal": "자동화 시스템으로 확장 확인"
    }
]

# 6. 5개의 컬럼으로 나누어 카드 형태로 완벽 배치
cols = st.columns(5)

for idx, data in enumerate(weeks_data):
    with cols[idx]:
        # 글래스모피즘 카드 컨테이너 시작
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="week-badge">{data["week"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">{data["title"]}</div>', unsafe_allow_html=True)
        
        # 상세 항목 렌더링
        items_html = "<div class='card-list'>"
        for item in data["items"]:
            items_html += f"{item}<br>"
        items_html += "</div>"
        st.markdown(items_html, unsafe_allow_html=True)
        
        # 이번 주 목표 렌더링
        st.markdown(
            f"""
            <div class="goal-box">
                🎯 <b>이번 주 목표</b><br>{data['goal']}
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

# 7. 하단 핵심 원칙 섹션
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("### 💎 핵심 원칙")
pc1, pc2, pc3, pc4 = st.columns(4)

with pc1:
    st.markdown(
        """
        <div class="principle-card">
            <strong style="color: #38BDF8;">👤 고객 중심</strong><br><br>
            <span style="font-size: 0.85rem; color: #94A3B8;">모든 진척은 고객의 문제와 성장에 집중합니다[cite: 1].</span>
        </div>
        """,
        unsafe_allow_html=True
    )
with pc2:
    st.markdown(
        """
        <div class="principle-card">
            <strong style="color: #8B5CF6;">💎 가치 우선</strong><br><br>
            <span style="font-size: 0.85rem; color: #94A3B8;">진짜 가치를 제공하고 성장을 추구합니다[cite: 1].</span>
        </div>
        """,
        unsafe_allow_html=True
    )
with pc3:
    st.markdown(
        """
        <div class="principle-card">
            <strong style="color: #EC4899;">📈 지속적 개선</strong><br><br>
            <span style="font-size: 0.85rem; color: #94A3B8;">데이터 피드백을 기반으로 계속 개선합니다[cite: 1].</span>
        </div>
        """,
        unsafe_allow_html=True
    )
with pc4:
    st.markdown(
        """
        <div class="principle-card">
            <strong style="color: #38BDF8;">⚙️ 자동화</strong><br><br>
            <span style="font-size: 0.85rem; color: #94A3B8;">시스템으로 확장합니다[cite: 1].</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# 8. 푸터
st.markdown(
    """
    <div style="text-align: center; color: #64748B; margin-top: 50px; font-size: 0.8rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 20px;">
        © 2026 Upnomad. All rights reserved. 이 로드맵은 디지털 상품으로 수익을 만들기 위한 일반적인 가이드입니다[cite: 1].
    </div>
    """,
    unsafe_allow_html=True,
)
