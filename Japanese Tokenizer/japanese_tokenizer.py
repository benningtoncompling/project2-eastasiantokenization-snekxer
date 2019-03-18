"""
Japanese Tokenization
For the Japanese tokenization project, you will use the MaxMatch algorithm to read in
a file with lines of Japanese text without spaces, find the word boundaries, and output
a file with the same lines of text with spaces added between words.
./japanese_tokenizer.py <input_file> <output_file>

The MaxMatch algorithm uses a dictionary (japanese_wordlist.txt). Starting from the
beginning of the sentence, match the longest consecutive string of characters that
exists in the dictionary. Once you have found that longest string, insert a space and
continue. If no matches exist in the dictionary, consider the character a one character
word, insert a space and continue.

The sample_out.txt file contains the correctly tokenized output of the in.txt file. Please
check your program output against this file.

gold_standard.txt contains the ideal tokenization. The MaxMatch algorithm makes
mistakes, so don't expect your tokenization output to match this. When you're done
implementing MaxMatch, compare the output of your file to the gold_standard. Make
a file (by hand or programmatically) named evaluation.txt that contains the following:

# of sentences tokenized correctly: <# of lines of output that match gold_standard>
# of sentences tokenized incorrectly: <# of lines of output that don't match
gold_standard>
accuracy: <# correct / total # of sentences>
"""
import sys
import regex
#infile = sys.argv[1]
#outfile = sys.argv[2]

outfile = "out.txt"
infile = open("in.txt", "r", encoding='UTF-8').read()

wordlist = open("japanese_wordlist.txt", "r", encoding='UTF-8').read()

lines = infile.split('\n')
allwords = []
words = []

def matchy(line):
    print(line)
    #reg = r"^)" + regex.escape(line) + r"$"
    if line != "。":
        if line in wordlist:
        #if regex.search(reg, wordlist, flags="MULTILINE"):
            words.append(line)
            return
        else:
            restofline = line
        #reg = r"^)" + regex.escape(restofline) + r"$"
        while restofline not in wordlist:
        #while regex.search(reg, wordlist, flags="MULTILINE"):
            restofline = line[0:len(restofline) - 1]
            # print(restofline)
        words.append(restofline)
        print(restofline)
        restofline = line[len(restofline):len(line)]
        matchy(restofline)
    else:
        words.append(line)


with open(outfile, 'w', encoding='UTF-8') as output:
    for line in lines:
        matchy(line)
        print(words)
        for word in words:
            output.write(word + " ")
        output.write("\n")
        allwords.append((words[:], words[0]))
        words.clear()




