import sys


for line in sys.stdin:
    # Split the line into fields
    article_id, title, section_title, section_text = line.strip().split(',')
    # Emit each word from the section text with the article ID as the key
    words = section_text.split()
    for word in words:
        print(f"{word.lower()}\t{article_id}\t1")
