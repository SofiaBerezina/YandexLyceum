import sys

try:
    if '--count' in sys.argv:
        sys.argv.remove('--count')
        count = True
    if '--num' in sys.argv:
        sys.argv.remove('--num')
        num = True
    if '--sort' in sys.argv:
        sys.argv.remove('--sort')
        sort = True
    with open(sys.argv[1]) as f:
        f.readlines()
        print(f)
except IndexError or ValueError:
    print('ERROR')
