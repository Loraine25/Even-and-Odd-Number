#Anonuevo, Loraine N. 
#BSCpE 1-4
#Even and Odd Text Files

#Header
print("\033[;33;1;3m\033[10m" * 65)
print("\033[;33;1;3mHello! I'm Loraine, and I'll be your programmer for today!\033[0m".center(81))
print("\033[;33;1;3mಠ\033[10m" * 65)

# Open numbers.txt (read), even.txt (append), odd.txt (append)
with open("numbers.txt") as number_txt_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
    # Read numbers.txt line by line
    numbers = number_txt_file.readlines()
    for line in numbers:
        # If even,
        if int(line) % 2 == 0:
            even_file.write(str(line))
        # If odd
        else:
            odd_file.write(str(line))

