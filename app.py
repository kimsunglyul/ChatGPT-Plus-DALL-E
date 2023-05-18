import streamlit as st
import openai
import os

openai.api_key = st.secrets["OPENAI_API_KEY"]
st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("프롬프트")
    gpt_model = st.selectbox("모델", ["gpt-3.5-turbo", "davinci"])
    image_size = st.selectbox("사이즈", ["1024x1024", "512x512", "256x256"])
    surmit = st.form_submit_button("제출")


if surmit and user_input:
   gpt_prompt = [{
       "role": "system",
       "content": "DALL-E 프롬프트로 사용 할 수 있도록 창의적으로 멋지게 묘사해서" 
       "영어로 DALL-E에서 길다고 에러가 발생되지 않도록 작성해주세요."
   }]
   
   gpt_prompt.append({
       "role": "user",
       "content": user_input
   })
   
   with st.spinner("잠시만 기다려주세요..."):
    get_result = openai.ChatCompletion.create(
            model=gpt_model,
            messages=gpt_prompt
    )

    prompt = get_result["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("달리를 잠시만 기다려주세요..."):
        delle_result = openai.Image.create(
        prompt=prompt,
        size=image_size
        )
    
    st.image(delle_result["data"][0]["url"])
else:
    st.write("입력해주세요")
