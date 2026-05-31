def extract_facts(user_message, facts):

    text = user_message.lower()

    if "ฉันชื่อ" in user_message:
        name = user_message.replace("ฉันชื่อ", "").strip()

        if name:
            facts["name"] = name

    return facts