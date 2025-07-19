from translator import translate_text

def run_agent():
    print("🌐 Language Translator Agent")
    input_text = input("Enter text: ")
    target_lang = input("Translate to (e.g., Urdu, French, Hindi): ")
    
    translated = translate_text(input_text, target_lang)
    print(f"\n🗣️ Translated Text: {translated}")

if __name__ == "__main__":
    run_agent()