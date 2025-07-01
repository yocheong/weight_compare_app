import streamlit as st

st.set_page_config(page_title="무게 비교 시뮬레이터", page_icon="⚖️")

st.title("⚖️ 양팔저울 무게 비교 시뮬레이터")
st.markdown("A, B, C, D 구슬의 무게를 조절해보세요!")

weights = {
    'A': st.slider("A 구슬 무게 (g)", 1, 100, 20),
    'B': st.slider("B 구슬 무게 (g)", 1, 100, 40),
    'C': st.slider("C 구슬 무게 (g)", 1, 100, 70),
    'D': st.slider("D 구슬 무게 (g)", 1, 100, 50)
}

log = []

def compare(ball1, ball2):
    log.append(f"비교: {ball1} vs {ball2}")
    if weights[ball1] < weights[ball2]:
        log.append(f"→ {ball2}가 더 무겁습니다.")
        return ball2
    else:
        log.append(f"→ {ball1}가 더 무겁습니다.")
        return ball1

def insert(ball, sorted_list):
    for i in range(len(sorted_list)):
        heavier = compare(ball, sorted_list[i])
        if heavier == ball:
            continue
        else:
            sorted_list.insert(i, ball)
            return
    sorted_list.append(ball)

def sort_balls():
    balls = list(weights.keys())
    sorted_list = [balls[0]]
    for ball in balls[1:]:
        insert(ball, sorted_list)
    return sorted_list[::-1]

sorted_result = sort_balls()

st.subheader("📋 비교 기록")
for l in log:
    st.write(l)

st.subheader("🏆 결과")
for i, b in enumerate(sorted_result):
    st.write(f"{i+1}위: {b} ({weights[b]}g)")