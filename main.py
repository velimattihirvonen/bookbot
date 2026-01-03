import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(path):
    with open(path, "r", encoding="utf-8") as f:
        file_contents = f.read()
        #print(file_contents)
    return file_contents
    

path = sys.argv[1]

file_contents = main(path)



from stats import word_count, char_count, char_sort

count = word_count(file_contents)

characters = char_count(file_contents)

sorted = char_sort(characters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"{count}")
print("--------- Character Count -------")
for item in sorted:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")

