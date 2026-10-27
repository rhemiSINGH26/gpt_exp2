from utils import ask_ollama


def generate_titles(topic):

    prompt = f"""
Generate 5 attractive and professional blog titles for this topic:

{topic}

Give exactly 5 titles.
Number them from 1 to 5.
"""

    return ask_ollama(prompt)