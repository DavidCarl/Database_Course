import custom_json
import argparse
import os


db_dict = {}

def startup():
    global db_dict
    if os.path.isfile('simple.db'):
        db_dict = load_from_file()

def db_set(args):
    global db_dict
    db_dict[args.key] = args.value
    save_to_file(db_dict)

def db_read(args):
    global db_dict
    print(db_dict[args.key])

def save_to_file(value):
    string = custom_json.dumps(value).encode('utf-8').hex()
    with open('simple.db', 'w') as f:
        f.write(string)


def load_from_file():
    hex_string = ''
    with open('simple.db', 'r') as f:
        hex_string = f.read()
    return custom_json.loads(bytes.fromhex(hex_string).decode('utf-8'))

def argparse_setup():
    global args
    parser = argparse.ArgumentParser(prog='Task-1',)
    subparsers = parser.add_subparsers()
    
    parser_db_set = subparsers.add_parser('save', help='Save to DB file')
    parser_db_set.add_argument('-k', '--key', type=str, help='This is the key its stored under!')
    parser_db_set.add_argument('-v', '--value', type=str, help='This is the value its storing!')
    parser_db_set.usage = 'python main.py save -k [key_here] -v [value_here]'
    parser_db_set.set_defaults(func=db_set)


    parser_db_read = subparsers.add_parser('read', help='Read from DB file')
    parser_db_read.add_argument('-k', '--key', type=str, help='This is the key you search for!')    
    parser_db_read.set_defaults(func=db_read)

    args = parser.parse_args()

def main():
    startup()
    argparse_setup()
    try:
        args.func(args)
    except:
        pass

if __name__ == '__main__':
    main()
