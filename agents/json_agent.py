import json

def process_json(content: str):
    data = json.loads(content)
    issues = []

    # Example target schema and validation
    required_fields = ['id', 'sender', 'date', 'amount']
    for field in required_fields:
        if field not in data or not data[field]:
            issues.append(f"Missing or empty field: {field}")

    # Optional: reformat or flatten nested structures if needed
    reformatted = {
        'id': data.get('id'),
        'sender': data.get('sender'),
        'date': data.get('date'),
        'amount': data.get('amount'),
        # Add more fields or transform here as needed
    }

    return {
        'type': 'JSON',
        'reformatted': reformatted,
        'issues': issues
    }
