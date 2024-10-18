import os

def print_readme_contents():
    readme_file = os.path.join('resources', 'readme.txt')
    with open(readme_file, 'r') as f:
        contents = f.read()
        print(contents)

if __name__ == '__main__':
    print_readme_contents()