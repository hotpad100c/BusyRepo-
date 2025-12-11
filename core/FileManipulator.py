import random
import string
from datetime import datetime
from RandomContentGenerator import fetch_random_text, fetch_random_word, generate_random_gibberish

def mutate_readme(repo):
    path = "README.md"
    file = repo.get_contents(path)
    content = file.decoded_content.decode()
    
    content_type = random.choice(['text', 'word'])
    if content_type == 'text':
        random_content = fetch_random_text()
    else:
        random_content = fetch_random_word()
    
    new_block = (
        "\n\n---\n"
        f"### Busy at {datetime.utcnow()} UTC\n"
        f"> {random_content}\n"
    )
    new_content = content + new_block
    return path, new_content, file.sha, random_content

def create_random_file(repo):
    file_types = [
        ('notes.txt', 'txt'),
        ('diary.md', 'md'),
        ('log.txt', 'txt'),
        ('thoughts.md', 'md'),
        ('data.txt', 'txt')
    ]
    
    filename, ext = random.choice(file_types)
    filename = fetch_random_word() + "_" + filename
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    path = f"random_files/{filename}"
    
    content_lines = []
    num_lines = random.randint(5, 15)
    
    for i in range(num_lines):
        line_type = random.choice(['text', 'word', 'gibberish'])
        if line_type == 'text':
            content_lines.append(fetch_random_text())
        elif line_type == 'word':
            content_lines.append(fetch_random_word())
        else:
            gibberish_length = random.randint(30, 100)
            content_lines.append(generate_random_gibberish(gibberish_length))
        content_lines.append('\n')
    
    content = ''.join(content_lines)
    
    try:
        file = repo.get_contents(path)
        return path, content, file.sha, fetch_random_text()
    except:
        return path, content, None, fetch_random_text()
