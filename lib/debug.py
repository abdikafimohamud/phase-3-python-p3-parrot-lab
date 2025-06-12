#!/usr/bin/env python3

import sys
sys.path.append('./lib')  

from parrot import parrot  

if __name__ == '__main__':
    result = parrot("Hello!")
    print(f"Returned: {result}")
