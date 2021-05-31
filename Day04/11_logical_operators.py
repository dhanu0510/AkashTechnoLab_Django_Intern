n1 = 10
n2 = 20
n3 = 30

# Examples of and
if n1 > n2 and n1 > n3:
    print("n1 is the largest")

if n2 > n1 and n2 > n3:
    print("n2 is the largest")

if n3 > n1 and n3 > n2:
    print("n3 is the largest")


# Examples of or

ch = input("Enter a char:")

if(ch=='A' or ch=='a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U'):
    print(ch, "is a vowel")
else:
    print(ch,"is a consonant")