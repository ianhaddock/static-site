# generate_html.py

import os
import re




def extract_title(markdown: str) -> str:
    """ pulls H1 header from a markdown file and returns it """

    try:
        with open(markdown) as file:
            source = file.read()
    except Exception as e:
        return Exception(f"ERROR: {e}")

    for line in source.splitlines():
        if line.startswith("# "):
            ### regex: replace string that starts with # followed
            ### by one or more whitespace characters with nothing
            ### This catches any extra whitespace before h1 title
            return re.sub(f"^#\s+", '', line)

    raise Exception("No H1 Header found")
