import re


def clean_value(value):
    value = value.strip()
    value = value.replace("นะ", "").replace("จ้า", "").replace("ค่ะ", "").replace("ครับ", "")
    value = value.strip(" .,!?:;\"'“”‘’")
    return value.strip()


def extract_facts(user_message, facts):
    text = user_message.strip()

    name_patterns = [
        r"ฉันชื่อ\s*([^\n,.!?]+)",
        r"เราชื่อ\s*([^\n,.!?]+)",
        r"ชื่อฉันคือ\s*([^\n,.!?]+)",
        r"ชื่อของฉันคือ\s*([^\n,.!?]+)",
        r"เรียกฉันว่า\s*([^\n,.!?]+)",
        r"เราเรียกว่า\s*([^\n,.!?]+)",
    ]

    for pattern in name_patterns:
        match = re.search(pattern, text)
        if match:
            name = clean_value(match.group(1))
            if name and len(name) <= 30:
                facts["name"] = name

    if "ฉันชอบ" in text:
        liked = clean_value(text.split("ฉันชอบ", 1)[1])
        if liked:
            facts["likes"] = liked

    if "เราชอบ" in text:
        liked = clean_value(text.split("เราชอบ", 1)[1])
        if liked:
            facts["likes"] = liked

    return facts