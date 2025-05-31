from agents.json_agent import process_json

# Read sample JSON file as string
with open("input_samples/sample_invoice.json", "r") as f:
    content = f.read()

result = process_json(content)
print(result)
