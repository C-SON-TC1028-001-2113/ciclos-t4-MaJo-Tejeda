
def main():


height = int(input("Enter triangle height: "))
x = 2 * height - 2
for y in range(0, height):
    for z in range(0, x):
        print(end=" ")
    x = x - 2
    for z in range(0, y + 1):
        print("* ", end="")
    print("")




if __name__=='__main__':
    main()
