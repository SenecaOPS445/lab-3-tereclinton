#!/usr/bin/env python3

# Author ID: 119911220

import subprocess

def free_space():
    process = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    grep = subprocess.Popen(['grep', '/$'], stdin=process.stdout, stdout=subprocess.PIPE)
    process.stdout.close()
    awk = subprocess.Popen(['awk', '{print $4}'], stdin=grep.stdout, stdout=subprocess.PIPE)
    grep.stdout.close()
    output, error = awk.communicate()
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())