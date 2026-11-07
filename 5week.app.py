import datetime
import json
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import streamlit as st

# 1. 페이지 전체 설정 (와이드 레이아웃 및 탭 타이틀)
st.set_page_config(
    page_title="디지털 상품을 통한 5주 로드맵 - 휴먼픽",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. 디자인 및 UI 표준 적용 (다크 네이비, 글래스모피즘, 화이트 폼 규칙)
st.markdown(
    """
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif !important;
    }

    .stApp {
        background-color: #0B1120 !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(236, 72, 153, 0.15) 0px, transparent 50%);
        color: #FFFFFF !important;
    }

    /* 사이드바 스타일링 */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.95) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* 메인 히어로 타이틀 */
    .hero-title {
        text-align: center;
        font-size: 2.5rem;
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
        margin-bottom: 1.5rem;
    }

    /* 핵심 흐름 네온 캡슐 */
    .flow-container {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(139, 92, 246, 0.3);
        box-shadow: 0 0 20px rgba(139, 92, 246, 0.15);
        backdrop-filter: blur(12px);
        border-radius: 40px;
        padding: 12px 24px;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 0.95rem;
        font-weight: 600;
    }

    /* 카드 박스 */
    .glass-card-header {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 10px;
    }

    /* White Form 규칙: 입력창 배경 화이트, 폰트 블랙 강제 */
    input, textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }
    textarea:focus, input:focus {
        border-color: #8B5CF6 !important;
        box-shadow: 0 0 15px rgba(139, 92, 246, 0.6) !important;
    }

    /* 하단 핵심 원칙 카드 */
    .principle-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
</style>
""",
    unsafe_allow_html=True,
)

# 3. 로드맵 기본 데이터 정의
roadmap_data = [
    {
        "week": 1,
        "title": "주제 선정 & 고객문제 찾기",
        "goal": "판매가능성 높은 주제 1개 확정",
        "tasks": [
            "누구에게 닿을지 명확히 정의하기 (예: 작은 가게 사장님, 프랑스어 공부하는 한국 남성)",
            "내 노하우가 실제 풀어줄 수 있는 문제 1개 고르기",
            "이 고객이 되어 그들의 하루, 감정, 불편함 정리하기",
            "고객을 위한 사업 예시 10개 설계",
            "디지털 상품 종류 결정 (eBook / PDF / Checklist / Notion / 코칭 등)",
        ],
    },
    {
        "week": 2,
        "title": "제품 구조 설계 + MVP 제작",
        "goal": "최소 기능 서비스 및 상품 구성 완료하기",
        "tasks": [
            "판매할 디지털 상품 구성하기",
            "축소 상품 기획 및 AI를 통해 만들어보기",
            "고객의 '작은 성공, 성과' 나오게 설계 *중요*",
        ],
    },
    {
        "week": 3,
        "title": "랜딩페이지 & 원라이너 작성",
        "goal": "사람들이 '사고 싶게 만드는' 페이지 완성",
        "tasks": [
            "랜딩페이지 원라이너 만들기 (문제 -> 해결 -> 성공)",
            "리드 제너레이터 제작 (무료 자료 / 체크리스트 만들기)",
            "Before/After 시각화 (가능하면!)",
            "랜딩페이지 초안 완성",
            "판매할 디지털 상품 지속적으로 업데이트",
        ],
    },
    {
        "week": 4,
        "title": "자동화 + 마케팅 시스템 구축",
        "goal": "'자동으로 끌리는 구조' 세팅 완료",
        "tasks": [
            "DB 수집 자동화 만들기 (타입폼, 자피어, make, 스티비, 소셜비즈, 카카오톡)",
            "콘텐츠 시작하기 -> 첫 시작 플랫폼 추천 (인스타, 유튜브, 블로그, 틱톡, X 등)",
        ],
    },
    {
        "week": 5,
        "title": "오픈 -> 피드백 -> 최종 개선",
        "goal": "자동으로 셀링되는 랜딩페이지 완성",
        "tasks": [
            "첫 구매자 5명 확보 목표",
            "빠르게 피드백 수집",
            "제일 많이 묻는 5가지 -> FAQ 제작",
            "문제 발견하면 즉시 업데이트",
            "추가 3개 확보 -> 랜딩페이지 추가",
        ],
    },
]

# 4. 세션 상태 초기화 (입력값 유지)
if "tasks_state" not in st.session_state:
    st.session_state.tasks_state = {}
if "notes_state" not in st.session_state:
    st.session_state.notes_state = {}

# 5. 사이드바: 구글 시트 주소 입력 및 연동 설정
st.sidebar.title("⚙️ 구글 시트 자동 저장 설정")
sheet_url = st.sidebar.text_input(
    "구글 시트 URL 입력:",
    placeholder="https://docs.google.com/spreadsheets/d/...",
    help="데이터를 저장할 구글 시트의 웹 주소를 입력하세요.",
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
**📌 시트 사용 팁:**
1. 시트의 공유 설정을 **'링크가 있는 모든 사용자(편집자)'**로 변경하세요.
2. 아래 **'구글 시트에 데이터 저장'** 버튼을 누르면 현재 진척도와 메모가 즉시 업로드됩니다.
"""
)


# 6. 구글 시트 저장 함수
def save_to_google_sheet(url):
    try:
        # 서비스 계정 인증 (Streamlit Secrets를 이용하거나 서비스 계정이 없을 경우 gspread 퍼블릭 처리)
        # secrets에 google_credentials가 지정되어 있다면 사용, 없을 경우 기저 세팅 이용
        if "gcp_service_account" in st.secrets:
            creds = Credentials.from_service_account_info(
                st.secrets["gcp_service_account"],
                scopes=[
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive",
                ],
            )
            gc = gspread.authorize(creds)
            doc = gc.open_by_url(url)
        else:
            # 퍼블릭 오픈 시트 direct access 지원 모드
            gc = gspread.public_authorize()
            doc = gc.open_by_url(url)

        sheet = doc.get_worksheet(0)  # 첫 번째 탭 선택

        # 저장할 데이터 프레임 생성
        rows = []
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for data in roadmap_data:
            w_num = data["week"]
            total_t = len(data["tasks"])
            comp_t = sum(
                1
                for idx in range(total_t)
                if st.session_state.tasks_state.get(f"w{w_num}_t{idx}", False)
            )
            progress = (
                f"{int((comp_t / total_t) * 100)}%" if total_t > 0 else "0%"
            )
            memo = st.session_state.notes_state.get(f"week_{w_num}", "")

            rows.append(
                [
                    f"WEEK {w_num}",
                    comp_t,
                    total_t,
                    progress,
                    memo,
                    now_str,
                ]
            )

        # 데이터 업데이트
        sheet.clear()
        sheet.append_row(
            [
                "주차",
                "체크항목_완료수",
                "총_체크항목",
                "진척도",
                "전략메모",
                "최종수정시간",
            ]
        )
        for r in rows:
            sheet.append_row(r)

        return True, "성공적으로 구글 시트에 저장되었습니다!"
    except Exception as e:
        return (
            False,
            f"저장 실패: 구글 시트 공유 권한이나 URL을 확인해 주세요. ({str(e)})",
        )


# 7. 메인 헤더 & 전체 진척도
st.markdown(
    '<div class="hero-title">디지털 상품을 통한 5주 로드맵</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="hero-subtitle">아이디어를 수익으로 바꾸는 5단계 시스템</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="flow-container">
    <span style="color: #38BDF8;">🎯 핵심 흐름</span> &nbsp;&nbsp;|&nbsp;&nbsp; 
    주제 선정 &nbsp;➔&nbsp; 제품 설계 &nbsp;➔&nbsp; 페이지 제작 &nbsp;➔&nbsp; 자동화 구축 &nbsp;➔&nbsp; 오픈 & 개선
</div>
""",
    unsafe_allow_html=True,
)

# 전체 진척도 계산
total_all_tasks = sum(len(d["tasks"]) for d in roadmap_data)
completed_all_tasks = sum(
    1 for v in st.session_state.tasks_state.values() if v
)
overall_progress = (
    int((completed_all_tasks / total_all_tasks) * 100)
    if total_all_tasks > 0
    else 0
)

# 진행 상황 요약 패널
col_p1, col_p2 = st.columns([3, 1])
with col_p1:
    st.progress(overall_progress / 100)
    st.caption(
        f"전반적 진척도: **{overall_progress}%** (완료 {completed_all_tasks} / 총 {total_all_tasks}개)"
    )
with col_p2:
    if st.button("💾 구글 시트에 즉시 저장", use_container_width=True):
        if not sheet_url:
            st.warning("왼쪽 사이드바에 구글 시트 주소를 먼저 입력해 주세요!")
        else:
            with st.spinner("구글 시트로 데이터를 전송 중..."):
                success, msg = save_to_google_sheet(sheet_url)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)

st.markdown("<br>", unsafe_allow_html=True)

# 8. 5주차 로드맵 메인 카드 5열 배치
cols = st.columns(5)

for idx, data in enumerate(roadmap_data):
    w_num = data["week"]
    week_key = f"week_{w_num}"

    with cols[idx]:
        st.markdown(
            f"""
        <div class="glass-card-header">
            <span style="background: linear-gradient(135deg, #8B5CF6, #EC4899); padding: 4px 12px; border-radius: 12px; font-weight: 800; font-size: 0.8rem;">WEEK {w_num}</span>
            <h4 style="font-size: 1rem; font-weight: 700; margin-top: 10px; color: #FFFFFF;">{data['title']}</h4>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # 체크리스트 항목 생성
        for t_idx, task in enumerate(data["tasks"]):
            task_id = f"w{w_num}_t{t_idx}"
            st.session_state.tasks_state[task_id] = st.checkbox(
                task,
                value=st.session_state.tasks_state.get(task_id, False),
                key=task_id,
            )

        # 이번 주 목표 표시
        st.info(f"🎯 **이번 주 목표:**\n{data['goal']}")

        # 전략 메모 입력창 (휴먼픽 White Form 스타일 적용)
        st.session_state.notes_state[week_key] = st.text_area(
            "📝 전략 메모",
            value=st.session_state.notes_state.get(week_key, ""),
            key=f"input_{week_key}",
            placeholder="아이디어나 메모를 기록하세요...",
            height=100,
        )

# 9. 하단 핵심 원칙 섹션
st.markdown("---")
st.markdown("### 💎 핵심 원칙 (Core Principles)")

p_cols = st.columns(4)
principles = [
    ("👤 고객 중심", "#38BDF8", "모든 진행은 고객의 문제와 성과에 집중합니다."),
    ("💎 가치 우선", "#8B5CF6", "먼저 가치를 제공하고 실제 성과를 만들어 냅니다."),
    ("📈 지속적 개선", "#EC4899", "데이터와 고객 피드백을 기반으로 계속 개선합니다."),
    ("⚙️ 자동화", "#10B981", "시스템을 구축하여 비즈니스의 지속 가능성을 확보합니다."),
]

for idx, (p_title, p_color, p_desc) in enumerate(principles):
    with p_cols[idx]:
        st.markdown(
            f"""
        <div class="principle-card">
            <div style="color: {p_color}; font-weight: 700; font-size: 1rem; margin-bottom: 6px;">{p_title}</div>
            <div style="font-size: 0.8rem; color: #94A3B8; line-height: 1.4;">{p_desc}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
<div style="text-align: center; color: #475569; margin-top: 40px; font-size: 0.8rem;">
    © 2026 Upnomad. All rights reserved.
</div>
""",
    unsafe_allow_html=True,
)
