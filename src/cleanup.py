import os
import shutil
import sys

def clean_pycache(root_dir=None):
    """
    Recursively finds and removes all __pycache__ directories
    within the specified root directory.

    Args:
        root_dir (str, optional): The directory path to start searching from.
                                  Defaults to the current working directory.
                                  It's usually best to pass the project root explicitly.
    """
    # If no root directory is specified, default to the current working directory
    if root_dir is None:
        root_dir = os.getcwd()
        print(f"No root directory specified, using current working directory: {root_dir}")
    elif not os.path.isdir(root_dir):
        print(f"Error: Specified root directory '{root_dir}' not found or is not a directory.", file=sys.stderr)
        return # Exit the function if the path is invalid

    print(f"Starting pycache cleanup in: {os.path.abspath(root_dir)}")
    found_count = 0
    removed_count = 0
    failed_removals = []

    # os.walk generates the file names in a directory tree by walking the tree
    # either top-down or bottom-up. For each directory in the tree rooted at
    # directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
    # We use topdown=True (default) to potentially modify dirnames in-place to prune the search.
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
        # Check if '__pycache__' exists in the list of directories for the current dirpath
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            found_count += 1
            print(f"-- Found: {pycache_path}")
            try:
                # Use shutil.rmtree to remove the directory and all its contents
                shutil.rmtree(pycache_path)
                print(f"   Removed: {pycache_path}")
                removed_count += 1
                # Optional: Remove '__pycache__' from dirnames list to prevent
                # os.walk from trying to descend into the directory we just removed.
                # This is good practice, though rmtree should make it a non-issue.
                dirnames.remove('__pycache__')
            except OSError as e:
                # Catch potential errors during removal (e.g., permission errors)
                print(f"   Error removing {pycache_path}: {e}", file=sys.stderr)
                failed_removals.append(pycache_path)
            except Exception as e:
                 # Catch any other unexpected errors
                 print(f"   Unexpected error removing {pycache_path}: {e}", file=sys.stderr)
                 failed_removals.append(pycache_path)


    # Print summary
    print("\nPycache cleanup finished.")
    print(f"Searched directory: {os.path.abspath(root_dir)}")
    print(f"Found {found_count} __pycache__ directories.")
    print(f"Successfully removed {removed_count} directories.")
    if failed_removals:
        print(f"Failed to remove {len(failed_removals)} directories:")
        for path in failed_removals:
            print(f"  - {path}")

# --- Main Execution Block ---
# This part runs only when the script is executed directly (e.g., python cleanup.py)
# It does NOT run when the script is imported into another module.
if __name__ == "__main__":
    print("Running cleanup.py directly...")
    # Determine the project root directory (assuming the script is in the root or a known subdir)
    # For direct execution, often the current working directory is appropriate.
    project_root = os.getcwd()

    # Example: If cleanup.py is inside a 'scripts' folder in your project root,
    # you might want to go one level up:
    # script_dir = os.path.dirname(__file__)
    # project_root = os.path.abspath(os.path.join(script_dir, '..'))

    print(f"Using project root for direct execution: {project_root}")
    clean_pycache(project_root)

