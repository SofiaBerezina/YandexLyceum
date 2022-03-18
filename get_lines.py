import argparse

try:
    few = None
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', nargs='*')
    args = parser.parse_args()
    assert (0 in args.arg)
    if len([*args.arg]) == 1:
        few = True
        assert (len([*args.arg]) != 1)
    elif len([*args.arg]) > 2:
        few = False
        assert (len([*args.arg]) < 2)
    if args.arg:
        print(sum([*args.arg]))
    else:
        print(f'NO PARAMS')
except AssertionError:
    if few:
        print('TOO FEW PARAMS')
    elif not few:
        print('TOO MANY PARAMS')
    else:
        print('ValueError')