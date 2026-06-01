from facts import answer_from_facts


def generate_fake_reply(user_message, stage, user_facts, relationship_state, analytics):
    direct_reply = answer_from_facts(user_message, user_facts)

    if direct_reply:
        return f"[DEV TEST MODE]\n{direct_reply}"

    name = user_facts.get("name", "มนุษย์")

    trust = relationship_state.get("trust", 0)
    familiarity = relationship_state.get("familiarity", 0)
    curiosity = relationship_state.get("curiosity", 0)

    engagement = analytics.get("engagement_score", 0)

    return (
        f"[DEV TEST MODE] i nik เห็นอยู่นะ {name}\n\n"
        f"Stage: {stage}\n"
        f"Trust: {trust}\n"
        f"Familiarity: {familiarity}\n"
        f"Curiosity: {curiosity}\n"
        f"Engagement: {engagement}\n\n"
        "ระบบ memory / relationship / analytics กำลังทำงานอยู่ "
        "แต่ข้อความนี้ไม่ได้ยิง Gemini API"
    )