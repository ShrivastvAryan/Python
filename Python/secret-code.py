
def coding():
    a=input("Enter the word:")

    b=input("You want to code the message Yes/No: ")

    if(b=='Yes'):
        if(len(a)<3):
            coded_small=a[::-1]
            return coded_small
        else:
            a=a[::-1]
            c=a[0:2]
            coded_large=a[2]+c
            return coded_large

    else:
        print("You dont want to code the text")


def decoding():
    decoding=input("Do u want to decode Yes/No: ")

    if(decoding=='Yes'):
        if(coded_small):
            decoded_small=coded_small[::-1]
            print('Decoded word is: ',decoded_small)
        else:
            decoded_large=coded_large[::-1]
            decoded_large=decoded_large-coded_large
            print('decoded one is:',decoded_large)


        