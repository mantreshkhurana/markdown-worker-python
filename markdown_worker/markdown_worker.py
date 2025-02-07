import re
import markdown
import requests


class MarkdownParser:
    def __init__(self, filename=None):
        self.filename = filename
        self.markdown_text = self.read_markdown_file() if filename else ""
        self.lines = self.markdown_text.split("\n")

    def read_markdown_file(self):
        if self.filename and self.filename.endswith(".md"):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    return file.read()
            except IOError:
                return "Error: unable to read the markdown file."
        return "Error: file is not a markdown file."

    def extract_headers_and_paragraphs(self):
        header_pattern = r"^#{1,6}\s(.+)$"
        paragraph_pattern = r"^[^#\n].+$"

        headers = []
        paragraphs = []
        header_indices = []

        for index, line in enumerate(self.lines):
            if re.match(header_pattern, line):
                headers.append(line.strip("# ").strip())
                header_indices.append(index)
            elif re.match(paragraph_pattern, line):
                paragraphs.append(line)

        return headers, paragraphs, header_indices

    def search_heading(self, heading_to_search):
        headers, _, header_indices = self.extract_headers_and_paragraphs()

        if heading_to_search in headers:
            heading_index = headers.index(heading_to_search)
            start_index = header_indices[heading_index]
            end_index = (
                header_indices[heading_index + 1]
                if heading_index + 1 < len(header_indices)
                else len(self.lines)
            )
            return "\n".join(self.lines[start_index:end_index])
        return "Heading not found in the markdown file."

    def read_complete_file(self):
        return self.markdown_text

    def markdown_to_html(self, markdown_text=None, output_filename=None):
        markdown_text = markdown_text if markdown_text else self.markdown_text

        # Convert Markdown to HTML using markdown library
        html_text = markdown.markdown(
            markdown_text, extensions=["extra", "tables", "fenced_code"]
        )

        if output_filename:
            try:
                with open(output_filename, "w", encoding="utf-8") as output_file:
                    output_file.write(html_text)
            except IOError:
                return "Error: unable to write to the output file."

        return html_text

    def fetch_markdown_from_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.markdown_text = response.text
                self.lines = self.markdown_text.split("\n")
                return "Markdown content fetched successfully."
            return "Error: Unable to fetch the content."
        except requests.RequestException:
            return "Error: Invalid URL or network issue."

    def backup_markdown_file(self, backup_filename):
        try:
            with open(backup_filename, "w", encoding="utf-8") as backup_file:
                backup_file.write(self.markdown_text)
            return "Backup created successfully."
        except IOError:
            return "Error: Unable to create a backup."

    def interactive_mode(self):
        print("Enter Markdown text (type 'EXIT' to finish):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "EXIT":
                break
            lines.append(line)
        self.markdown_text = "\n".join(lines)
        print("Converted HTML:\n", self.markdown_to_html())

    def preview_html(self, output_filename="preview.html"):
        html_content = self.markdown_to_html()
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(html_content)
        import webbrowser

        webbrowser.open(output_filename)

    def find_and_replace(self, find_text, replace_text):
        if find_text in self.markdown_text:
            self.markdown_text = self.markdown_text.replace(find_text, replace_text)
            return "Text replaced successfully."
        return "Text not found."

    def get_statistics(self):
        word_count = len(re.findall(r"\b\w+\b", self.markdown_text))
        char_count = len(self.markdown_text)
        line_count = len(self.lines)
        return {"Words": word_count, "Characters": char_count, "Lines": line_count}


# Example Usage:
if __name__ == "__main__":
    parser = MarkdownParser("example.md")
    print(parser.markdown_to_html())
