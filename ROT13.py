import string
alpha1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alpha2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

def encode(strEnc):
     return strEnc.translate(str.maketrans(alpha1, alpha2))
def decode(strEnc):
    return strEnc.translate(str.maketrans(alpha2, alpha1))

inpWhich = str(input("Are we encoding or decoding? (E/D): "))

if(inpWhich == "E"):
    inpSent = str(input("Enter the string to encode: "))
    print(encode(inpSent))
else:
    inpSent = str(input("Enter the string to decode: "))
    print(decode(inpSent))