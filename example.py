from markdown_worker import MarkdownParser


parser = MarkdownParser(filename="example.md")


test_url = "https://example.com/sample.md"
fetch_result = parser.fetch_markdown_from_url(test_url)
print("\nFetching Markdown from URL:")
print(fetch_result)


backup_result = parser.backup_markdown_file("example_backup.md")
print("\nBackup Result:")
print(backup_result)


stats = parser.get_statistics()
print("\nMarkdown File Statistics:")
print(stats)


html_output = parser.markdown_to_html()
print("\nConverted HTML:")
print(html_output)


blockquote_test = parser.search_heading("Blockquote Example")
print("\nBlockquote Test:")
print(blockquote_test)


hr_test = parser.search_heading("Horizontal Rule Example")
print("\nHorizontal Rule Test:")
print(hr_test)


table_test = parser.search_heading("Table Example")
print("\nTable Test:")
print(table_test)


image_test = parser.search_heading("Image Example")
print("\nImage Test:")
print(image_test)


link_test = parser.search_heading("Link Example")
print("\nLink Test:")
print(link_test)


replace_result = parser.find_and_replace("OpenAI", "Markdown Parser")
print("\nFind and Replace Test:")
print(replace_result)


parser.preview_html("test_preview.html")
