import PyPDF2

with open("./data/David-A-Phillips-The-Complete-Book-of-Numerology.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    chapters = {}
    current_chapter = None

    print(f'Book metadata: {reader.metadata}')
    print(f'# pages: {len(reader.pages)}')

    # Iterate through each page
    for page_num in range(5, len(reader.pages) - 6):                                        # Skip everything before "Tables of Contents" and after "About Author"
        page = reader.pages[page_num].extract_text()
        if page.startswith("CHAPTER"):                                                      # Detect when a new chapter start and organize the book by chapters
            current_chapter = int(page[len("CHAPTER") + 1: len("CHAPTER") + 3].strip())
        elif page.startswith("CONTENTS"):
            current_chapter = 0                                                             # Chapter 0: Table of contents
        else:
            continue

        if current_chapter not in chapters.keys():
            chapters[current_chapter] = ''

        print(f'Starting chapter {current_chapter}--------------------------------------')
        chapters[current_chapter] += page