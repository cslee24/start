import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os

st.title('6하원칙 작문 도우미')

# API 키 입력 받기
api_key = st.text_input("Google API 키를 입력하세요:", type="password")

if api_key:
    # Gemini 모델 설정
    genai.configure(api_key=api_key)
    
    # Google API 인증 정보 설정
    os.environ["GOOGLE_API_KEY"] = api_key
    
    # 6하원칙 입력 필드
    who = st.text_input("누가:")
    when = st.text_input("언제:")
    where = st.text_input("어디서:")
    what = st.text_input("무엇을:")
    how = st.text_input("어떻게:")
    why = st.text_input("왜:")

    # 프롬프트 템플릿 생성
    template = """
    다음 6하원칙을 바탕으로 자연스러운 글을 작성해주세요:
    
    누가: {who}
    언제: {when}
    어디서: {where}
    무엇을: {what}
    어떻게: {how}
    왜: {why}
    """

    prompt = PromptTemplate(
        input_variables=["who", "when", "where", "what", "how", "why"],
        template=template
    )

    if st.button("글 생성하기"):
        try:
            # 모든 필드가 입력되었는지 확인
            if all([who, when, where, what, how, why]):
                # LangChain과 Gemini 연동
                llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", temperature=0.7)
                
                # 프롬프트 생성 및 응답 받기
                formatted_prompt = prompt.format(
                    who=who, when=when, where=where, 
                    what=what, how=how, why=why
                )
                response = llm.invoke(formatted_prompt)
                
                # 결과 표시
                st.subheader("생성된 글:")
                st.write(response.content)
            else:
                st.warning("모든 항목을 입력해주세요.")
                
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
else:
    st.warning("API 키를 입력해주세요.")
