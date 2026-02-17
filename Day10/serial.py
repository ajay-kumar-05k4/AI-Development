import json

data = {
    "student": {
        "name": "Ajai",
        "marks": 88
    },
    "subjects": ["Math", "AI"]
}

json_string = json.dumps(data)

new_data = json.loads(json_string)

print(new_data["student"]["name"])
