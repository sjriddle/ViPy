#!/usr/bin/python3
def encryptText(input_text, key):
    input_text = input_text.upper()
    result = ''
    for letter in input_text:
        ascii_value = ord(letter)
        if (ord("A") > ascii_value) or (ascii_value > ord("Z")):
            result += letter
        else:
            key_value = ascii_value + key
            if not((ord("A")) < key_value < ord("Z")):
                key_value=ord("A") + (key_value-ord("A")) % (ord("Z")-ord("A")+1)
            result += str(chr(key_value))
        return result


def main():
    print("Please enter text to scramble: ")
    try:
        user_input = input()
        scrambled_result = encryptText(user_input,10)
        print(f"Result: {scrambled_result}")
        print("To un-scramble, press enter again")
        input()
        unscrambled_result = encryptText(scrambled_result,-10)
        print(f"Result: {unscrambled_result}")
    except UnicodeDecodeError:
        print("Sorry: Only ASCII Characters are supported")    

        
if __name__=="__main__":
  main()
