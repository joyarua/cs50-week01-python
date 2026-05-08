def convert(str):
    str = str.replace(":)","🙂")
    str = str.replace(":(","🙁")
    return str
def main():
    text = input()
    print(convert(text))
main()
