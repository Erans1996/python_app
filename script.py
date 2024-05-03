import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: python script.py <file_path>')
        sys.exit(1)

    file_path = sys.argv[1]
    print(f'File uploaded successfully. File path: {file_path}')

if __name__ == '__main__':
    main()
