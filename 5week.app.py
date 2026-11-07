import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 전체 설정 (와이드 레이아웃)
st.set_page_config(
    page_title="디지털 상품을 통한 5주 로드맵 - 휴먼픽",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. 스타일 초기화 CSS
st.markdown(
    """
<style>
    .main .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    header, footer, #MainMenu {
        display: none !important;
        visibility: hidden !important;
    }
    body {
        background-color: #0B1120;
    }
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        color: #FFFFFF !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    section[data-testid="stSidebar"] label {
        color: #E2E8F0 !important;
        font-weight: 600 !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# 3. HTML/JS 기반 대시보드 컴포넌트 (LocalStorage 자동 저장 + 구글 시트 바로가기 버튼 포함)
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>디지털 상품을 통한 5주 로드맵</title>
  
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Pretendard', '-apple-system', 'BlinkMacSystemFont', 'system-ui', 'Roboto', 'sans-serif'],
          },
          colors: {
            cyberDark: '#0B1120',
            cyberCard: 'rgba(15, 23, 42, 0.65)',
            accentPurple: '#8B5CF6',
            accentPink: '#EC4899',
            accentBlue: '#38BDF8',
            accentGreen: '#10B981',
          },
        }
      }
    }
  </script>

  <style>
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #0B1120; }
    ::-webkit-scrollbar-thumb { background: rgba(139, 92, 246, 0.4); border-radius: 4px; }
    
    .glass-panel {
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .glass-card {
      background: rgba(30, 41, 59, 0.5);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card:hover {
      border-color: rgba(139, 92, 246, 0.5);
      transform: translateY(-4px);
      box-shadow: 0 10px 30px -10px rgba(139, 92, 246, 0.3);
    }
    .neon-focus:focus {
      outline: none;
      box-shadow: 0 0 15px rgba(139, 92, 246, 0.6);
      border-color: #8B5CF6;
    }
    .custom-checkbox {
      appearance: none;
      background-color: rgba(255, 255, 255, 0.05);
      width: 1.25em; height: 1.25em;
      border: 1.5px solid rgba(255, 255, 255, 0.3);
      border-radius: 0.35em;
      display: grid; place-content: center; cursor: pointer;
      transition: all 0.2s ease;
    }
    .custom-checkbox::before {
      content: ""; width: 0.65em; height: 0.65em; transform: scale(0);
      transition: 120ms transform ease-in-out;
      box-shadow: inset 1em 1em #EC4899;
      clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
    }
    .custom-checkbox:checked {
      border-color: #EC4899; background: rgba(236, 72, 153, 0.15);
    }
    .custom-checkbox:checked::before { transform: scale(1); }
    .completed-text { text-decoration: line-through; color: #64748B !important; }
  </style>
</head>

<body class="bg-cyberDark text-slate-100 font-sans min-h-screen relative overflow-x-hidden">

  <div class="fixed -top-40 -left-40 w-96 h-96 bg-accentPurple/20 rounded-full blur-[120px] pointer-events-none"></div>
  <div class="fixed top-1/2 -right-40 w-96 h-96 bg-accentPink/15 rounded-full blur-[140px] pointer-events-none"></div>

  <div class="max-w-[1440px] mx-auto px-4 py-6 md:px-8 md:py-8 flex flex-col gap-6 relative z-10">

    <!-- Header -->
    <header class="glass-panel rounded-2xl p-6 md:p-8 flex flex-col md:flex-row justify-between items-center gap-6 border-slate-800">
      <div class="text-center md:text-left space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-accentPurple/10 border border-accentPurple/30 text-accentPurple text-xs font-semibold uppercase mb-1">
          <i class="fa-solid fa-rocket text-xs"></i> 휴먼픽 디지털 시스템
        </div>
        <h1 class="text-2xl md:text-4xl font-extrabold tracking-tight text-white">
          디지털 상품을 통한 <span class="text-transparent bg-clip-text bg-gradient-to-r from-accentPurple via-accentPink to-accentBlue">5주 로드맵</span>
        </h1>
        <p class="text-slate-400 text-sm md:text-base font-medium">아이디어를 수익으로 바꾸는 5단계 시스템</p>
      </div>

      <div class="w-full md:w-80 bg-slate-900/80 rounded-xl p-4 border border-slate-800/80 flex flex-col gap-3">
        <div class="flex justify-between items-center">
          <span class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-2">
            <i class="fa-solid fa-chart-line text-accentPink"></i> 전반적 진척도
          </span>
          <span id="progress-percent" class="text-lg font-black text-transparent bg-clip-text bg-gradient-to-r from-accentPurple to-accentPink">0%</span>
        </div>
        <div class="w-full bg-slate-800 h-3 rounded-full overflow-hidden p-0.5 border border-slate-700/50">
          <div id="progress-bar" class="h-full bg-gradient-to-r from-accentPurple via-accentPink to-accentBlue rounded-full transition-all duration-500 ease-out" style="width: 0%"></div>
        </div>
        <div class="flex justify-between items-center text-xs text-slate-400">
          <span>완료: <strong id="completed-count" class="text-white">0</strong> / <span id="total-count">0</span></span>
          <button id="reset-btn" class="hover:text-accentPink transition-colors text-xs flex items-center gap-1">
            <i class="fa-solid fa-rotate-right"></i> 초기화
          </button>
        </div>
      </div>
    </header>

    <!-- Core Flow Bar -->
    <section class="glass-panel rounded-xl p-4 border-slate-800">
      <div class="flex flex-col md:flex-row items-center justify-between gap-2 md:gap-4">
        <div class="flex items-center gap-2 font-bold text-accentPurple text-sm px-3 py-1.5 rounded-lg bg-accentPurple/10 border border-accentPurple/20">
          <i class="fa-solid fa-bullseye"></i> 핵심 흐름
        </div>
        <div class="w-full flex-1 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2 text-center text-xs md:text-sm">
          <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">1. 주제 선정</div>
          <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">2. 제품 설계</div>
          <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">3. 페이지 제작</div>
          <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">4. 자동화 구축</div>
          <div class="col-span-2 sm:col-span-1 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">5. 오픈 & 개선</div>
        </div>
      </div>
    </section>

    <!-- Cards Grid -->
    <main class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 md:gap-5"></main>

  </div>

  <script>
    const roadmapData = [
      { week: 1, title: "주제 선정 & 고객문제 찾기", goal: "판매가능성 높은 주제 1개 확정", tasks: ["누구에게 닿을지 명확히 정의하기", "내 노하우가 실제 풀어줄 수 있는 문제 1개 고르기", "이 고객이 되어 하루, 감정, 불편함 정리하기", "고객을 위한 사업 예시 10개 설계", "디지털 상품 종류 결정"] },
      { week: 2, title: "제품 구조 설계 + MVP 제작", goal: "최소 기능 서비스 및 상품 구성 완료", tasks: ["판매할 디지털 상품 구성하기", "축소 상품 기획 및 AI 활용 제작", "고객의 '작은 성공, 성과' 나오게 설계"] },
      { week: 3, title: "랜딩페이지 & 원라이너 작성", goal: "사고 싶게 만드는 페이지 완성", tasks: ["랜딩페이지 원라이너 만들기", "리드 제너레이터 제작 (무료 자료)", "Before/After 시각화", "랜딩페이지 초안 완성"] },
      { week: 4, title: "자동화 + 마케팅 시스템 구축", goal: "자동으로 끌리는 구조 세팅", tasks: ["DB 수집 자동화 만들기 (타입폼/카카오)", "콘텐츠 시작 플랫폼 구축"] },
      { week: 5, title: "오픈 -> 피드백 -> 최종 개선", goal: "자동 셀링 랜딩페이지 완성", tasks: ["첫 구매자 5명 확보 목표", "빠르게 피드백 수집 및 FAQ 제작", "문제 즉시 업데이트"] }
    ];

    const STORAGE_KEY_TASKS = "upnomad_roadmap_tasks_v1";
    const STORAGE_KEY_NOTES = "upnomad_roadmap_notes_v1";
    let taskState = JSON.parse(localStorage.getItem(STORAGE_KEY_TASKS)) || {};
    let noteState = JSON.parse(localStorage.getItem(STORAGE_KEY_NOTES)) || {};

    const mainGrid = document.querySelector('main');
    const progressBar = document.getElementById('progress-bar');
    const progressPercent = document.getElementById('progress-percent');
    const completedCountEl = document.getElementById('completed-count');
    const totalCountEl = document.getElementById('total-count');

    function renderCards() {
      mainGrid.innerHTML = "";
      roadmapData.forEach((data) => {
        const weekKey = `week_${data.week}`;
        const weekNotes = noteState[weekKey] || "";

        const card = document.createElement('article');
        card.className = "glass-card rounded-2xl p-5 flex flex-col justify-between h-full border-slate-800/80";
        
        let tasksHTML = "";
        data.tasks.forEach((task, idx) => {
          const taskId = `w${data.week}_t${idx}`;
          const isChecked = !!taskState[taskId];
          tasksHTML += `
            <li class="flex items-start gap-2.5 cursor-pointer">
              <input type="checkbox" id="${taskId}" data-task-id="${taskId}" class="custom-checkbox mt-0.5 shrink-0" ${isChecked ? 'checked' : ''}>
              <label for="${taskId}" class="text-xs text-slate-300 leading-relaxed cursor-pointer select-none ${isChecked ? 'completed-text' : ''}">${task}</label>
            </li>`;
        });

        card.innerHTML = `
          <div class="space-y-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800/80">
              <span class="px-3 py-1 rounded-lg bg-accentPurple/20 text-accentPurple font-black text-xs">WEEK ${data.week}</span>
            </div>
            <h3 class="text-base font-extrabold text-white">${data.title}</h3>
            <ul class="space-y-3 pt-1">${tasksHTML}</ul>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-800/80 space-y-3">
            <div class="p-3 rounded-xl bg-accentPurple/10 border border-accentPurple/20">
              <span class="block text-[10px] font-bold text-accentPurple uppercase">이번 주 목표</span>
              <p class="text-xs font-bold text-slate-100 mt-0.5">${data.goal}</p>
            </div>
            <div>
              <label class="block text-[10px] font-semibold text-slate-400 mb-1">📝 나의 전략 메모</label>
              <textarea data-week-key="${weekKey}" rows="2" placeholder="메모를 적으세요..." class="w-full bg-white text-slate-900 text-xs font-semibold p-2.5 rounded-lg border-0 neon-focus resize-none">${weekNotes}</textarea>
            </div>
          </div>`;
        mainGrid.appendChild(card);
      });
    }

    function updateProgress() {
      let totalTasks = 0, completedTasks = 0;
      roadmapData.forEach(d => {
        d.tasks.forEach((_, idx) => {
          totalTasks++;
          if (taskState[`w${d.week}_t${idx}`]) completedTasks++;
        });
      });
      const percentage = totalTasks === 0 ? 0 : Math.round((completedTasks / totalTasks) * 100);
      progressBar.style.width = `${percentage}%`;
      progressPercent.textContent = `${percentage}%`;
      completedCountEl.textContent = completedTasks;
      totalCountEl.textContent = totalTasks;
    }

    mainGrid.addEventListener('change', (e) => {
      if (e.target.classList.contains('custom-checkbox')) {
        taskState[e.target.getAttribute('data-task-id')] = e.target.checked;
        localStorage.setItem(STORAGE_KEY_TASKS, JSON.stringify(taskState));
        updateProgress();
        renderCards();
      }
    });

    mainGrid.addEventListener('input', (e) => {
      if (e.target.tagName === 'TEXTAREA') {
        noteState[e.target.getAttribute('data-week-key')] = e.target.value;
        localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(noteState));
      }
    });

    document.getElementById('reset-btn').addEventListener('click', () => {
      if (confirm("초기화하시겠습니까?")) {
        localStorage.clear();
        taskState = {}; noteState = {};
        renderCards(); updateProgress();
      }
    });

    renderCards();
    updateProgress();
  </script>
</body>
</html>
"""

# 4. 사이드바: 방금 생성된 구글 시트로 바로 이동하는 편의 버튼 제공
st.sidebar.title("📊 구글 시트 연동")
st.sidebar.markdown("방금 자동 생성된 구글 시트에서 전체 진행 상황을 표로 확인하실 수 있습니다.")
st.sidebar.markdown(
    "[👉 디지털 상품 5주 로드맵 데이터 시트 열기](https://docs.google.com/spreadsheets/d/1oLhLk1KO8ZzBHL0-AdZVlrmWTBejmUB8HIVbqJ6qfok/edit)",
    unsafe_allow_html=True,
)

# 5. 컴포넌트 렌더링
components.html(html_code, height=1150, scrolling=True)
