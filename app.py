import streamlit as st
import google.generativeai as genai

from behavior import get_stage, get_stage_description
from character import CHARACTER_BIBLE
from memory import build_chat_history
from facts import extract_facts, answer_from_facts
from rewards import check_reward
from relationship import (
    create_relationship_state,
    update_relationship_state,
    describe_relationship_state
)
from persistent_memory import load_memory, save_memory


st.set_page_config(
    page_title="i nik AI Prototype",
    page_icon="◧",
    layout="centered"
)


API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

USE_FAKE_AI = False


if "persistent_memory" not in st.session_state:
    st.session_state.persistent_memory = load_memory()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_facts" not in st.session_state:
    st.session_state.user_facts = st.session_state.persistent_memory.get("user_facts", {})

if "intimacy_score" not in st.session_state:
    st.session_state.intimacy_score = st.session_state.persistent_memory.get("intimacy_score", 0)

if "points" not in st.session_state:
    st.session_state.points = st.session_state.persistent_memory.get("points", 0)

if "relationship_state" not in st.session_state:
    st.session_state.relationship_state = st.session_state.persistent_memory.get(
        "relationship_state",
        create_relationship_state()
    )

if "inventory" not in st.session_state:
    st.session_state.inventory = st.session_state.persistent_memory.get("inventory", [])


def persist_current_state():
    save_memory(
        st.session_state.user_facts,
        st.session_state.inventory,
        st.session_state.intimacy_score,
        st.session_state.points,
        st.session_state.relationship_state
    )

    st.session_state.persistent_memory = {
        "user_facts": st.session_state.user_facts,
        "inventory": st.session_state.inventory,
        "intimacy_score": st.session_state.intimacy_score,
        "points": st.session_state.points,
        "relationship_state": st.session_state.relationship_state
    }


stage = get_stage(st.session_state.intimacy_score)
stage_description = get_stage_description(stage)


st.sidebar.header("User State")

st.sidebar.metric("Intimacy", st.session_state.intimacy_score)
st.sidebar.metric("Stage", stage)
st.sidebar.metric("Points", st.session_state.points)

st.sidebar.divider()

st.sidebar.subheader("Relationship")
st.sidebar.metric("Trust", st.session_state.relationship_state["trust"])
st.sidebar.metric("Familiarity", st.session_state.relationship_state["familiarity"])
st.sidebar.metric("Curiosity", st.session_state.relationship_state["curiosity"])

st.sidebar.divider()

st.sidebar.subheader("Memory")

if st.session_state.user_facts:
    for key, value in st.session_state.user_facts.items():
        st.sidebar.write(f"{key}: {value}")
else:
    st.sidebar.write("ยังไม่มีข้อมูลที่จำได้")

st.sidebar.divider()

st.sidebar.subheader("Inventory")

if st.session_state.inventory:
    for item in st.session_state.inventory:
        st.sidebar.write(f"🎁 {item}")
else:
    st.sidebar.write("ยังไม่มีของแปลก")


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

    reward = check_reward(st.session_state.points)

    st.session_state.user_facts = extract_facts(
        user_message,
        st.session_state.user_facts
    )

    st.session_state.relationship_state = update_relationship_state(
        user_message,
        st.session_state.relationship_state
    )

    stage = get_stage(st.session_state.intimacy_score)
    stage_description = get_stage_description(stage)

    relationship_description = describe_relationship_state(
        st.session_state.relationship_state
    )

    chat_history = build_chat_history(
        st.session_state.messages,
        limit=10
    )

    direct_reply = answer_from_facts(
        user_message,
        st.session_state.user_facts
    )

    if direct_reply:
        reply = direct_reply

    else:
        prompt = f"""
{CHARACTER_BIBLE}

กฎบุคลิกตามระดับความสนิท:
{stage_description}

สถานะความสัมพันธ์:
{relationship_description}

ประวัติการคุยล่าสุด:
{chat_history}

ข้อมูลที่จำได้:
{st.session_state.user_facts}

กฎการใช้ความจำ:
- ถ้าข้อมูลที่จำได้มี name ให้ใช้ชื่อนั้นเมื่อตอบคำถามเกี่ยวกับชื่อผู้ใช้
- ห้ามตอบว่าไม่รู้ชื่อ ถ้าในข้อมูลที่จำได้มี name อยู่แล้ว
- ถ้าผู้ใช้ถามว่า "ฉันชื่ออะไร" ให้ตอบจากข้อมูลที่จำได้โดยตรง
- ใช้ความจำอย่างเป็นธรรมชาติ ไม่ต้องประกาศว่าอ่านจากระบบ

ผู้ใช้พูดว่า:
{user_message}
"""

        try:
            if USE_FAKE_AI:
                reply = f"[TEST MODE] ตอนนี้ stage คือ {stage} และ i nik จำข้อมูลนี้ได้: {st.session_state.user_facts}"
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

    persist_current_state()

    st.rerun()