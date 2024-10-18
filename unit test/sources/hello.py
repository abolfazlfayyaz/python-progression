def main():
    name = input("what's your name?")
    outpu = hello(name)
    print(outpu)

def hello(to="World"):
    return f"hello, {to}"
if __name__ == "__main__":
    main()