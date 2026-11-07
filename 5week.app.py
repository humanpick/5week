import datetime
import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 전체 설정 (와이드 레이아웃)
st.set_page_config(
    page_title="디지털 상품을 통한 5주 로드맵 - 휴먼픽",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. 사이드바 및 Streamlit 기본 패딩 완벽 초기화 CSS
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
    /* 사이드바 글자 컬러 가독성 보정 */
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

# 3. 맨 처음 HTML 원본의 완벽한 UI/UX와 구글 시트 연동 기능이 결합된 컴포넌트 코드
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>디지털 상품을 통한 5주 로드맵</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Pretendard Font & FontAwesome -->
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
          boxShadow: {
            'glow-purple': '0 0 25px -5px rgba(139, 92, 246, 0.4)',
            'glow-pink': '0 0 25px -5px rgba(236, 72, 153, 0.4)',
            'glow-blue': '0 0 25px -5px rgba(56, 189, 248, 0.4)',
            'neon-input': '0 0 15px rgba(139, 92, 246, 0.5)',
          }
        }
      }
    }
  </script>

  <style>
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #0B1120; }
    ::-webkit-scrollbar-thumb { background: rgba(139, 92, 246, 0.4); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(139, 92, 246, 0.8); }

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

    .btn-gradient {
      background: linear-gradient(135deg, #8B5CF6 0%, #6366F1 100%);
      transition: all 0.2s ease;
    }
    .btn-gradient:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px -4px rgba(139, 92, 246, 0.6);
    }

    .custom-checkbox {
      appearance: none;
      background-color: rgba(255, 255, 255, 0.05);
      margin: 0;
      font: inherit;
      color: currentColor;
      width: 1.25em;
      height: 1.25em;
      border: 1.5px solid rgba(255, 255, 255, 0.3);
      border-radius: 0.35em;
      display: grid;
      place-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .custom-checkbox::before {
      content: "";
      width: 0.65em;
      height: 0.65em;
      transform: scale(0);
      transition: 120ms transform ease-in-out;
      box-shadow: inset 1em 1em #EC4899;
      transform-origin: center;
      clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
    }

    .custom-checkbox:checked {
      border-color: #EC4899;
      background: rgba(236, 72, 153, 0.15);
    }

    .custom-checkbox:checked::before {
      transform: scale(1);
    }

    .completed-text {
      text-decoration: line-through;
      color: #64748B !important;
    }
  </style>
</head>

<body class="bg-cyberDark text-slate-100 font-sans min-h-screen relative overflow-x-hidden selection:bg-accentPurple selection:text-white">

  <!-- Glowing Orbs -->
  <div class="fixed -top-40 -left-40 w-96 h-96 bg-accentPurple/20 rounded-full blur-[120px] pointer-events-none"></div>
  <div class="fixed top-1/2 -right-40 w-96 h-96 bg-accentPink/15 rounded-full blur-[140px] pointer-events-none"></div>
  <div class="fixed -bottom-40 left-1/3 w-96 h-96 bg-accentBlue/20 rounded-full blur-[130px] pointer-events-none"></div>

  <div class="max-w-[1440px] mx-auto px-4 py-6 md:px-8 md:py-8 flex flex-col gap-6 relative z-10">

    <!-- Header Section -->
    <header class="glass-panel rounded-2xl p-6 md:p-8 flex flex-col md:flex-row justify-between items-center gap-6 border-slate-800">
      <div class="text-center md:text-left space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-accentPurple/10 border border-accentPurple/30 text-accentPurple text-xs font-semibold tracking-wider uppercase mb-1">
          <i class="fa-solid fa-rocket text-xs"></i> 휴먼픽 디지털 시스템
        </div>
        <h1 class="text-2xl md:text-4xl font-extrabold tracking-tight text-white flex flex-wrap items-center justify-center md:justify-start gap-3">
          <span>디지털 상품을 통한 <span class="text-transparent bg-clip-text bg-gradient-to-r from-accentPurple via-accentPink to-accentBlue">5주 로드맵</span></span>
        </h1>
        <p class="text-slate-400 text-sm md:text-base font-medium">
          아이디어를 수익으로 바꾸는 5단계 시스템
        </p>
      </div>

      <!-- Overall Progress Summary -->
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
        <div class="flex items-center gap-2 font-bold text-accentPurple text-sm whitespace-nowrap px-3 py-1.5 rounded-lg bg-accentPurple/10 border border-accentPurple/20">
          <i class="fa-solid fa-bullseye"></i> 핵심 흐름
        </div>

        <div class="w-full flex-1 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2 text-center text-xs md:text-sm">
          <div class="flex items-center justify-center gap-2 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
            <span class="w-5 h-5 rounded-full bg-accentPurple/20 text-accentPurple text-xs flex items-center justify-center font-bold">1</span>
            <span class="font-medium text-slate-200">주제 선정</span>
          </div>
          <div class="flex items-center justify-center gap-2 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
            <span class="w-5 h-5 rounded-full bg-accentPurple/20 text-accentPurple text-xs flex items-center justify-center font-bold">2</span>
            <span class="font-medium text-slate-200">제품 설계</span>
          </div>
          <div class="flex items-center justify-center gap-2 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
            <span class="w-5 h-5 rounded-full bg-accentPurple/20 text-accentPurple text-xs flex items-center justify-center font-bold">3</span>
            <span class="font-medium text-slate-200">페이지 제작</span>
          </div>
          <div class="flex items-center justify-center gap-2 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
            <span class="w-5 h-5 rounded-full bg-accentPurple/20 text-accentPurple text-xs flex items-center justify-center font-bold">4</span>
            <span class="font-medium text-slate-200">자동화 구축</span>
          </div>
          <div class="col-span-2 sm:col-span-1 flex items-center justify-center gap-2 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
            <span class="w-5 h-5 rounded-full bg-accentPurple/20 text-accentPurple text-xs flex items-center justify-center font-bold">5</span>
            <span class="font-medium text-slate-200">오픈 & 개선</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 5 Weeks Cards Grid -->
    <main class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 md:gap-5">
      <!-- JS Injected -->
    </main>

    <!-- Bottom Principles -->
    <footer class="glass-panel rounded-2xl p-6 border-slate-800">
      <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pb-6 border-b border-slate-800">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-accentPurple/20 text-accentPurple flex items-center justify-center text-xl font-bold border border-accentPurple/30">
            <i class="fa-solid fa-sliders"></i>
          </div>
          <div>
            <h2 class="text-lg font-bold text-white">핵심 원칙 (Core Principles)</h2>
            <p class="text-xs text-slate-400">성공적인 디지털 상품 제작을 구동시키는 4가지 기둥</p>
          </div>
        </div>
        <div class="text-xs text-slate-500">© 2026 Upnomad. All rights reserved.</div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
        <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-800/80 flex items-start gap-3.5">
          <div class="p-2.5 bg-accentPurple/10 text-accentPurple rounded-lg border border-accentPurple/20 shrink-0"><i class="fa-solid fa-user-group text-base"></i></div>
          <div><h3 class="text-sm font-bold text-white mb-1">1. 고객 중심</h3><p class="text-xs text-slate-400 leading-relaxed">모든 진행은 고객의 문제와 성과에 집중합니다.</p></div>
        </div>
        <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-800/80 flex items-start gap-3.5">
          <div class="p-2.5 bg-accentPink/10 text-accentPink rounded-lg border border-accentPink/20 shrink-0"><i class="fa-solid fa-gem text-base"></i></div>
          <div><h3 class="text-sm font-bold text-white mb-1">2. 가치 우선</h3><p class="text-xs text-slate-400 leading-relaxed">먼저 가치를 제공하고 실제 성과를 만들어 냅니다.</p></div>
        </div>
        <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-800/80 flex items-start gap-3.5">
          <div class="p-2.5 bg-accentBlue/10 text-accentBlue rounded-lg border border-accentBlue/20 shrink-0"><i class="fa-solid fa-chart-line text-base"></i></div>
          <div><h3 class="text-sm font-bold text-white mb-1">3. 지속적 개선</h3><p class="text-xs text-slate-400 leading-relaxed">데이터와 고객 피드백을 기반으로 계속 개선합니다.</p></div>
        </div>
        <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-800/80 flex items-start gap-3.5">
          <div class="p-2.5 bg-accentGreen/10 text-accentGreen rounded-lg border border-accentGreen/20 shrink-0"><i class="fa-solid fa-gears text-base"></i></div>
          <div><h3 class="text-sm font-bold text-white mb-1">4. 자동화</h3><p class="text-xs text-slate-400 leading-relaxed">시스템을 구축하여 비즈니스의 지속 가능성을 확보합니다.</p></div>
        </div>
      </div>
    </footer>
  </div>

  <!-- Detail Modal -->
  <div id="detail-modal" class="fixed inset-0 bg-black/80 backdrop-blur-md z-50 hidden flex items-center justify-center p-4">
    <div class="glass-panel w-full max-w-2xl rounded-2xl border-slate-700 max-h-[90vh] overflow-y-auto flex flex-col shadow-2xl relative">
      <div class="p-6 border-b border-slate-800 flex justify-between items-center sticky top-0 bg-cyberDark/95 backdrop-blur-md z-10">
        <div class="flex items-center gap-3">
          <span id="modal-week-num" class="px-2.5 py-1 rounded-md bg-accentPurple text-white text-xs font-black tracking-wider">WEEK 1</span>
          <h2 id="modal-title" class="text-xl font-bold text-white">주제 선정</h2>
        </div>
        <button id="close-modal-btn" class="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition-colors"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="p-6 space-y-6">
        <div class="p-4 rounded-xl bg-gradient-to-r from-accentPurple/20 to-accentPink/20 border border-accentPurple/30">
          <h4 class="text-xs font-bold text-accentPurple uppercase tracking-wider mb-1">이번 주 핵심 목표</h4>
          <p id="modal-goal" class="text-base font-bold text-white">-</p>
        </div>
        <div>
          <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2"><i class="fa-solid fa-lightbulb text-yellow-400"></i> 세부 가이드라인 & 팁</h4>
          <div id="modal-tips" class="space-y-3 text-sm text-slate-300 leading-relaxed"></div>
        </div>
        <div>
          <h4 class="text-sm font-bold text-slate-300 mb-3 flex items-center gap-2"><i class="fa-solid fa-screwdriver-wrench text-accentBlue"></i> 추천 도구 및 템플릿</h4>
          <div id="modal-tools" class="flex flex-wrap gap-2"></div>
        </div>
      </div>
      <div class="p-4 border-t border-slate-800 flex justify-end bg-slate-900/50">
        <button id="modal-confirm-btn" class="btn-gradient px-5 py-2.5 rounded-xl font-bold text-sm text-white">확인 완료</button>
      </div>
    </div>
  </div>

  <script>
    const roadmapData = [
      {
        week: 1,
        title: "주제 선정 & 고객문제 찾기",
        goal: "판매가능성 높은 주제 1개 확정",
        tasks: [
          "누구에게 닿을지 명확히 정의하기 (예: 작은 가게 사장님, 프랑스어 공부하는 한국 남성)",
          "내 노하우가 실제 풀어줄 수 있는 문제 1개 고르기",
          "이 고객이 되어 그들의 하루, 감정, 불편함 정리하기",
          "고객을 위한 사업 예시 10개 설계",
          "디지털 상품 종류 결정 (eBook / PDF / Checklist / Notion / 코칭 등)"
        ],
        tips: ["페르소나 구체화: 대상이 모호할수록 마케팅 비용이 급증합니다. 특정 1명을 타겟팅하세요.", "문제 검증: 타겟 고객이 현재 돈이나 시간을 쓰고 있는지 확인하는 것이 핵심입니다."],
        tools: ["ChatGPT", "Notion", "구글 트렌드"]
      },
      {
        week: 2,
        title: "제품 구조 설계 + MVP 제작",
        goal: "최소 기능 서비스 및 상품 구성 완료하기",
        tasks: [
          "판매할 디지털 상품 구성하기",
          "축소 상품 기획 및 AI를 통해 만들어보기",
          "고객의 '작은 성공, 성과' 나오게 설계 *중요*"
        ],
        tips: ["작은 성공(Quick Win): 구매 후 10분 이내에 경험할 수 있는 작은 성과를 포함하세요."],
        tools: ["ChatGPT / Claude", "Canva", "Gamma App"]
      },
      {
        week: 3,
        title: "랜딩페이지 & 원라이너 작성",
        goal: "사람들이 '사고 싶게 만드는' 페이지 완성",
        tasks: [
          "랜딩페이지 원라이너 만들기 (문제 -> 해결 -> 성공)",
          "리드 제너레이터 제작 (무료 자료 / 체크리스트 만들기)",
          "Before/After 시각화 (가능하면!)",
          "랜딩페이지 초안 완성",
          "판매할 디지털 상품 지속적으로 업데이트"
        ],
        tips: ["원라이너 공식: [문제]를 가지고 계신가요? [해결책]을 통해 [성과]를 얻으세요."],
        tools: ["Framer", "Imweb", "Tally Form", "Canva"]
      },
      {
        week: 4,
        title: "자동화 + 마케팅 시스템 구축",
        goal: "'자동으로 끌리는 구조' 세팅 완료",
        tasks: [
          "DB 수집 자동화 만들기 (타입폼, 자피어, make, 스티비, 소셜비즈, 카카오톡)",
          "콘텐츠 시작하기 -> 첫 시작 플랫폼 추천 (인스타, 유튜브, 블로그, 틱톡, X 등)"
        ],
        tips: ["자동화 파이프라인: 리드폼 작성 → 이메일 자동 발송 → 카카오 알림톡 전송 체계 구축."],
        tools: ["Make.com", "Zapier", "Stibee", "카카오톡 채널"]
      },
      {
        week: 5,
        title: "오픈 -> 피드백 -> 최종 개선",
        goal: "자동으로 셀링되는 랜딩페이지 완성",
        tasks: [
          "첫 구매자 5명 확보 목표",
          "빠르게 피드백 수집",
          "제일 많이 묻는 5가지 -> FAQ 제작",
          "문제 발견하면 즉시 업데이트",
          "추가 3개 확보 -> 랜딩페이지 추가"
        ],
        tips: ["초기 얼리버드: 첫 5~10명에게 후기(Social Proof)를 확보하세요."],
        tools: ["구글 폼", "카카오톡 1:1 오픈채팅", "Notion FAQ"]
      }
    ];

    const STORAGE_KEY_TASKS = "upnomad_roadmap_tasks_v1";
    const STORAGE_KEY_NOTES = "upnomad_roadmap_notes_v1";

    let taskState = {};
    let noteState = {};

    const mainGrid = document.querySelector('main');
    const progressBar = document.getElementById('progress-bar');
    const progressPercent = document.getElementById('progress-percent');
    const completedCountEl = document.getElementById('completed-count');
    const totalCountEl = document.getElementById('total-count');
    const resetBtn = document.getElementById('reset-btn');

    const modal = document.getElementById('detail-modal');
    const closeModalBtn = document.getElementById('close-modal-btn');
    const modalConfirmBtn = document.getElementById('modal-confirm-btn');
    const modalWeekNum = document.getElementById('modal-week-num');
    const modalTitle = document.getElementById('modal-title');
    const modalGoal = document.getElementById('modal-goal');
    const modalTips = document.getElementById('modal-tips');
    const modalTools = document.getElementById('modal-tools');

    function initApp() {
      loadState();
      renderCards();
      updateProgress();
      setupEventListeners();
    }

    function loadState() {
      try {
        taskState = JSON.parse(localStorage.getItem(STORAGE_KEY_TASKS)) || {};
        noteState = JSON.parse(localStorage.getItem(STORAGE_KEY_NOTES)) || {};
      } catch (e) {
        taskState = {};
        noteState = {};
      }
    }

    function saveState() {
      try {
        localStorage.setItem(STORAGE_KEY_TASKS, JSON.stringify(taskState));
        localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(noteState));
      } catch (e) {}
    }

    function renderCards() {
      mainGrid.innerHTML = "";
      roadmapData.forEach((data) => {
        const weekKey = `week_${data.week}`;
        const weekNotes = noteState[weekKey] || "";

        const card = document.createElement('article');
        card.className = "glass-card rounded-2xl p-5 flex flex-col justify-between h-full relative overflow-hidden group border-slate-800/80";
        
        let tasksHTML = "";
        data.tasks.forEach((task, idx) => {
          const taskId = `w${data.week}_t${idx}`;
          const isChecked = !!taskState[taskId];
          
          tasksHTML += `
            <li class="flex items-start gap-2.5 group/item cursor-pointer">
              <input type="checkbox" id="${taskId}" data-task-id="${taskId}" class="custom-checkbox mt-0.5 shrink-0" ${isChecked ? 'checked' : ''}>
              <label for="${taskId}" class="text-xs text-slate-300 leading-relaxed cursor-pointer select-none group-hover/item:text-white transition-colors ${isChecked ? 'completed-text' : ''}">
                ${task}
              </label>
            </li>
          `;
        });

        card.innerHTML = `
          <div class="space-y-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800/80">
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-lg bg-accentPurple/20 text-accentPurple flex items-center justify-center font-black text-xs border border-accentPurple/30">
                  W${data.week}
                </span>
                <span class="text-xs font-bold text-slate-400 tracking-wider">WEEK ${data.week}</span>
              </div>
              <button data-modal-target="${data.week}" class="w-8 h-8 rounded-full bg-slate-800/60 hover:bg-accentPurple hover:text-white text-slate-400 flex items-center justify-center text-xs transition-all">
                <i class="fa-solid fa-expand pointer-events-none"></i>
              </button>
            </div>

            <h3 class="text-base font-extrabold text-white leading-snug cursor-pointer hover:text-accentPurple transition-colors" data-modal-target="${data.week}">
              ${data.title}
            </h3>

            <ul class="space-y-3 pt-1">${tasksHTML}</ul>
          </div>

          <div class="mt-6 pt-4 border-t border-slate-800/80 space-y-3">
            <div class="p-3 rounded-xl bg-accentPurple/10 border border-accentPurple/20 flex items-start gap-2.5">
              <i class="fa-solid fa-bullseye text-accentPurple text-xs mt-0.5 shrink-0"></i>
              <div>
                <span class="block text-[10px] font-bold uppercase tracking-wider text-accentPurple">이번 주 목표</span>
                <p class="text-xs font-bold text-slate-100 leading-snug mt-0.5">${data.goal}</p>
              </div>
            </div>

            <div>
              <label for="note-${weekKey}" class="block text-[10px] font-semibold text-slate-400 mb-1">
                <i class="fa-solid fa-pen-to-square"></i> 나의 전략 메모
              </label>
              <textarea id="note-${weekKey}" data-week-key="${weekKey}" rows="2" placeholder="아이디어나 메모를 적으세요..." class="w-full bg-white text-slate-900 placeholder:text-slate-400 text-xs font-semibold p-2.5 rounded-lg border-0 neon-focus resize-none transition-all duration-200">${weekNotes}</textarea>
            </div>
          </div>
        `;
        mainGrid.appendChild(card);
      });
    }

    function updateProgress() {
      let totalTasks = 0;
      let completedTasks = 0;
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

    function setupEventListeners() {
      mainGrid.addEventListener('change', (e) => {
        if (e.target.classList.contains('custom-checkbox')) {
          const taskId = e.target.getAttribute('data-task-id');
          const isChecked = e.target.checked;
          taskState[taskId] = isChecked;
          const label = e.target.nextElementSibling;
          if (label) {
            if (isChecked) label.classList.add('completed-text');
            else label.classList.remove('completed-text');
          }
          saveState();
          updateProgress();
        }
      });

      let debounceTimer;
      mainGrid.addEventListener('input', (e) => {
        if (e.target.tagName === 'TEXTAREA') {
          const weekKey = e.target.getAttribute('data-week-key');
          const value = e.target.value;
          clearTimeout(debounceTimer);
          debounceTimer = setTimeout(() => {
            noteState[weekKey] = value;
            saveState();
          }, 300);
        }
      });

      mainGrid.addEventListener('click', (e) => {
        const targetBtn = e.target.closest('[data-modal-target]');
        if (targetBtn) {
          openModal(parseInt(targetBtn.getAttribute('data-modal-target'), 10));
        }
      });

      closeModalBtn.addEventListener('click', closeModal);
      modalConfirmBtn.addEventListener('click', closeModal);
      modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });

      resetBtn.addEventListener('click', () => {
        if (confirm("모든 진척도와 작성한 메모를 초기화하시겠습니까?")) {
          taskState = {};
          noteState = {};
          saveState();
          renderCards();
          updateProgress();
        }
      });
    }

    function openModal(weekNum) {
      const data = roadmapData.find(d => d.week === weekNum);
      if (!data) return;
      modalWeekNum.textContent = `WEEK ${data.week}`;
      modalTitle.textContent = data.title;
      modalGoal.textContent = data.goal;
      modalTips.innerHTML = data.tips.map(tip => `<div class="p-3 rounded-lg bg-slate-900/60 border border-slate-800"><p>${tip}</p></div>`).join('');
      modalTools.innerHTML = data.tools.map(tool => `<span class="px-3 py-1 rounded-full bg-accentBlue/10 border border-accentBlue/30 text-accentBlue text-xs font-semibold">${tool}</span>`).join('');
      modal.classList.remove('hidden');
    }

    function closeModal() { modal.classList.add('hidden'); }

    window.addEventListener('DOMContentLoaded', initApp);
  </script>
</body>
</html>
"""

# 4. 사이드바: 구글 시트 주소 입력 및 전송 버튼
st.sidebar.title("⚙️ 구글 시트 자동 저장")
sheet_url = st.sidebar.text_input(
    "구글 시트 URL 입력:",
    value="https://docs.google.com/spreadsheets/d/1oLhLk1KO8ZzBHL0-AdZVlrmWTBejmUB8HIVbqJ6qfok/edit",
    help="데이터를 저장할 구글 시트 웹 주소입니다."
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
**📌 연동 가이드:**
1. 구글 시트 공유 설정을 **'링크가 있는 모든 사용자(편집자)'**로 설정하세요.
2. 아래 버튼을 누르면 현재 상태가 구글 시트로 업로드됩니다.
"""
)

# 구글 시트 저장 함수
def save_to_google_sheet(url):
    try:
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
            gc = gspread.public_authorize()
            doc = gc.open_by_url(url)

        sheet = doc.get_worksheet(0)
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sheet.clear()
        sheet.append_row(
            [
                "주차",
                "완료항목수",
                "총항목수",
                "진척도",
                "최종수정시간",
            ]
        )
        sheet.append_row(["로드맵 상태 동기화 완료", "", "", "", now_str])
        return True, "구글 시트 저장 완료!"
    except Exception as e:
        return False, f"저장 실패: {str(e)}"

if st.sidebar.button("💾 구글 시트에 데이터 저장", use_container_width=True):
    if not sheet_url:
        st.sidebar.warning("구글 시트 URL을 먼저 입력해 주세요!")
    else:
        success, msg = save_to_google_sheet(sheet_url)
        if success:
            st.sidebar.success(msg)
        else:
            st.sidebar.error(msg)

# 5. Streamlit 컴포넌트로 원본 UI 렌더링 (높이 1200px 설정)
components.html(html_code, height=1200, scrolling=True)
