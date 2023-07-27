# Markdown Worker

This is a simple markdown parser written in Python. It can read, write and parse markdown files. It can read a particular header, write a particular header, and parse a particular header. It can also parse the entire file.

## Installation

```bash
# use these commands to install the package source code to your local machine
git clone https://github.com/mantreshkhurana/markdown-worker-python.git
cd markdown-worker-python
```

or

```bash
pip install markdown-worker
```

or

```bash
pip3 install markdown-worker
```

## Usage

I provided a `example.md` file in the repository. You can use that to test the program, it contains all the [documentation](https://github.com/mantreshkhurana/markdown-worker-python/blob/stable/example.md) of the program.

```python
from markdown_worker import MarkdownParser

if __name__ == "__main__":
    file_name = input("Enter the path of the Markdown file: ")
    parser = MarkdownParser(file_name)

    heading_to_search = input("Enter the heading to search: ")

    result = parser.search_heading(heading_to_search)

    print("\nContent that was under this heading: \n")
    print(result)
```

## Author

- [Mantresh Khurana](https://github.com/mantreshkhurana)
