#!/usr/bin/python3

import argparse
import os

def parse_args():
    # Crea el parser
    parser = argparse.ArgumentParser()

    # Añade los argumentos
    parser.add_argument("-u", "--user", required=True, help="Usuario objetivo")
    parser.add_argument("-w", "--wordlist", required=True, help="Ruta del diccionario")

    # Parsea los argumentos
    args = parser.parse_args()

    # Uso de los valores
    return parser.parse_args()

    if not os.path.isfile(args.wordlist):
        print("El diccionario no existe")
        exit(0)

def printArgs():
    args = parse_args()

    print(args.user)
    print(args.wordlist)
        

printArgs()
