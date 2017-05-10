"""
    decoder.py
    Meghan Khurana
"""

def decode(message):
    print message
    decoded_message = []
    shift = 1
    add_next = 0
    print len(message)
    for i in range(0, len(message)):
        print "beg i: ", i
        if message[i].isdigit():
#            print "char/message[i]: ", message[i]
#            print type(message[i])
            add_next = i + int(message[i]) + 1
            print "shift: ", shift
            print "add_next: ", add_next
            i += shift
            print "end i: ", i, "\n"
            decoded_message.append(message[add_next])
            print decoded_message
#            print "decoded message string: ", "".join(decoded_message)
    print "decoded message string: ", "".join(decoded_message)


input_message = "0h2zyi2467"
decode(input_message)
