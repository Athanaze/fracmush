def extract_content(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as file:
        content = file.read()
        pattern = r'🍄([^\n]*?)🍄'
        matches = re.findall(pattern, content, re.DOTALL)
        for match in matches:
            content = re.sub(pattern, match+'999', content)
            print(match)
        # Replace the matched string with '999'
        # content = re.sub(pattern, '999', content)
        
    # Write the modified content to the output file
    with open(output_file, 'w') as file:
        try:
            ext = output_file.split(".")[-1]

            if ext in EXTENSION_TO_COMMENT:
                content = get_current_date(EXTENSION_TO_COMMENT[ext])+content
        finally:
            file.write(content)