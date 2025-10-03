from src.courses import update_courses_catalog
from src.cleanup import clean_pycache
from src.generate_catalog import main as generate_catalog
import os

project_root = os.path.dirname(os.path.abspath(__file__))

print("Updating courses catalog...")
generate_catalog()
print("Courses catalog updated successfully.")

print("Cleaning up __pycache__ directories...")
clean_pycache(project_root)
print("Cleanup completed successfully.")