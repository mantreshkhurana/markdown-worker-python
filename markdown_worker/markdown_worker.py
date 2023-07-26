import re

class MarkdownParser:
    def __init__(self, filename):
        self.filename = filename
        self.markdown_text = self.read_markdown_file()

    def read_markdown_file(self):
        if self.filename.endswith('.md'):
            with open(self.filename, 'r', encoding='utf-8') as file:
                markdown_text = file.read()
                return markdown_text
        else:
            return "File is not a Markdown file."

    def extract_headers_and_paragraphs(self):
        header_pattern = r'^#{1,6}\s(.+)$'
        paragraph_pattern = r'^([^#\n].+)$'

        headers = []
        paragraphs = []
        header_indices = []

        lines = self.markdown_text.split('\n')
        for index, line in enumerate(lines):
            header_match = re.match(header_pattern, line)
            paragraph_match = re.match(paragraph_pattern, line)
            
            if header_match:
                headers.append(header_match.group(1))
                header_indices.append(index)
            elif paragraph_match:
                paragraphs.append(paragraph_match.group(1))

        return headers, paragraphs, header_indices

    def search_heading(self, heading_to_search):
        headers, _, header_indices = self.extract_headers_and_paragraphs()

        if heading_to_search in headers:
            heading_index = headers.index(heading_to_search)
            start_index = header_indices[heading_index]
            if heading_index + 1 < len(header_indices):
                end_index = header_indices[heading_index + 1]
            else:
                end_index = len(self.markdown_text.split('\n'))

            content = '\n'.join(self.markdown_text.split('\n')[start_index:end_index])
            result = content
        else:
            result = "Heading not found in the Markdown file."

        return result
    
    def read_complete_file(self):
        return self.markdown_text
    
    def read_line(self, line_number):
        lines = self.markdown_text.split('\n')
        if line_number < len(lines):
            return lines[line_number]
        else:
            return "Line number out of range."
        
    def read_word(self, line_number, word_number):
        lines = self.markdown_text.split('\n')
        if line_number < len(lines):
            words = lines[line_number].split(' ')
            if word_number < len(words):
                return words[word_number]
            else:
                return "Word number out of range."
        else:
            return "Line number out of range."
        
    def read_character(self, line_number, word_number, character_number):
        lines = self.markdown_text.split('\n')
        if line_number < len(lines):
            words = lines[line_number].split(' ')
            if word_number < len(words):
                characters = list(words[word_number])
                if character_number < len(characters):
                    return characters[character_number]
                else:
                    return "Character number out of range."
            else:
                return "Word number out of range."
        else:
            return "Line number out of range."
        
    def read_character_from_line(self, line_number, character_number):
        lines = self.markdown_text.split('\n')
        if line_number < len(lines):
            characters = list(lines[line_number])
            if character_number < len(characters):
                return characters[character_number]
            else:
                return "Character number out of range."
        else:
            return "Line number out of range."
        
    def read_character_from_file(self, character_number):
        characters = list(self.markdown_text)
        if character_number < len(characters):
            return characters[character_number]
        else:
            return "Character number out of range."
        
    def read_word_from_line(self, line_number, word_number):
        lines = self.markdown_text.split('\n')
        if line_number < len(lines):
            words = lines[line_number].split(' ')
            if word_number < len(words):
                return words[word_number]
            else:
                return "Word number out of range."
        else:
            return "Line number out of range."