def print_the_file_content():


    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)


print_the_file_content()

##########

def number_of_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"The number of words is {len(words)}.")

number_of_words()

#########

def number_of_characters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
        character_counts = {}
        for char in lowered_string:
            if char in character_counts:
                character_counts[char] +=1
            else:
                character_counts[char] = 1
        print(character_counts)

number_of_characters()

##########

def sort_on(dict):
    return dict["num"]

sorted_chars = [


]

with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
        character_counts = {}
        for char in lowered_string:
            if char in character_counts:
                character_counts[char] +=1
            else:
                character_counts[char] = 1

sorted_chars.sort(reverse=True, key=sort_on)
print(sorted_chars)

sort_on()