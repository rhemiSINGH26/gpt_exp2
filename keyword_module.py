from utils import ask_ollama


def generate_keywords(blog):

    prompt = f"""
Analyze the following blog and generate 10 SEO-friendly keywords.

Blog:
{blog}

Give only the keywords as a numbered list.
"""

    return ask_ollama(prompt)