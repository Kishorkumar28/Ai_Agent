import json

def process_json(content: str):
    data = json.loads(content)
    issues = []

    # Example target schema and validation
    required_fields = ['id', 'sender', 'date', 'amount']
    for field in required_fields:
        if field not in data or not data[field]:
            issues.append(f"Missing or empty field: {field}")

    reformatted = {
        'id': data.get('id'),
        'sender': data.get('sender'),
        'date': data.get('date'),
        'amount': data.get('amount'),
        # More fields can be added based on the need
    }

    return {
        'type': 'JSON',
        'reformatted': reformatted,
        'issues': issues
    }
