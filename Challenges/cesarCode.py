#! /bin/env python

import sys, argparse
#from typing import List

def cifrar(string: str, offset: int = 2) -> str:
    var = ""
    for x in string:
        var += chr((((ord(x)+offset) - 97) % 26) + 97)
    return var

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cifrar', action='store_true', help='Usalo para cifrar')
    parser.add_argument('-d', '--descifrar', action='store_true', help='Usalo para descifrar')
    parser.add_argument('-t', '--texto', nargs='*', help='Parámetro obligatorio para introducir texto.')
    parser.add_argument('-p', '--parametro', type=int, default=2, help='Parametro para elegir el desplazamiento del cifrado César')

    args = parser.parse_args()

    if not args.cifrar and not args.descifrar:
        print("Error: madafaka, que hago")
        exit(1)

    if args.cifrar and args.descifrar:
        print("Error: no puedo hacerlo todo")
        exit(1)

    if args.cifrar:
        n = args.parametro

    if args.descifrar:
        n = -args.parametro

    for x in args.texto:
        print(cifrar(x, n))

if __name__ == "__main__":
    main()
