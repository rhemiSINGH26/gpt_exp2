from utils import ask_ollama


def generate_summary(blog):

    prompt = f"""
Summarize the following blog in approximately 100 words.

Blog:
{blog}

Give only the summary.
"""

    return ask_ollama(prompt)