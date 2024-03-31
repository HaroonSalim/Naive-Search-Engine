import sys

# Initialize variables to store current word and counts
current_word = None
current_article_ids = []
current_count = 0


for line in sys.stdin:
    # Parse the input line into word, article_id, and count
    word, article_id, count = line.strip().split('\t')
    # Convert count to an integer
    count = int(count)
    # If the word is the same as the current word, update counts
    if word == current_word:
        current_count += count
        # Add article_id to the list if it's not already present
        if article_id not in current_article_ids:
            current_article_ids.append(article_id)
    # If the word is different from the current word, emit the current word and counts
    else:
        # Emit word, article_id list, and total count if the current word is not None
        if current_word:
            print(f"{current_word}\t{current_article_ids}\t{current_count}")
        # Update current word, article_ids, and count
        current_word = word
        current_article_ids = [article_id]
        current_count = count

# Emit the last word, article_ids, and count
if current_word:
    print(f"{current_word}\t{current_article_ids}\t{current_count}")
