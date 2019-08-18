# coding = utf-8
# using namespace std
from itertools import combinations_with_replacement
from os import system
from typing import AnyStr
from sys import argv
from color import ColorSystem


class InvalidOption(Exception):
    args = "That's not a valid option!"


def get_possibilities(to_force: str):
    raw_data = combinations_with_replacement(to_force, len(to_force))
    rs = ""
    for i in raw_data: rs += "".join(i) + "\n"
    return rs


def put_on_file(file: AnyStr, content: AnyStr):
    try:
        n = open(file, "w")
        n.write(content)
        del n
    except FileNotFoundError:
        system("touch " + file)
        put_on_file(file, content)


def get_from_file(file_to_get: AnyStr):
    with open(file_to_get, "r") as crypt:
        return crypt.read()


def do_by_arg():
    if argv[1] == "-df":
        dta = get_possibilities(get_from_file(argv[2]))
        put_on_file("./pos.dat", dta)
    elif argv[1] == "-d":
        put_on_file("./pos.dat", get_possibilities(argv[2]))
    elif argv[1] == "-c":
        with open("./pos.dat", "w") as cls: cls.write("")
    elif argv[1] == "-h":
        print("""
        """)
    else: raise InvalidOption


logo = """
  ____ _       _                _       
 / ___(_)_   _| |__  _ __ _   _| |_ ___ 
| |  _| | | | | '_ \| '__| | | | __/ _ \\
| |_| | | |_| | |_) | |  | |_| | ||  __/
 \____|_|\__,_|_.__/|_|   \__,_|\__\___|
"""

if __name__ == "__main__":
    if len(argv) > 1:
        do_by_arg()
        exit(0)
    while True:
        system("clear")
        while True:
            print(logo + f"""

        {ColorSystem().set_color_to("@author GiullianoRossi1987", "yellow")}
        {ColorSystem().set_color_to("@email giulliano.scatalon.rossi@gmail.com", "yellow")}
//////////////////////////////////////////////////////
[1] Decript data
[2] Decript from file
[3] Clean file
[4] Exit
/////////////////////////////////////////////////////

            """)
            opt = int(input(">>>"))
            conf = int(input("Confirm?\n[1] Yes\n[2] No\n>>> "))
            if conf == 1: break
        if opt == 1:
            abort = False
            while True:
                data = str(input("Type the cipher: "))
                conf1 = int(input("Confirm that data?\n[1] Yes\n[2] No\n[3] Abort\n>>> "))
                if conf1 == 3:
                    abort = True
                    break
                if conf1 == 1: break
            if not abort:
                dt = get_possibilities(data)
                put_on_file("./pos.dat", dt)
                print("Done!\nCheck 'pos.dat'!\n")
                input("/////////////////\n<<Press any button to Return>>\n/////////////////")
            continue
        elif opt == 2:
            abort = False
            while True:
                path = str(input("Type the file to decode: "))
                confirm = int(input("Confirm that data?\n[1] Yes\n[2] No\n[3] Abort\n>>> "))
                if confirm == 3:
                    abort = True
                break
            if not abort:
                dt = get_possibilities(get_from_file(path))
                put_on_file("./pos.dat", dt)
                print("Done!\nSee 'pos.dat'")
                input("/////////////////\n<<Press any button to Return>>\n/////////////////")
            continue
        elif opt == 3:
            with open("./pos.dat", "w") as to_clear: to_clear.write("")
            print("Done!")
            input("/////////////////\n<<Press any button to Return>>\n/////////////////")
        else: exit(0)





