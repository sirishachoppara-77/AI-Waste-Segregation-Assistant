# AI-Based Waste Segregation & Awareness Assistant
# 1M1B – IBM SkillsBuild AI for Sustainability Internship
# SDG 12: Responsible Consumption and Production

print("🌱 Welcome to the AI Waste Segregation & Awareness Assistant 🌱")
print("Type 'exit' to end the conversation.\n")

def classify_waste(item):
    item = item.lower()

    waste_db = {
        "biodegradable": {
            "items": ["food waste", "vegetable peels", "fruit waste", "leaves"],
            "disposal": "Dispose in compost or wet waste bin.",
            "impact": "Reduces landfill waste and supports composting."
        },
        "recyclable": {
            "items": ["plastic bottle", "glass bottle", "metal can", "paper"],
            "disposal": "Dispose in dry/recyclable waste bin.",
            "impact": "Conserves natural resources through recycling."
        },
        "hazardous": {
            "items": ["battery", "used battery", "e-waste", "medicine"],
            "disposal": "Dispose in designated hazardous or e-waste bins.",
            "impact": "Prevents soil and water pollution from toxic substances."
        }
    }

    for category, data in waste_db.items():
        if item in data["items"]:
            return category.capitalize(), data["disposal"], data["impact"]

    return (
        "Unknown",
        "Follow local waste disposal guidelines.",
        "Responsible disposal helps protect the environment."
    )


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Assistant: Thank you for supporting sustainability 🌍")
        break

    category, disposal, impact = classify_waste(user_input)

    print("\nAssistant:")
    print(f" Waste Category: {category}")
    print(f" Disposal Method: {disposal}")
    print(f" Environmental Impact: {impact}\n")
