import streamlit as st
import google.generativeai as genai

from behavior import get_stage, get_stage_description
from character import CHARACTER_BIBLE
from memory import build_chat_history
from facts import extract_facts
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

USE_FAKE_AI = False
st.set_page_config(
    page_title="i nik AI Prototype",
    page_icon="◧",
    layout="centered"
)

if "intimacy_score" not in st.session_state:
    st.session_state.intimacy_score = 0

if "points" not in st.session_state:
    st.session_state.points = 0

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_facts" not in st.session_state:
    st.session_state.user_facts = {}

stage = get_stage(st.session_state.intimacy_score)
stage_description = get_stage_description(stage)
st.sidebar.header("User State")
st.sidebar.metric("Intimacy", st.session_state.intimacy_score)
st.sidebar.metric("Stage", stage)
st.sidebar.metric("Points", st.session_state.points)

st.title("i nik ◧")
st.caption("AI Character Loyalty Prototype")
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
        st.session_state.intimacy_score + 10
    )

    st.session_state.points += 1

    st.session_state.user_facts = extract_facts(
        user_message,
        st.session_state.user_facts
    )

    chat_history = build_chat_history(
        st.session_state.messages,
        limit=10
    )

    prompt = f"""
{CHARACTER_BIBLE}

กฎบุคลิกตามระดับความสนิท:
{stage_description}

ประวัติการคุยล่าสุด:
{chat_history}

ข้อมูลที่จำได้:
{st.session_state.user_facts}

ผู้ใช้พูดว่า:
{user_message}
"""

    try:
        if USE_FAKE_AI:
            reply = f"[TEST MODE] ตอนนี้ stage คือ {stage} และ i nik จำแชตล่าสุดได้แล้ว"
        else:
            response = model.generate_content(prompt)
            reply = response.text
    except Exception as e:
        reply = f"ERROR: {e}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()