import streamlit as st

# 🌐 앱 설정
st.set_page_config(page_title="무게 비교 시뮬레이터", page_icon="⚖️")

# 🖼️ 상단 이미지 삽입 (웹 이미지 사용)
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Balance_scale_justice.svg/600px-Balance_scale_justice.svg.png",
    caption="양팔저울로 무게 순서를 알아보는 체험 활동",
    use_column_width=True
)

# 🧾 제목 및 설명
st.title("⚖️ 양팔저울 무게 비교 시뮬레이터")
st.markdown("""
슬라이더를 움직여 A, B, C, D 구슬의 무게를 직접 설정해보세요.  
알고리즘이 구슬을 비교해가며 **무게 순서를 자동으로 정렬**해드립니다!
""")

# ⚙️ 사용자 입력
weights = {
    'A': st.slider("🔴 A 구슬 무게", 1, 100, 25),
    'B': st.slider("🟢 B 구슬 무게", 1, 100, 50),
    'C': st.slider("🔵 C 구슬 무게", 1, 100, 70),
    'D': st.slider("🟣 D 구슬 무게", 1, 100, 40)
}

# 📋 비교 과정 로그 저장
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
    return sorted_list[::-1]  # 무거운 순서로 반환

# 🧮 정렬 실행
sorted_result = sort_balls()

# 📋 비교 기록 출력
st.subheader("📌 비교 과정")
for entry in log:
    st.write(entry)

# 🏆 결과 출력
ball_icons = {'A': '🔴', 'B': '🟢', 'C': '🔵', 'D': '🟣'}
st.subheader("🏆 무거운 순서")
for i, b in enumerate(sorted_result):
    st.markdown(f"**{i+1}위: {ball_icons[b]} {b} ({weights[b]}g)**")

# 🎉 응원 메시지
st.success("🎉 잘했어요! 정렬 결과가 위에 표시되었어요. 다시 무게를 바꾸어보며 연습해보세요!")