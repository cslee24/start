import streamlit as st

st.title('두 숫자 더하기')

# 사용자로부터 두 숫자 입력받기
a = st.number_input('첫 번째 숫자를 입력하세요:', value=10)
b = st.number_input('두 번째 숫자를 입력하세요:', value=20)

# 결과 계산
result = a + b

# 결과 출력
st.write(f'계산 결과: {a} + {b} = {result}')

# 결과를 더 눈에 띄게 보여주기
st.header(f'결과: {result}')

