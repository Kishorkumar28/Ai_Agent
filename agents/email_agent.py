def process_email(content: str):
    sender = None
    urgency = "normal"

    lines = content.splitlines()
    for line in lines:
        if "From:" in line:
            sender = line.split("From:")[1].strip()
        if "urgent" in line.lower():
            urgency = "high"

    return {
        'type': 'Email',
        'sender': sender,
        'urgency': urgency,
        'body': content
    }
