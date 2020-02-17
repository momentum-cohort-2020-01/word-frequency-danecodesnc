# import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

print(string.punctuation)

with open('seneca_falls.txt', 'r') as f:
    data = f.read()
    print(data)

    remove = dict.fromkeys(map(ord, '\n ' + data.punctuation))

# define punctuation
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


# To take input from the user
my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in data:
   if char not in punctuation:
        no_punct = no_punct + char
        data_lower = no_punct.lower()
        print(no_punct)

split_string = data_lower.split(" ")

print(split_string)

for stop_word in split_string:
    if stop_word in STOP_WORDS:
        split_string.remove(stop_word)

        print(split_string)
        word_dict = {}


# display the unpunctuated string
# print(no_punct)
#This function will get called below
data_split = data_lower.split(" ")
print(data_split)


# Now I want this to be a list of words.    
no_stop_words = ""
for word in data_split:
    if word not in STOP_WORDS:
        no_stop_words = no_stop_words + word
        remove_words = no_stop_words.words()
        print(no_stop_words)
        data_split.remove(word)
        # return data_split



    # remove punctuation from the string

        # def print_word_free(file):
        #     """Read in 'file' and print out the frequency of words in that file."""
        #     pass

# Take everything you've written and put it into this function.
def print_word_freq(file):2
    # """Read in `file` and print out the frequency of words in that file."""
    # pass
with open(file) as file:
        open_file = file.read()
        print(type(open_file))
        print(open_file)
    
    # print(type(file))

def print_word_freq(file):
        open_file(file)


#The function will get called here.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

       

