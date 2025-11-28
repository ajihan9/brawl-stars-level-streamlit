import streamlit as st

# 브롤스타즈 레벨업 PP 및 Gold 비용 배열
pp_cost =   [20, 30, 50, 80, 130, 190, 280, 480, 600, 890]
gold_cost = [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]

def calc_upgrade_cost(start_level, end_level):
    """start_level → end_level 업그레이드 총 비용 계산"""
    total_pp = sum(pp_cost[start_level-1 : end_level-1])
    total_gold = sum(gold_cost[start_level-1 : end_level-1])
    return total_pp, total_gold


# ---------------------------
# Streamlit UI 시작
# ---------------------------

st.title("브롤스타즈 업그레이드 비용 계산기")

st.write("현재 PP, 골드, 브롤러 레벨을 입력하면 필요한 비용을 계산해줍니다!")

current_pp = st.number_input("현재 PP", min_value=0, value=0)
current_gold = st.number_input("현재 골드", min_value=0, value=0)

start_level = st.number_input("현재 레벨 (1~10)", min_value=1, max_value=10, value=1)
end_level = st.number_input("목표 레벨 (2~11)", min_value=2, max_value=11, value=2)

if st.button("계산하기"):
    if end_level <= start_level:
        st.error("목표 레벨은 현재 레벨보다 높아야 합니다.")
    else:
        needed_pp, needed_gold = calc_upgrade_cost(start_level, end_level)

        st.subheader("📌 계산 결과")
        st.write(f"필요한 총 PP : **{needed_pp}**")
        st.write(f"필요한 총 GOLD : **{needed_gold}**")

        # 부족한 양 계산
        if current_pp >= needed_pp:
            st.success("PP가 충분합니다!")
        else:
            st.warning(f"PP가 {needed_pp - current_pp} 부족합니다.")

        if current_gold >= needed_gold:
            st.success("Gold가 충분합니다!")
        else:
            st.warning(f"Gold가 {needed_gold - current_gold} 부족합니다.")
