# Markdown Worker Examples

The `MarkdownParser` class provides various methods to parse and manipulate Markdown files. Here's a detailed explanation of each function and its usage:

## Class: MarkdownParser

### `__init__(self, filename=None)`

- Description: Constructor for the `MarkdownParser` class.
- Parameters:
  - `filename` (optional): A string representing the filename of the Markdown file to read.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  ```

### `read_markdown_file(self)`

- Description: Reads the content of the Markdown file and stores it in the `markdown_text` attribute.
- Returns: The content of the Markdown file as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  content = parser.read_markdown_file()
  ```

### `extract_headers_and_paragraphs(self)`

- Description: Extracts headers and paragraphs from the Markdown file.
- Returns:
  - `headers`: A list of strings containing the header titles.
  - `paragraphs`: A list of strings containing the content of paragraphs.
  - `header_indices`: A list of integers representing the line numbers of the headers in the Markdown file.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  headers, paragraphs, header_indices = parser.extract_headers_and_paragraphs()
  ```

### `search_heading(self, heading_to_search)`

- Description: Searches for a specific header in the Markdown file and returns its content.
- Parameters:
  - `heading_to_search`: A string representing the header title to search for.
- Returns: The content of the header as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  heading_content = parser.search_heading('Introduction')
  ```

### `read_complete_file(self)`

- Description: Returns the complete content of the Markdown file.
- Returns: The content of the entire Markdown file as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  complete_content = parser.read_complete_file()
  ```

### `read_line(self, line_number)`

- Description: Reads a specific line from the Markdown file.
- Parameters:
  - `line_number`: An integer representing the line number to read (0-based index).
- Returns: The content of the specified line as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  line_content = parser.read_line(5)
  ```

### `read_word(self, line_number, word_number)`

- Description: Reads a specific word from a given line in the Markdown file.
- Parameters:
  - `line_number`: An integer representing the line number (0-based index) to read.
  - `word_number`: An integer representing the word number (0-based index) to read.
- Returns: The specified word from the specified line as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  word_content = parser.read_word(10, 3)
  ```

### `read_character(self, line_number, word_number, character_number)`

- Description: Reads a specific character from a given word in a given line in the Markdown file.
- Parameters:
  - `line_number`: An integer representing the line number (0-based index) to read.
  - `word_number`: An integer representing the word number (0-based index) to read.
  - `character_number`: An integer representing the character number (0-based index) to read.
- Returns: The specified character from the specified word in the specified line as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  character = parser.read_character(15, 2, 4)
  ```

### `read_character_from_line(self, line_number, character_number)`

- Description: Reads a specific character from a given line in the Markdown file.
- Parameters:
  - `line_number`: An integer representing the line number (0-based index) to read.
  - `character_number`: An integer representing the character number (0-based index) to read.
- Returns: The specified character from the specified line as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  character = parser.read_character_from_line(20, 10)
  ```

### `read_character_from_file(self, character_number)`

- Description: Reads a specific character from the entire Markdown file.
- Parameters:
  - `character_number`: An integer representing the character number (0-based index) to read.
- Returns: The specified character from the Markdown file as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  character = parser.read_character_from_file(50)
  ```

### `read_word_from_line(self, line_number, word_number)`

- Description: Reads a specific word from a given line in the Markdown file.
- Parameters:
  - `line_number`: An integer representing the line number (0-based index) to read.
  - `word_number`: An integer representing the word number (0-based index) to read.
- Returns: The specified word from the specified line as a string.
- Usage:

  ```python
  parser = MarkdownParser('example.md')
  word_content = parser.read_word_from_line(25, 5)
  ```

### `markdown_to_html(self, markdown_text, output_filename=None)`

- Description: Converts Markdown text to HTML format.
- Parameters:
  - `markdown_text`: A string representing the Markdown content to convert to HTML.
  - `output_filename` (optional): A string representing the filename to save the HTML output. If not provided, the function will only return the HTML string.
- Returns: The Markdown content converted to HTML as a string.
- Usage:

  ```python
  parser = MarkdownParser()
  html_output = parser.markdown_to_html('# Heading 1\n\n**Bold Text**')
  ```

Note: To use most of the functions that read from the Markdown file (e.g., `read_line`, `read_word`, etc.), make sure to initialize the `MarkdownParser` instance with a valid Markdown file using the `filename` parameter. Otherwise, the `markdown_text` will be an empty string.
