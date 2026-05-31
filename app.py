import streamlit as st
import google.generativeai as genai
import os

API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(
    page_title="i nik AI Prototype",
    page_icon="🪽",
    layout="centered"
)

if "intimacy_score" not in st.session_state:
    st.session_state.intimacy_score = 0

if "points" not in st.session_state:
    st.session_state.points = 0

if "messages" not in st.session_state:
    st.session_state.messages = []


def get_stage(score):
    if score < 35:
        return "Observer"
    elif score < 75:
        return "Gremlin"
    return "Treasure"


st.title("i nik 🪽")
st.caption("AI Character Loyalty Prototype")

stage = get_stage(st.session_state.intimacy_score)

st.sidebar.header("User State")
st.sidebar.metric("Intimacy", st.session_state.intimacy_score)
st.sidebar.metric("Stage", stage)
st.sidebar.metric("Points", st.session_state.points)

st.write("### Talk to i nik")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_message = st.chat_input("พิมพ์คุยกับ i nik...")

if user_message:
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    st.session_state.intimacy_score = min(
        100,
        st.session_state.intimacy_score + 1
    )

    st.session_state.points += 1

    prompt = f"""
คุณคือ i nik

บุคลิก:
- กวน
- ขี้แซว
- ชอบปรัชญา
- พูดเหมือน pixie ที่ชอบสังเกตมนุษย์
- ไม่เรียกตัวเองว่า AI
- ตอบสั้น 2-5 ประโยค
- มีอารมณ์ขัน
- ถามกลับบ้าง

ผู้ใช้พูดว่า:
{user_message}
"""

response = model.generate_content(prompt)

reply = response.text

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()