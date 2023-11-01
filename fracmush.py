# Here is a healthy reserve of 🍄🍄🍄🍄

import sys
import re
import os

from datetime import datetime

EXTENSION_TO_COMMENT = {
    "py":"#",
    "c":"//"
}

def get_current_date(comment: str) -> str:
    return comment+" 🍄 "+(datetime.now().strftime("%Y-%m-%d %H:%M"))+"\n\n"

def compute_replacement(match: str) -> str:
    content_filename = match.split()[0]
    with open(content_filename, 'r') as content:
        li = content.readlines()
        



def extract_content(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as file:
        content = file.read()
        pattern = r'🍄([^\n]*?)🍄'
        matches = re.findall(pattern, content, re.DOTALL)
        for match in matches:
            content = content.replace('🍄' + match + '🍄', match + '888')
        
    # Write the modified content to the output file
    with open(output_file, 'w') as file:
        try:
            ext = output_file.split(".")[-1]

            if ext in EXTENSION_TO_COMMENT:
                content = get_current_date(EXTENSION_TO_COMMENT[ext])+content
        finally:
            file.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_filename> <output_filename>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        os.system("rm "+output_file)
        extract_content(input_file, output_file)
