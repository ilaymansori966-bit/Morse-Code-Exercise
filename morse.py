MORSE_TO_CHAR = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"
}

def morse_letter_counter(morse_text):
   morse_text = morse_text.replace(" ", "")
   counts = {}
   for char in morse_text:
       if char in counts:
           counts[char] += 1
       else:
           counts[char] = 1
   max_count = 0
   for c in counts.values():
       if c > max_count:
           max_count = c

   while max_count > 0:
       same_count = ''
       for char in counts:
           if counts[char] == max_count:
               same_count += char
       if same_count != '':
           print(same_count + " - " + str(max_count))
       max_count -= 1


def decode_morse(filename):
    with open(filename, "r") as f:
        morse_text = f.read()

    morse_text += ' '
    message = ''
    morse_char = ''

    for letter in morse_text:
        if letter in '.-':
            morse_char += letter
        elif letter == ' ':
            if morse_char:
                try:
                    message += MORSE_TO_CHAR[morse_char]
                except KeyError:
                    print("Error in Morse Code")
                    return
                morse_char = ''
        elif letter == '/':
            if morse_char:
                try:
                    message += MORSE_TO_CHAR[morse_char]
                except KeyError:
                    print("Error in Morse Code")
                    return
                morse_char = ''
            message += ' '
    print(message)
    morse_letter_counter(message)

decode_morse("C:\\Users\\ilay\\Desktop\\סייבר\\Pycharm\\pythonProject\\פייתון 3\\morse1.txt")
