import os
import filecmp
from filecmp import dircmp

def compare_directories(left_dir, right_dir, output):
    directories_comparison = dircmp(left_dir, right_dir)

    if directories_comparison.left_only:
        for filename in directories_comparison.left_only:
            add_to_nested_collection(output, "files_present_on_left", left_dir, filename)

    if directories_comparison.right_only:
        for filename in directories_comparison.right_only:
            add_to_nested_collection(output, "files_present_on_right", right_dir, filename)

    for filename in directories_comparison.diff_files:
        add_to_nested_collection(output, "differing_files", left_dir, filename)

    for name in directories_comparison.common_dirs:
        new_left_dir = os.path.join(left_dir, name)
        new_right_dir = os.path.join(right_dir, name)
        compare_directories(new_left_dir, new_right_dir, output)

def add_to_nested_collection(main_dict, outer_key, inner_key, new_value):
    if inner_key not in main_dict[outer_key]:
        main_dict[outer_key][inner_key] = []
    main_dict[outer_key][inner_key].append(new_value)

def pretty_print_output(output):
    for key, value in output.items():
        if value:
            print(f"{key.replace('_', ' ').capitalize()}:")
            for sub_key, sub_value in value.items():
                print(f"  In {sub_key}:")
                for item in sub_value:
                    print(f"    - {item}")
            print()

if __name__ == "__main__":
    dir1 = 'Z:\\media' 
    dir2 = 'D:\\media'
    output = {"files_present_on_left": {}, "files_present_on_right": {}, "differing_files": {}}
    compare_directories(dir1, dir2, output)
    pretty_print_output(output)
