# generate_html.py

import re
import os

from markdown_to_html import (
    markdown_to_html_node
    )


def extract_title(markdown: str) -> str:
    """ pulls H1 header from a markdown text and returns it """

    for line in markdown.splitlines():
        if line.startswith("# "):
            line = line.rstrip()
            # regex: replace string that starts with # followed
            # by one or more whitespace characters with nothing
            # This catches any extra whitespace before h1 title
            return re.sub(r"^#\s+", '', line)

    raise Exception("No H1 Header found")


def generate_pages(from_path: str, template_path: str, dest_path: str) -> None:
    """ reads markdown for title and contents and build HTML file from a template """

    print(f'Generating page from {from_path} to {dest_path} using {template_path}.')

    try:
        with open(template_path) as file:
            template = file.read()
    except Exception as e:
        raise Exception(f"ERROR: Can't read template file. {e}")

    try:
        markdown_files = os.listdir(from_path)
    except Exception as e:
        raise Exception(f"ERROR: Can't find path. {e}")

    for file in markdown_files:
        if os.path.isdir(os.path.join(from_path, file)):
            os.mkdir(os.path.join(dest_path, file))
            return generate_pages(os.path.join(from_path, file), template_path,
                          os.path.join(dest_path, file))

        try:
            with open(os.path.join(from_path, file), "r") as file:
                markdown_file = file.read()
        except OSError as e:
            raise Exception(f"ERROR: Can't read markdown. {e}")

        file_title = extract_title(markdown_file)
        file_content = markdown_to_html_node(markdown_file)
        composed_file = re.sub(r"\s+{{ Title }}\s+", file_title, template)
        composed_file = re.sub(r"\s+{{ Content }}\s+", file_content.to_html(), composed_file)

        # get the file name without path and drop the .md extension
        filename = os.path.basename(file.name)
        filename = filename[:-3]

        try:
            with open(os.path.join(dest_path, f'{filename}.html'), "w") as dest_file:
                dest_file.write(composed_file)
        except Exception as e:
            raise Exception(f'ERROR: Cant write to file. {e}')







