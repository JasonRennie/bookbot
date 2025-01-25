def load_book(file_name):
    with open(f"books/{file_name}") as f:
        return f.read()

def print_book(book):
    print(book)

def word_count(book):
    return len(book.split())

def char_counts(book):
    char_counts = {}
    for char in book.lower():
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    return char_counts

def print_report(file_name):
    book = load_book(file_name)

    report_text = []
    report_text.append("Report of books/{file_name}")
    report_text.append(f"{word_count(book)} words in the document")
    chars = char_counts(book)
    for char in chars:
        if not char.isalpha():
            continue
        report_text.append(f"'{char}' was found {chars[char]} times")
    
    print("\n".join(report_text))


print_report("frankenstein.txt")

