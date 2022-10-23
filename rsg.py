#!/bin/python3
from pwn import *
import argparse
import yaml

def getIpAddress(interface):
    Interface = pwnlib.util.net.interfaces4(all=False)
    ip=''.join(Interface.get(bytes(interface, 'utf-8')))
    return ip

def listTypeShell():
    with open('data.yml', 'r') as file:
        prime_service = yaml.safe_load(file)
    return '\n'.join(prime_service['reverse_shell'])

def generateShellforType(rsg):
    return "shell"

def generate(host,port):
    with open('data.yml', 'r') as file:
        prime_service = yaml.safe_load(file)

    for key in prime_service['reverse_shell'].keys():
        print("\n[+]\033[92m{}\033[0m\n\033[1m{}\033[0m".format(key,'\n\n'.join(prime_service['reverse_shell'][key])).replace('[HOST]', host).replace('[PORT]', str(port)))



def main():
    #print("[+] RSG!")
    parser = argparse.ArgumentParser(description='Reverse Shell Generator',prog='rsg.py')
    parser.add_argument('--list',dest='list',action='store_true',help='List All Shell',default=False)
    parser.add_argument('--interface',metavar='tun0',help='Interface (Default=tun0)',default=False)
    parser.add_argument('--host',default='tun0',metavar='192.168.1.2',help='\nIP Address (Default IP for interface tun0)')
    parser.add_argument('--port',default='53',metavar='80',help='Port (Default=53)',type=int)
    parser.add_argument('--generate',dest='generate',action='store_true',help='Generate Shell',default=False, required=True)
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
    else:
        if args.list:
            print(listTypeShell())
    
        if args.generate:
            if args.interface:
                generate(getIpAddress(args.interface),args.port)
            elif args.host == "tun0":
                generate(getIpAddress(args.host),args.port)
            else:
                generate(args.host,args.port)
    

if __name__ == "__main__":
    main()