#! /bin/env python

import sys, argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--numero', type=int)

    args = parser.parse_args()

    if not args.numero:
        print("Error: No hay argumentos")
    else:
        if type(args.numero) is int:
            print(int(str(args.numero)[0]))
        else:
            print("Error: Eso no es un número")

if __name__ == "__main__":
    main()
