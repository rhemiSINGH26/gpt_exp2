from utils import ask_ollama


def detect_intent(user_input):

    prompt = f"""
You are an intent detection system.

Classify the user's request into exactly ONE of these categories:

BLOG_GENERATION
SUMMARY
KEYWORD_GENERATION
META_DESCRIPTION

User Request:
{user_input}

Return ONLY the category name.
"""

    result = ask_ollama(prompt).strip().upper()

    if "BLOG_GENERATION" in result:
        return "BLOG_GENERATION"

    elif "SUMMARY" in result:
        return "SUMMARY"

    elif "KEYWORD_GENERATION" in result:
        return "KEYWORD_GENERATION"

    elif "META_DESCRIPTION" in result:
        return "META_DESCRIPTION"

    return "UNKNOWN"