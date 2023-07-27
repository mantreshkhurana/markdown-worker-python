from markdown_worker import MarkdownParser

# Create an instance of the MarkdownParser class and provide a Markdown file (replace 'example.md' with your file name).
parser = MarkdownParser(filename='example.md')

# Read the entire contents of the Markdown file.
markdown_text = parser.read_complete_file()
print("Markdown Content:")
print(markdown_text)

# Extract headers and paragraphs from the Markdown file.
headers, paragraphs, header_indices = parser.extract_headers_and_paragraphs()
print("\nHeaders:")
print(headers)
print("\nParagraphs:")
print(paragraphs)

# Search for a specific heading in the Markdown file.
search_heading = "Introduction"
result = parser.search_heading(search_heading)
print(f"\nContent of '{search_heading}' heading:")
print(result)

# Read a specific line from the Markdown file.
line_number = 2
line_content = parser.read_line(line_number)
print(f"\nContent of line {line_number}:")
print(line_content)

# Read a specific word from a specific line in the Markdown file.
line_number = 3
word_number = 1
word_content = parser.read_word(line_number, word_number)
print(f"\nWord at line {line_number}, word {word_number}:")
print(word_content)

# Read a specific character from a specific word in a specific line in the Markdown file.
line_number = 4
word_number = 0
character_number = 2
character_content = parser.read_character(line_number, word_number, character_number)
print(f"\nCharacter at line {line_number}, word {word_number}, character {character_number}:")
print(character_content)

# Read a specific character from a specific line in the Markdown file.
line_number = 5
character_number = 3
character_content = parser.read_character_from_line(line_number, character_number)
print(f"\nCharacter at line {line_number}, character {character_number}:")
print(character_content)

# Read a specific character from the entire Markdown file.
character_number = 10
character_content = parser.read_character_from_file(character_number)
print(f"\nCharacter at index {character_number}:")
print(character_content)

# Convert the Markdown text to HTML.
html_output = parser.markdown_to_html(markdown_text)
print("\nHTML Output:")
print(html_output)
