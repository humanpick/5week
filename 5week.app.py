<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>디지털 상품을 통한 5주 로드맵</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Pretendard Font -->
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css" />
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Pretendard', 'sans-serif'],
                    },
                    colors: {
                        darkbg: '#0B1120',
                        glassborder: 'rgba(255, 255, 255, 0.12)',
                        neonPurple: '#8B5CF6',
                        neonPink: '#EC4899',
                        neonSky: '#38BDF8',
                    },
                    boxShadow: {
                        'neon-purple': '0 0 20px rgba(139, 92, 246, 0.4)',
                        'neon-pink': '0 0 20px rgba(236, 72, 153, 0.4)',
                        'neon-sky': '0 0 20px rgba(56, 189, 248, 0.4)',
                    }
                }
            }
        }
    </script>

    <style>
        body {
            font-family: 'Pretendard', sans-serif;
            background-color: #0B1120;
            color: #F3F4F6;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(139, 92, 246, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 85% 85%, rgba(236, 72, 153, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 50% 50%, rgba(56, 189, 248, 0.08) 0%, transparent 50%);
            background-attachment: fixed;
        }

        .glass-panel {
            background: rgba(17, 24, 39, 0.65);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .glass-card {
            background: rgba(30, 41, 59, 0.5);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .glass-card:hover {
            border-color: rgba(139, 92, 246, 0.4);
            transform: translateY(-2px);
        }

        /* Input Cyberpunk Glow Requirement */
        .glow-input {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            font-weight: 700 !important;
            transition: all 0.2s ease;
        }

        .glow-input:focus {
            outline: none;
            box-shadow: 0 0 15px #8B5CF6, 0 0 2px #8B5CF6;
            border-color: #8B5CF6;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0B1120;
        }
        ::-webkit-scrollbar-thumb {
            background: #1E293B;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #8B5CF6;
        }

        /* Custom Checkbox Animation */
        .custom-checkbox {
            appearance: none;
            width: 1.25rem;
            height: 1.25rem;
            border: 2px solid #6B7280;
            border-radius: 0.375rem;
            outline: none;
            cursor: pointer;
            position: relative;
            transition: all 0.2s ease;
        }

        .custom-checkbox:checked {
            background-color: #8B5CF6;
            border-color: #8B5CF6;
            box-shadow: 0 0 10px rgba(139, 92, 246, 0.6);
        }

        .custom-checkbox:checked::after {
            content: '✓';
            position: absolute;
            color: white;
            font-size: 0.875rem;
            font-weight: bold;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
    </style>
</head>
<body class="min-h-screen pb-12">

    <!-- Container Layout -->
    <div class="max-w-[1400px] mx-auto px-4 py-6">

        <!-- HEADER SECTION -->
        <header class="glass-panel rounded-2xl p-6 mb-6 shadow-2xl relative overflow-hidden">
            <div class="absolute -right-10 -top-10 w-40 h-40 bg-purple-600/20 rounded-full blur-3xl pointer-events-none"></div>
            <div class="absolute -left-10 -bottom-10 w-40 h-40 bg-pink-600/20 rounded-full blur-3xl pointer-events-none"></div>

            <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6 relative z-10">
                <div>
                    <div class="flex items-center gap-3 mb-2">
                        <span class="px-3 py-1 rounded-full text-xs font-bold bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg">
                            UPNOMAD SYSTEM
                        </span>
                        <span class="text-gray-400 text-sm font-medium">
                            <i class="fa-solid font-bold fa-bolt text-yellow-400 mr-1"></i> 아이디어를 수익으로 바꾸는 5단계 시스템
                        </span>
                    </div>
                    <h1 class="text-3xl lg:text-4xl font-extrabold tracking-tight text-white flex items-center gap-3">
                        디지털 상품을 통한 5주 로드맵
                    </h1>
                </div>

                <!-- OVERALL PROGRESS CARD -->
                <div class="glass-card p-4 rounded-xl min-w-[280px] lg:min-w-[340px] border border-white/10">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs font-semibold text-gray-300 uppercase tracking-wider">전체 달성률</span>
                        <span id="overall-percent" class="text-xl font-black text-transparent bg-clip-text bg-gradient-to-r from-neonSky via-neonPurple to-neonPink">0%</span>
                    </div>
                    <div class="w-full bg-gray-800 rounded-full h-3 overflow-hidden p-0.5 border border-white/5">
                        <div id="overall-progress-bar" class="bg-gradient-to-r from-sky-400 via-purple-500 to-pink-500 h-full rounded-full transition-all duration-500 w-0"></div>
                    </div>
                    <div class="flex justify-between items-center mt-2 text-[11px] text-gray-400">
                        <span>완료한 항목: <strong id="completed-count" class="text-purple-400">0</strong> / <span id="total-count">0</span></span>
                        <button onclick="resetAllProgress()" class="hover:text-red-400 transition-colors cursor-pointer flex items-center gap-1">
                            <i class="fa-solid fa-rotate-right text-[10px]"></i> 초기화
                        </button>
                    </div>
                </div>
            </div>

            <!-- CORE FLOW & VIEW SWITCHER -->
            <div class="mt-6 pt-5 border-t border-white/10 flex flex-col md:flex-row md:items-center justify-between gap-4">
                <!-- Flow Steps Visualizer -->
                <div class="flex items-center gap-1 text-xs sm:text-sm text-gray-300 overflow-x-auto pb-2 md:pb-0 scrollbar-none">
                    <span class="font-bold text-purple-400 flex items-center gap-1 shrink-0"><i class="fa-solid fa-bullseye"></i> 핵심 흐름:</span>
                    <span class="px-2 py-0.5 rounded bg-white/5 shrink-0">주제 선정</span>
                    <i class="fa-solid fa-chevron-right text-[10px] text-gray-500 shrink-0"></i>
                    <span class="px-2 py-0.5 rounded bg-white/5 shrink-0">제품 설계</span>
                    <i class="fa-solid fa-chevron-right text-[10px] text-gray-500 shrink-0"></i>
                    <span class="px-2 py-0.5 rounded bg-white/5 shrink-0">페이지 제작</span>
                    <i class="fa-solid fa-chevron-right text-[10px] text-gray-500 shrink-0"></i>
                    <span class="px-2 py-0.5 rounded bg-white/5 shrink-0">자동화 구축</span>
                    <i class="fa-solid fa-chevron-right text-[10px] text-gray-500 shrink-0"></i>
                    <span class="px-2 py-0.5 rounded bg-white/5 shrink-0">오픈 & 피드백</span>
                </div>

                <!-- View Switcher Controls -->
                <div class="flex items-center gap-2 bg-gray-900/80 p-1 rounded-lg border border-white/10 self-start md:self-auto shrink-0">
                    <button id="view-grid-btn" onclick="setViewMode('grid')" class="px-3 py-1.5 rounded-md text-xs font-semibold transition-all flex items-center gap-1.5 bg-purple-600 text-white shadow-lg">
                        <i class="fa-solid fa-border-all"></i> 전체 5주 한눈에 보기
                    </button>
                    <button id="view-single-btn" onclick="setViewMode('single')" class="px-3 py-1.5 rounded-md text-xs font-semibold text-gray-400 hover:text-white transition-all flex items-center gap-1.5">
                        <i class="fa-solid fa-bullseye"></i> 집중 모드 (주차별 선택)
                    </button>
                </div>
            </div>
        </header>

        <!-- SINGLE VIEW TAB SELECTOR (Hidden in Grid Mode) -->
        <div id="single-view-tabs" class="hidden mb-6 flex overflow-x-auto gap-2 pb-2">
            <button onclick="setActiveWeekTab(1)" class="week-tab-btn flex-1 min-w-[140px] p-3 rounded-xl glass-card text-left border border-white/10 hover:border-purple-500/50 transition-all">
                <div class="text-[10px] font-bold text-purple-400 uppercase">Step 01</div>
                <div class="text-sm font-bold truncate">WEEK 1</div>
            </button>
            <button onclick="setActiveWeekTab(2)" class="week-tab-btn flex-1 min-w-[140px] p-3 rounded-xl glass-card text-left border border-white/10 hover:border-purple-500/50 transition-all">
                <div class="text-[10px] font-bold text-purple-400 uppercase">Step 02</div>
                <div class="text-sm font-bold truncate">WEEK 2</div>
            </button>
            <button onclick="setActiveWeekTab(3)" class="week-tab-btn flex-1 min-w-[140px] p-3 rounded-xl glass-card text-left border border-white/10 hover:border-purple-500/50 transition-all">
                <div class="text-[10px] font-bold text-purple-400 uppercase">Step 03</div>
                <div class="text-sm font-bold truncate">WEEK 3</div>
            </button>
            <button onclick="setActiveWeekTab(4)" class="week-tab-btn flex-1 min-w-[140px] p-3 rounded-xl glass-card text-left border border-white/10 hover:border-purple-500/50 transition-all">
                <div class="text-[10px] font-bold text-purple-400 uppercase">Step 04</div>
                <div class="text-sm font-bold truncate">WEEK 4</div>
            </button>
            <button onclick="setActiveWeekTab(5)" class="week-tab-btn flex-1 min-w-[140px] p-3 rounded-xl glass-card text-left border border-white/10 hover:border-purple-500/50 transition-all">
                <div class="text-[10px] font-bold text-purple-400 uppercase">Step 05</div>
                <div class="text-sm font-bold truncate">WEEK 5</div>
            </button>
        </div>

        <!-- MAIN 5 WEEKS CONTAINER GRID -->
        <main id="weeks-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-5 mb-8">
            
            <!-- WEEK 1 -->
            <div id="week-card-1" class="week-card glass-card rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-purple-500 to-indigo-500"></div>
                <div>
                    <!-- Card Header -->
                    <div class="flex justify-between items-start mb-4">
                        <div>
                            <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30 mb-1">
                                1단계
                            </span>
                            <h2 class="text-lg font-black text-white">WEEK 1</h2>
                            <p class="text-xs text-purple-300 font-semibold mt-0.5">주제 선정 & 고객문제 찾기</p>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-purple-400 text-lg group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-magnifying-glass"></i>
                        </div>
                    </div>

                    <!-- Checklist -->
                    <div class="space-y-3 mb-6">
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="1" data-idx="0" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>누구에게 팔지</strong> 타겟층 정의하기 <span class="text-[10px] text-gray-400 block">(예: 작은 가게 사장님, 프랑스어를 공부하는 한국 남성)</span>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="1" data-idx="1" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                내 노하우가 실제 풀어줄 수 있는 <strong>문제 1개 고르기</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="1" data-idx="2" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                이 고객이 되어 <strong>그들의 하루, 감정, 불편함 정리</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="1" data-idx="3" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                고객을 위한 <strong>사업 예시 10개 설계</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="1" data-idx="4" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>디지털 상품 종류 결정</strong> <span class="text-[10px] text-gray-400 block">(eBook / PDF / Checklist / Notion / 코칭 등)</span>
                            </span>
                        </label>
                    </div>
                </div>

                <div>
                    <!-- Target Goal Box -->
                    <div class="p-3 rounded-xl bg-purple-950/40 border border-purple-500/30 mb-4">
                        <div class="flex items-center gap-1.5 text-[11px] font-bold text-purple-300 mb-1">
                            <i class="fa-solid fa-bullseye"></i> 이번 주 목표
                        </div>
                        <p class="text-xs text-gray-200 font-medium">판매가능성 높은 주제 1개 확정</p>
                    </div>

                    <!-- Cyberpunk Note Input -->
                    <div>
                        <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-1.5">
                            <i class="fa-solid fa-pen text-purple-400"></i> 실행 노트 & 아이디어 메모
                        </label>
                        <textarea id="note-1" oninput="saveNote(1, this.value)" rows="3" placeholder="선정한 주제와 타겟 고객 아이디어를 적어보세요..." class="w-full text-xs p-2.5 rounded-lg glow-input shadow-inner resize-none"></textarea>
                    </div>
                </div>
            </div>

            <!-- WEEK 2 -->
            <div id="week-card-2" class="week-card glass-card rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 to-cyan-500"></div>
                <div>
                    <!-- Card Header -->
                    <div class="flex justify-between items-start mb-4">
                        <div>
                            <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 mb-1">
                                2단계
                            </span>
                            <h2 class="text-lg font-black text-white">WEEK 2</h2>
                            <p class="text-xs text-sky-300 font-semibold mt-0.5">제품 구조 설계 + MVP 제작</p>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-sky-500/10 border border-sky-500/30 flex items-center justify-center text-sky-400 text-lg group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-box-archive"></i>
                        </div>
                    </div>

                    <!-- Checklist -->
                    <div class="space-y-3 mb-6">
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="2" data-idx="0" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>판매할 디지털 상품 구성하기</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="2" data-idx="1" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                축소 상품 기획 및 <strong>AI를 통해 만들어보기</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="2" data-idx="2" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                고객의 <strong>"작은 성공, 성과"</strong> 나오게 설계 <span class="text-amber-400 font-bold">*중요*</span>
                            </span>
                        </label>
                    </div>
                </div>

                <div>
                    <!-- Target Goal Box -->
                    <div class="p-3 rounded-xl bg-sky-950/40 border border-sky-500/30 mb-4">
                        <div class="flex items-center gap-1.5 text-[11px] font-bold text-sky-300 mb-1">
                            <i class="fa-solid fa-bullseye"></i> 이번 주 목표
                        </div>
                        <p class="text-xs text-gray-200 font-medium">최소 기능 서비스 및 상품 구성 완료하기</p>
                    </div>

                    <!-- Cyberpunk Note Input -->
                    <div>
                        <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-1.5">
                            <i class="fa-solid fa-pen text-sky-400"></i> 실행 노트 & 아이디어 메모
                        </label>
                        <textarea id="note-2" oninput="saveNote(2, this.value)" rows="3" placeholder="상품 목차 및 AI 활용 초안 작성 기록..." class="w-full text-xs p-2.5 rounded-lg glow-input shadow-inner resize-none"></textarea>
                    </div>
                </div>
            </div>

            <!-- WEEK 3 -->
            <div id="week-card-3" class="week-card glass-card rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-teal-500 to-emerald-500"></div>
                <div>
                    <!-- Card Header -->
                    <div class="flex justify-between items-start mb-4">
                        <div>
                            <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 mb-1">
                                3단계
                            </span>
                            <h2 class="text-lg font-black text-white">WEEK 3</h2>
                            <p class="text-xs text-emerald-300 font-semibold mt-0.5">랜딩페이지 & 원라이너 작성</p>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 text-lg group-hover:scale-110 transition-transform">
                            <i class="fa-regular fa-window-maximize"></i>
                        </div>
                    </div>

                    <!-- Checklist -->
                    <div class="space-y-3 mb-6">
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="3" data-idx="0" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                랜딩페이지 <strong>원라이너 만들기</strong> <span class="text-[10px] text-gray-400 block">(문제 -&gt; 해결 -&gt; 성공)</span>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="3" data-idx="1" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>리드 제너레이터 제작</strong> <span class="text-[10px] text-gray-400 block">(무료 자료 / 체크리스트 만들기)</span>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="3" data-idx="2" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>Before/After 시각화</strong> (가능하면!)
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="3" data-idx="3" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>랜딩페이지 초안 완성</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="3" data-idx="4" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                판매할 디지털 상품 <strong>지속적으로 업데이트</strong>
                            </span>
                        </label>
                    </div>
                </div>

                <div>
                    <!-- Target Goal Box -->
                    <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 mb-4">
                        <div class="flex items-center gap-1.5 text-[11px] font-bold text-emerald-300 mb-1">
                            <i class="fa-solid fa-bullseye"></i> 이번 주 목표
                        </div>
                        <p class="text-xs text-gray-200 font-medium">사람들이 "사고 싶게 만드는" 페이지 완성</p>
                    </div>

                    <!-- Cyberpunk Note Input -->
                    <div>
                        <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-1.5">
                            <i class="fa-solid fa-pen text-emerald-400"></i> 실행 노트 & 아이디어 메모
                        </label>
                        <textarea id="note-3" oninput="saveNote(3, this.value)" rows="3" placeholder="원라이너 문구 및 리드제너레이터 주제 정리..." class="w-full text-xs p-2.5 rounded-lg glow-input shadow-inner resize-none"></textarea>
                    </div>
                </div>
            </div>

            <!-- WEEK 4 -->
            <div id="week-card-4" class="week-card glass-card rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-pink-500 to-rose-500"></div>
                <div>
                    <!-- Card Header -->
                    <div class="flex justify-between items-start mb-4">
                        <div>
                            <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30 mb-1">
                                4단계
                            </span>
                            <h2 class="text-lg font-black text-white">WEEK 4</h2>
                            <p class="text-xs text-pink-300 font-semibold mt-0.5">자동화 + 마케팅 시스템 구축</p>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-pink-500/10 border border-pink-500/30 flex items-center justify-center text-pink-400 text-lg group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-gear"></i>
                        </div>
                    </div>

                    <!-- Checklist -->
                    <div class="space-y-3 mb-6">
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="4" data-idx="0" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>DB 수집 자동화 만들기</strong> <span class="text-[10px] text-gray-400 block">(타입폼, 자피어, make, 스티비, 소셜비즈, 카카오톡)</span>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="4" data-idx="1" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>콘텐츠 시작하기</strong> -&gt; 첫 시작 플랫폼 추천 <span class="text-[10px] text-gray-400 block">(인스타, 유튜브, 블로그, 틱톡, X ...)</span>
                            </span>
                        </label>
                    </div>
                </div>

                <div>
                    <!-- Target Goal Box -->
                    <div class="p-3 rounded-xl bg-pink-950/40 border border-pink-500/30 mb-4">
                        <div class="flex items-center gap-1.5 text-[11px] font-bold text-pink-300 mb-1">
                            <i class="fa-solid fa-bullseye"></i> 이번 주 목표
                        </div>
                        <p class="text-xs text-gray-200 font-medium">"자동으로 팔리는 구조" 세팅 완료</p>
                    </div>

                    <!-- Cyberpunk Note Input -->
                    <div>
                        <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-1.5">
                            <i class="fa-solid fa-pen text-pink-400"></i> 실행 노트 & 아이디어 메모
                        </label>
                        <textarea id="note-4" oninput="saveNote(4, this.value)" rows="3" placeholder="연동 툴 (Zapier/Stibee) 설정 및 마케팅 채널..." class="w-full text-xs p-2.5 rounded-lg glow-input shadow-inner resize-none"></textarea>
                    </div>
                </div>
            </div>

            <!-- WEEK 5 -->
            <div id="week-card-5" class="week-card glass-card rounded-2xl p-5 flex flex-col justify-between relative overflow-hidden group">
                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-amber-500 to-orange-500"></div>
                <div>
                    <!-- Card Header -->
                    <div class="flex justify-between items-start mb-4">
                        <div>
                            <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 mb-1">
                                5단계
                            </span>
                            <h2 class="text-lg font-black text-white">WEEK 5</h2>
                            <p class="text-xs text-amber-300 font-semibold mt-0.5">오픈 -&gt; 피드백 -&gt; 최종 개선</p>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400 text-lg group-hover:scale-110 transition-transform">
                            <i class="fa-solid fa-comments"></i>
                        </div>
                    </div>

                    <!-- Checklist -->
                    <div class="space-y-3 mb-6">
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="5" data-idx="0" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>첫 구매자 5명 확보 목표</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="5" data-idx="1" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                <strong>빠르게 피드백 수집</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="5" data-idx="2" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                제일 많이 묻는 5가지 -&gt; <strong>FAQ 제작</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="5" data-idx="3" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                문제 발견하면 <strong>즉시 업데이트</strong>
                            </span>
                        </label>
                        <label class="flex items-start gap-2.5 cursor-pointer group/item">
                            <input type="checkbox" data-week="5" data-idx="4" onchange="toggleTask(this)" class="custom-checkbox mt-0.5 shrink-0">
                            <span class="text-xs text-gray-300 leading-relaxed group-hover/item:text-white transition-colors">
                                추가 3개 확보 -&gt; <strong>랜딩페이지 추가</strong>
                            </span>
                        </label>
                    </div>
                </div>

                <div>
                    <!-- Target Goal Box -->
                    <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30 mb-4">
                        <div class="flex items-center gap-1.5 text-[11px] font-bold text-amber-300 mb-1">
                            <i class="fa-solid fa-bullseye"></i> 이번 주 목표
                        </div>
                        <p class="text-xs text-gray-200 font-medium">자동화 시스템 및 랜딩페이지 확정/개선</p>
                    </div>

                    <!-- Cyberpunk Note Input -->
                    <div>
                        <label class="block text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-1.5">
                            <i class="fa-solid fa-pen text-amber-400"></i> 실행 노트 & 아이디어 메모
                        </label>
                        <textarea id="note-5" oninput="saveNote(5, this.value)" rows="3" placeholder="초기 구매자 반응 및 FAQ 모음..." class="w-full text-xs p-2.5 rounded-lg glow-input shadow-inner resize-none"></textarea>
                    </div>
                </div>
            </div>

        </main>

        <!-- CORE PRINCIPLES SECTION (핵심 원칙) -->
        <footer class="glass-panel rounded-2xl p-6 relative overflow-hidden border border-white/10">
            <div class="flex items-center gap-2 mb-6">
                <div class="w-8 h-8 rounded-lg bg-gradient-to-tr from-purple-500 to-pink-500 flex items-center justify-center text-white text-sm shadow-md">
                    <i class="fa-solid fa-chart-line"></i>
                </div>
                <h3 class="text-lg font-black text-white tracking-wide">핵심 원칙</h3>
                <span class="text-xs text-gray-400 ml-2 hidden sm:inline"> 성공적인 디지털 상품 비즈니스를 위한 4가지 가이드</span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <!-- Principle 1 -->
                <div class="p-4 rounded-xl bg-white/5 border border-white/5 hover:border-purple-500/30 transition-all flex items-start gap-3">
                    <div class="w-10 h-10 rounded-lg bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400 text-lg shrink-0">
                        <i class="fa-solid fa-user-group"></i>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold text-white mb-1">고객 중심</h4>
                        <p class="text-xs text-gray-400 leading-relaxed">모든 전략은 고객의 문제와 성과에 집중합니다.</p>
                    </div>
                </div>

                <!-- Principle 2 -->
                <div class="p-4 rounded-xl bg-white/5 border border-white/5 hover:border-sky-500/30 transition-all flex items-start gap-3">
                    <div class="w-10 h-10 rounded-lg bg-sky-500/10 border border-sky-500/20 flex items-center justify-center text-sky-400 text-lg shrink-0">
                        <i class="fa-solid fa-gem"></i>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold text-white mb-1">가치 우선</h4>
                        <p class="text-xs text-gray-400 leading-relaxed">먼저 가치를 제공하고 실제 성과를 만듭니다.</p>
                    </div>
                </div>

                <!-- Principle 3 -->
                <div class="p-4 rounded-xl bg-white/5 border border-white/5 hover:border-pink-500/30 transition-all flex items-start gap-3">
                    <div class="w-10 h-10 rounded-lg bg-pink-500/10 border border-pink-500/20 flex items-center justify-center text-pink-400 text-lg shrink-0">
                        <i class="fa-solid fa-sliders"></i>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold text-white mb-1">지속적 개선</h4>
                        <p class="text-xs text-gray-400 leading-relaxed">데이터와 피드백을 기반으로 계속 개선합니다.</p>
                    </div>
                </div>

                <!-- Principle 4 -->
                <div class="p-4 rounded-xl bg-white/5 border border-white/5 hover:border-amber-500/30 transition-all flex items-start gap-3">
                    <div class="w-10 h-10 rounded-lg bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400 text-lg shrink-0">
                        <i class="fa-solid fa-gears"></i>
                    </div>
                    <div>
                        <h4 class="text-sm font-bold text-white mb-1">자동화</h4>
                        <p class="text-xs text-gray-400 leading-relaxed">시스템으로 지속 가능하게 확장합니다.</p>
                    </div>
                </div>
            </div>

            <div class="mt-6 pt-4 border-t border-white/5 flex flex-col sm:flex-row justify-between items-center text-[11px] text-gray-500 gap-2">
                <div>© 2026 Upnomad. All rights reserved. 이 로드맵은 디지털 상품으로 수익을 만들기 위한 가이드입니다.</div>
                <div class="font-semibold text-purple-400 tracking-wider">upnomad</div>
            </div>
        </footer>

    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        // Storage Keys
        const STORAGE_CHECKBOXES = 'upnomad_roadmap_tasks_v1';
        const STORAGE_NOTES = 'upnomad_roadmap_notes_v1';

        let currentViewMode = 'grid'; // 'grid' or 'single'
        let activeSingleTab = 1;

        // Initialize App
        window.addEventListener('DOMContentLoaded', () => {
            loadSavedTasks();
            loadSavedNotes();
            updateProgress();
        });

        // Toggle Task Checkboxes
        function toggleTask(checkbox) {
            saveTasksState();
            updateProgress();
        }

        // Save All Checkbox States to LocalStorage
        function saveTasksState() {
            const checkboxes = document.querySelectorAll('input[type="checkbox"]');
            const state = {};
            checkboxes.forEach(cb => {
                const key = `w${cb.dataset.week}_i${cb.dataset.idx}`;
                state[key] = cb.checked;
            });
            localStorage.setItem(STORAGE_CHECKBOXES, JSON.stringify(state));
        }

        // Load Checkbox States
        function loadSavedTasks() {
            const saved = localStorage.getItem(STORAGE_CHECKBOXES);
            if (!saved) return;
            try {
                const state = JSON.parse(saved);
                const checkboxes = document.querySelectorAll('input[type="checkbox"]');
                checkboxes.forEach(cb => {
                    const key = `w${cb.dataset.week}_i${cb.dataset.idx}`;
                    if (state[key] !== undefined) {
                        cb.checked = state[key];
                    }
                });
            } catch (e) {
                console.error("Failed to load saved task state", e);
            }
        }

        // Save Notes to LocalStorage
        function saveNote(week, value) {
            const saved = localStorage.getItem(STORAGE_NOTES);
            let notesObj = {};
            if (saved) {
                try { notesObj = JSON.parse(saved); } catch(e){}
            }
            notesObj[week] = value;
            localStorage.setItem(STORAGE_NOTES, JSON.stringify(notesObj));
        }

        // Load Notes
        function loadSavedNotes() {
            const saved = localStorage.getItem(STORAGE_NOTES);
            if (!saved) return;
            try {
                const notesObj = JSON.parse(saved);
                for (let i = 1; i <= 5; i++) {
                    const textarea = document.getElementById(`note-${i}`);
                    if (textarea && notesObj[i] !== undefined) {
                        textarea.value = notesObj[i];
                    }
                }
            } catch (e) {
                console.error("Failed to load saved notes", e);
            }
        }

        // Update Overall Progress Calculation
        function updateProgress() {
            const checkboxes = document.querySelectorAll('input[type="checkbox"]');
            const total = checkboxes.length;
            let checked = 0;

            checkboxes.forEach(cb => {
                if (cb.checked) checked++;
            });

            const percent = total > 0 ? Math.round((checked / total) * 100) : 0;

            // UI Update
            document.getElementById('overall-percent').textContent = `${percent}%`;
            document.getElementById('overall-progress-bar').style.width = `${percent}%`;
            document.getElementById('completed-count').textContent = checked;
            document.getElementById('total-count').textContent = total;
        }

        // Reset All Progress & Notes
        function resetAllProgress() {
            if (confirm("모든 진척도와 작성한 메모를 초기화하시겠습니까?")) {
                localStorage.removeItem(STORAGE_CHECKBOXES);
                localStorage.removeItem(STORAGE_NOTES);

                document.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = false);
                document.querySelectorAll('textarea').forEach(ta => ta.value = '');

                updateProgress();
            }
        }

        // View Mode Switcher (Grid vs Single Focus Mode)
        function setViewMode(mode) {
            currentViewMode = mode;
            const container = document.getElementById('weeks-container');
            const tabs = document.getElementById('single-view-tabs');
            const gridBtn = document.getElementById('view-grid-btn');
            const singleBtn = document.getElementById('view-single-btn');

            if (mode === 'grid') {
                container.className = "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-5 mb-8";
                tabs.classList.add('hidden');
                
                // Show all cards
                for (let i = 1; i <= 5; i++) {
                    const card = document.getElementById(`week-card-${i}`);
                    if (card) card.classList.remove('hidden');
                }

                gridBtn.className = "px-3 py-1.5 rounded-md text-xs font-semibold transition-all flex items-center gap-1.5 bg-purple-600 text-white shadow-lg";
                singleBtn.className = "px-3 py-1.5 rounded-md text-xs font-semibold text-gray-400 hover:text-white transition-all flex items-center gap-1.5";
            } else {
                container.className = "grid grid-cols-1 max-w-2xl mx-auto gap-5 mb-8";
                tabs.classList.remove('hidden');

                gridBtn.className = "px-3 py-1.5 rounded-md text-xs font-semibold text-gray-400 hover:text-white transition-all flex items-center gap-1.5";
                singleBtn.className = "px-3 py-1.5 rounded-md text-xs font-semibold transition-all flex items-center gap-1.5 bg-purple-600 text-white shadow-lg";

                setActiveWeekTab(activeSingleTab);
            }
        }

        // Active Tab in Single View Mode
        function setActiveWeekTab(weekNum) {
            activeSingleTab = weekNum;
            if (currentViewMode !== 'single') return;

            // Toggle Visibility
            for (let i = 1; i <= 5; i++) {
                const card = document.getElementById(`week-card-${i}`);
                if (card) {
                    if (i === weekNum) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                }
            }

            // Tab Styling Updates
            const tabBtns = document.querySelectorAll('.week-tab-btn');
            tabBtns.forEach((btn, idx) => {
                if (idx + 1 === weekNum) {
                    btn.classList.add('border-purple-500', 'bg-purple-950/40');
                    btn.classList.remove('border-white/10');
                } else {
                    btn.classList.remove('border-purple-500', 'bg-purple-950/40');
                    btn.classList.add('border-white/10');
                }
            });
        }
    </script>
</body>
</html>