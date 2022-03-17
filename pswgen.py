#!/usr/bin/python3
import argparse
import sys
import random
import time




default_charsets ={
            'd' : '0123456789',       #digits
            'h' : '0123456789abcdef', #hex digits
            'H' : '0123456789ABCDEF', #hex digits capital
            'l' : 'abcdefghijklmnopqrstuvwxyz', #letters
            'L' : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', #letters capital
            's' : '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ', #special characters
            'c' : 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', #cyrillic letters
            'C' : 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', #cyrillic letters capital
            'a' : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ', #all characters except cyrillic
            'A' : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #all characters except cyrillic
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Password generator')

    parser.add_argument('-n', '--numbers', type=int, default=1, help='Numbers of output passwords')
    parser.add_argument('-m', '--mask', type=str, help='Mask for generated passwords')
    parser.add_argument('-c', '--charset', type=str, help='Set custom user charset (use ?u in mask)')

    args = parser.parse_args()

    #print(args)
    if not args.mask:
        print('Mask argument missing! Use ' + sys.argv[0] + ' --help for print help')
        sys.exit(-1)

    #checking mask
    chunk_list = []
    chunk = ''
    special_flag = False
    protected_flag = False

    for c in args.mask:
        if c == '\\' and not protected_flag:
            protected_flag = True
            continue

        if protected_flag:
            chunk = chunk + c
            protected_flag = False
            continue

        if c == '?' and not special_flag:
            special_flag = True
            continue

        if special_flag:
            if chunk:
                chunk_list.append(chunk)
                chunk = ''

            chunk_list.append('?' + c)
            special_flag = False
            continue

        chunk = chunk + c

    if chunk:
        chunk_list.append(chunk)

    #checking chunklist
    charsets = default_charsets
    if args.charset:
        charsets['u'] = args.charset

    charsets_list = list(charsets.keys())

    line = ''

    random.seed(time.time())

    for i in range(0, args.numbers):
        line = ''

        for chunk in chunk_list:
            if chunk[0] == '?':
                if not chunk[1] in charsets_list:
                    print('Wrong mask! Use ' + sys.argv[0] + ' --help for print help')
                    sys.exit(-2)

                line = line + charsets[chunk[1]][random.randrange(0, len(charsets[chunk[1]]))]
                continue

            line = line + chunk

        print(line)

    sys.exit(0)
