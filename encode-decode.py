#############################

#PROJECT : ENCODER-DECODER

#Language :English


#basic encode and decode

#Contact me  on ;

#Telegram  : Zafiyetsiz0
#Instagram : Zafiyetsiz
#Discord   : Zafiyetsiz#4172

##############################

print("1-Encoder ; 2-Decoder")
choise=int(input("Please type the number of transaction you want :"))
print("-----------------------------------------------------------------------------")
if choise==1:
    letters=("abcdefghijklmnopqrstuvwxyz")

    print("key should be between 1-9999 and do not forget it ;")
    key=int(input("Choose a number for your encode key:"))

    text=input("Enter text for encode:")
    x= len(letters)

    encoded=" "

    for i in text:
        for ii in letters:
            if i == ii:
                number=letters.index(ii)
                number += key
                encoded +=letters[number % x]

    print("Do not forget your key :", key )
    print("Your encoded text :")

    print(encoded)


elif choise==2:
    letters=("abcdefghijklmnopqrstuvwxyz")

    key=int(input("Choose a number for your decode key:"))

    text=input("Enter text for decode:")

    while key==key:
        if key > 26:
            key=key-26
            print(key)
        else:
                break


    print("--------------------------------------------------")


    decoded_key = 26  - key




    x= len(letters)

    decoded=" "

    for i in text:
        for ii in letters:
            if i == ii:
                number=letters.index(ii)
                number += decoded_key
                decoded +=letters[number % x]




    print("Your decoded text :")
    print(decoded)



else:
    print("ERROR : type 1 or 2")
