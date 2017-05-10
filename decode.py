"""
    decoder.py
    Meghan Khurana

    when a digit is found:
    - remember the number value of that digit->type str, cast to int (shift = int(message[i]))
        -- message[i] represents the digit found
    - skip that number of digits ( i = i + message[i] + 1)
        -- message[i] represents the character to be encoded
        -- ok to update because we don't care about the previous characters anymore
    - shift forward one space to resume loop at next digit (i += shift)
        -- message[i] represents next character (should be a digit)
        -- this should shift i past characters that are placeholder digits
"""

def decode(message):

    print "\nencoded message: ", message
    decoded_message = []

    for i in range(0, len(message)):
        if message[i].isdigit():        # loop has found a digit in character string
            shift = int(message[i])     # shift = digit found at message[i]

            # debugging *************************************************************
            # print "mid i: ", i
            # print "shift: ", shift
            # print "add_next: ", add_next
            # print "len(message): ", len(message)
            # print "i + shift + 1: ", i + shift + 1
            # -> current position + shift value + 1 to start shift with placeholders

            # add_next = message[i + shift + 1] --> separate these steps to stay in range
            add_next = i + shift + 1    # add_next = position of letter to be stored
            if add_next < len(message): # if fallen off the loop, the string has ended
                decoded_message.append(message[add_next]) # add decoded character to list
            i += shift + 2                  # updates i to

#            print "end i: ", i, "\n"
#            print decoded_message

    print "decoded message: ", "".join(decoded_message), "\n"


input_message = ["0h2abe1zy", "2xyz", "0h2zyi2467"]
for encode in range(0, len(input_message)):
    decode(input_message[encode])
#
#
# input_message = "0h2abe1zy"
# decode(input_message)
#
# input_message = "2xyz"
# decode(input_message)
#
# input_message = "0h2zyi2467"
# decode(input_message)
