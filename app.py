import streamlit as st

# ----------------------------------------
# 브롤스타즈 테마 스타일(CSS)
# ----------------------------------------
st.markdown("""
    <style>
        body {
            background-color: #0073E6 !important;
        }
        .main {
            background-color: #0073E6;
        }
        .title-text {
            color: white;
            text-align: center;
            font-size: 38px;
            font-weight: 800;
            text-shadow: 2px 2px 4px #000000;
        }
        .box {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
            margin-top: 20px;
        }
        .result-box {
            background: #F7D308;
            padding: 20px;
            border-radius: 12px;
            font-size: 20px;
            margin-top: 15px;
            color: #1B1B1B;
            font-weight: 600;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
        }
        .btn {
            background-color: #F7D308 !important;
            color: #1B1B1B !important;
            border-radius: 10px !important;
            font-weight: 700 !important;
            font-size: 18px !important;
        }
    </style>
""", unsafe_allow_html=True)


# ----------------------------------------
# 브롤스타즈 아이콘 (인터넷 URL 사용)
# ----------------------------------------
st.image(
    "https://static.wikia.nocookie.net/brawlstars/images/9/94/Logo.png",
    width=180
)


# 제목
st.markdown("<h1 class='title-text'>브롤스타즈 업그레이드 비용 계산기</h1>", unsafe_allow_html=True)


# 업그레이드 비용 데이터
pp_cost =   [20, 30, 50, 80, 130, 190, 280, 480, 600, 890]
gold_cost = [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]

def calc_upgrade_cost(start_level, end_level):
    total_pp = sum(pp_cost[start_level-1 : end_level-1])
    total_gold = sum(gold_cost[start_level-1 : end_level-1])
    return total_pp, total_gold


# 입력창 박스
with st.container():
    st.markdown("<div class='box'>", unsafe_allow_html=True)

    current_pp = st.number_input("현재 PP", min_value=0, value=0)
    current_gold = st.number_input("현재 골드", min_value=0, value=0)
    start_level = st.number_input("현재 레벨 (1~10)", min_value=1, max_value=10, value=1)
    end_level = st.number_input("목표 레벨 (2~11)", min_value=2, max_value=11, value=2)

    calculate = st.button("계산하기", key="calc_button")

    st.markdown("</div>", unsafe_allow_html=True)


# 클릭 시 결과 출력
if calculate:
    if end_level <= start_level:
        st.error("⚠ 목표 레벨은 현재 레벨보다 높아야 합니다!")
    else:
        needed_pp, needed_gold = calc_upgrade_cost(start_level, end_level)

        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.subheader("📌 계산 결과")
        st.write(f"🔸 필요한 총 PP : **{needed_pp}**")
        st.write(f"🔸 필요한 총 GOLD : **{needed_gold}**")

        if current_pp >= needed_pp:
            st.success("✔ PP가 충분합니다!")
        else:
            st.warning(f"⚠ PP가 {needed_pp - current_pp} 부족합니다.")

        if current_gold >= needed_gold:
            st.success("✔ Gold가 충분합니다!")
        else:
            st.warning(f"⚠ Gold가 {needed_gold - current_gold} 부족합니다.")

        st.markdown("</div>", unsafe_allow_html=True)
