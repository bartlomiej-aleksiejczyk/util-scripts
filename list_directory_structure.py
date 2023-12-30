import os
import sys
import fnmatch

def parse_gitignore(gitignore_path):
    ignore_patterns = ['./.git', './list_directory_structure.py', './.idea']  # Always ignore .git directory
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    ignore_patterns.append(stripped_line)
    return ignore_patterns

def is_ignored(path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def list_directory_structure(startpath, ignore_git):
    ignore_patterns = []
    if ignore_git:
        gitignore_path = os.path.join(startpath, '.gitignore')
        ignore_patterns = parse_gitignore(gitignore_path)

    for root, dirs, files in os.walk(startpath, topdown=True):
        dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d), ignore_patterns)]
        files = [f for f in files if not is_ignored(os.path.join(root, f), ignore_patterns)]

        if not files and not dirs:
            continue

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)

        for f in files:
            print(f"{subindent}{f}")

if __name__ == "__main__":
    directory = '.'
    ignore_git = False

    if len(sys.argv) == 2:
        if sys.argv[1].lower() == 'true' or sys.argv[1].lower() == 'false':
            ignore_git = sys.argv[1].lower() == 'true'
        else:
            directory = sys.argv[1]
    elif len(sys.argv) > 2:
        directory = sys.argv[1]
        ignore_git = sys.argv[2].lower() == 'true'

    list_directory_structure(directory, ignore_git)
