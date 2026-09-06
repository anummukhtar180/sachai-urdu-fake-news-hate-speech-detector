import re

FAKE_NEWS_PATTERNS = [
    "100% true",
    "breaking news",
    "shocking news",
    "viral",
    "فوری خبر",
    "بریکنگ نیوز",
    "حیران کن خبر",
    "وائرل"
]

HATE_SPEECH_PATTERNS = [
    "مار دو",
    "قتل کرو",
    "نفرت",
    "دشمن",
    "kill",
    "hate",
    "attack"
]


def analyze_text(text):
    text_lower = text.lower()

    fake_matches = [
        word for word in FAKE_NEWS_PATTERNS
        if word.lower() in text_lower
    ]

    hate_matches = [
        word for word in HATE_SPEECH_PATTERNS
        if word.lower() in text_lower
    ]

    if hate_matches:
        result = "Hate Speech Detected"
        category = "نفرت انگیز مواد"
    elif fake_matches:
        result = "Potential Fake News"
        category = "ممکنہ جعلی خبر"
    else:
        result = "No Immediate Risk Detected"
        category = "واضح خطرہ نہیں ملا"

    return {
        "result": result,
        "category": category,
        "fake_indicators": fake_matches,
        "hate_indicators": hate_matches
    }


def main():
    print("=" * 50)
    print("SachAI - Urdu Fake News & Hate Speech Detector")
    print("=" * 50)

    text = input("\nاردو یا انگریزی متن درج کریں:\n")

    if not text.strip():
        print("براہ کرم کوئی متن درج کریں۔")
        return

    analysis = analyze_text(text)

    print("\n--- SachAI Analysis ---")
    print("Result:", analysis["result"])
    print("Category:", analysis["category"])

    if analysis["fake_indicators"]:
        print("Fake-news indicators:", analysis["fake_indicators"])

    if analysis["hate_indicators"]:
        print("Hate-speech indicators:", analysis["hate_indicators"])


if __name__ == "__main__":
    main()
