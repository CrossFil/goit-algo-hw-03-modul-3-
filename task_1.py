import os
import shutil
import argparse

def copy_files_recursively(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for item in os.listdir(src):
        s = os.path.join(src, item)
        if os.path.isdir(s):
            copy_files_recursively(s, dst)
        else:
            file_extension = os.path.splitext(item)[1][1:]
            target_dir = os.path.join(dst, file_extension)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            shutil.copy2(s, target_dir)

def main():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument("src", help="Source directory")
    parser.add_argument("dst", nargs="?", default="dist", help="Destination directory (default: dist)")
    args = parser.parse_args()

    try:
        copy_files_recursively(args.src, args.dst)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
