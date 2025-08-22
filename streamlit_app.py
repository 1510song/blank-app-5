import streamlit as st
import random
from datetime import date

# 페이지 제목을 흰색으로 설정
st.markdown("<h1 style='text-align: center; color: white;'>🍀 오늘의 운세 🍀</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>하루에 한 번만 운세를 확인할 수 있습니다.</p>", unsafe_allow_html=True)


# --- 상태 관리 초기화 ---
if 'checked_today' not in st.session_state:
    st.session_state.checked_today = False
if 'last_checked_date' not in st.session_state:
    st.session_state.last_checked_date = None

today = date.today()

# 운세 텍스트 (여기에 직접 운세를 입력하세요!)
fortunes = [
    '오늘은 행운이 가득한 날입니다. 새로운 도전을 두려워하지 마세요!',
    '잠시 쉬어가는 여유를 가져보세요. 예상치 못한 곳에서 좋은 일이 생길 수 있습니다.',
    '노력한 만큼 좋은 결과가 있을 것입니다. 포기하지 않고 꾸준히 나아가세요.',
    '집간다.',
    '집가고싶다.'
]

# --- 운세 확인 로직 ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if not st.session_state.checked_today or st.session_state.last_checked_date != today:
        if st.button('오늘의 운세 확인', use_container_width=True):
            random_fortune = random.choice(fortunes)
            
            st.markdown("<h3 style='text-align: center; color: green;'>🍀 오늘의 운세 결과 🍀</h3>", unsafe_allow_html=True)
            st.info(random_fortune)
            st.balloons()
            
            st.session_state.checked_today = True
            st.session_state.last_checked_date = today

    else:
        st.warning('오늘은 이미 운세를 확인했습니다. 내일 다시 시도해주세요.')