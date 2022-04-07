import argparse

try:
    few = None
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', nargs='*')
    args = parser.parse_args()
    print(args.arg)
    assert len(args.arg) == 2
    if len(args.arg) < 2 and len(args.arg) != 0:
        few = True
    elif len(args.arg) > 2:
        few = False
    for i in args.arg:
        if float(i) != int(i):

except AssertionError:
    if few:
        print('TOO FEW PARAMS')
    elif not few:
        print('TOO MANY PARAMS')
except Exception as e:
print(e.__class__.__name__)