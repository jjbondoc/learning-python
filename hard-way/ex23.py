import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line: # the end of the file is an empty string, which has the value False
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # recursive, it stops because of line 7

def print_line(line, encoding, errors):
    next_lang = line.strip() # stripping the \n characters
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)