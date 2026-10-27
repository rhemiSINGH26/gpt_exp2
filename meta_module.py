from utils import ask_ollama


def generate_meta_description(blog):

    prompt = f"""
Create an SEO-friendly meta description for the following blog.

Requirements:
- Maximum 160 characters
- Attractive
- Clear
- Include important keywords

Blog:
{blog}

Give only the meta description.
"""

    return ask_ollama(prompt)