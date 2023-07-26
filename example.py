from markdown_parser import MarkdownParser

if __name__ == "__main__":
    file_name = input("Enter the path of the Markdown file: ")
    parser = MarkdownParser(file_name)

    heading_to_search = input("Enter the heading to search: ")

    result = parser.search_heading(heading_to_search)

    print("\nContent that was under this heading: \n")
    print(result)
