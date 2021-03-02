
print(">>>>>>>>>>>>>>> Binary converter <<<<<<<<<<<<<<<")

run = True
while run:
    text = input("Enter text to convert to  Binary: ")
    print("".join(format(ord(x), "b") for x in text))
    end = input("Would you like to try another one? press 'q' to quit")
    if end == "q":
        run = False
