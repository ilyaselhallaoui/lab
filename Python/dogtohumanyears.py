hundeAlter = int(input("How old is the dog? "))
if hundeAlter == 1:
        print ("The dog is about 14 years old")
elif hundeAlter == 2:
        print ("The dog is about 22 years old")
elif hundeAlter > 2:
        zwischenAlter = hundeAlter - 2
        menschenAlter = zwischenAlter * 5 + 22
        print(f"The dog is {menschenAlter} years old")
else:
    exit()
