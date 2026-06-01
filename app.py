import streamlit as st
import google.generativeai as genai

from behavior import get_stage, get_stage_description
from character import CHARACTER_BIBLE
from memory import build_chat_history
from facts import extract_facts
from rewards import check_reward
from relationship import create_relationship_state, update_relationship_state, describe_relationship_state
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

if "relationship_state" not in st.session_state:
    st.session_state.relationship_state = create_relationship_state()

if "inventory" not in st.session_state:
    st.session_state.inventory = []

stage = get_stage(st.session_state.intimacy_score)
stage_description = get_stage_description(stage)
st.sidebar.header("User State")

st.sidebar.metric(
    "Intimacy",
    st.session_state.intimacy_score
)

st.sidebar.metric(
    "Stage",
    stage
)

st.sidebar.metric(
    "Points",
    st.session_state.points
)

st.sidebar.divider()

st.sidebar.subheader("Relationship")

st.sidebar.metric(
    "Trust",
    st.session_state.relationship_state["trust"]
)

st.sidebar.metric(
    "Familiarity",
    st.session_state.relationship_state["familiarity"]
)

st.sidebar.metric(
    "Curiosity",
    st.session_state.relationship_state["curiosity"]
)

st.sidebar.divider()

st.sidebar.subheader("Inventory")

if st.session_state.inventory:
    for item in st.session_state.inventory:
        st.sidebar.write(f"🎁 {item}")
else:
    st.sidebar.write("ยังไม่มีของแปลก")

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

    reward = check_reward(
    st.session_state.points
    )

    st.session_state.user_facts = extract_facts(
        user_message,
        st.session_state.user_facts
    )

    st.session_state.relationship_state = update_relationship_state(
        user_message,
        st.session_state.relationship_state
    )

    relationship_description = describe_relationship_state(
        st.session_state.relationship_state
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

สถานะความสัมพันธ์:
{relationship_description}

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

if reward:
    st.session_state.inventory.append(reward)

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"🎁 i nik เจอของแปลกให้เธอ: {reward}"
    })

    st.rerun()