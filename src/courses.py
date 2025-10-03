import re
import unicodedata
from collections import defaultdict
from pathlib import Path
import string
from typing import Optional, List, Dict, Tuple, DefaultDict, Any, Literal
from datetime import datetime
import time

# --- Constants ---
BASE_DIR: str = "courses"
OUTPUT_FILENAME: str = "courses.md"
MAX_LEVEL: int = 4  # Set maximum heading level to include (e.g., 2, 3, or 4)
INDENT_SPACES: str = "    " # 4 spaces for indentation
StyleType = Literal['title', 'sentence', 'upper', 'lower']


# --- Helper Functions ---

def get_timestamp(format_string = "%Y-%m-%d %I:%M %p %Z") -> str:
    # Example: 2025-04-15 02:34 PM CDT
    
    # Get current local time
    now_aware = datetime.now().astimezone()
    timestamp_str = now_aware.strftime(format_string)

    return timestamp_str

def generate_anchor(text: str) -> str:
    """Generates a GitHub-style anchor link from heading text."""
    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    except TypeError:
         pass
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+|-+', '-', text)
    text = text.strip('-')
    return text

HEADING_REGEX = re.compile(r"""
    ^(\#{1,6})       # Capture group 1: Heading level (1-6 '#' chars)
    \s+             # One or more whitespace chars
    (?:             # Non-capturing group for link formats or plain text
        \[([^\]]+)\] # Capture group 2: Text within brackets [Linked Text](...)
        \(.*?\)       # Must be followed by (...)
    |
        \[([^\]]+)\] # Capture group 3: Text within brackets [Linked Text][...]
        \[.*?\]       # Must be followed by [...]
    |
        \[([^\]]+)\] # Capture group 4: Text within brackets [Just Brackets]
    |
        ([^#\n\[]+)    # Capture group 5: Plain text heading (cannot start with '[')
    )
""", re.VERBOSE)


def extract_heading_info(line: str) -> Optional[Tuple[int, str]]:
    """
    Extracts heading level (1-6) and the visible text from a Markdown heading line.
    Handles: Plain Text, [Linked Text](...), [Linked Text][...], and [Just Brackets].
    Returns (level, text) tuple or None if not a valid heading.
    """
    match = HEADING_REGEX.match(line)
    if match:
        level = len(match.group(1))
        text = next((group for group in match.groups()[1:] if group is not None), None)
        return (level, text.strip()) if text else None
    return None

def format_display_name(text: str, style: StyleType = 'title') -> str:
    """
    Formats text using different capitalization styles, handling hyphens/underscores.

    Args:
        text: The input string to format.
        style: The desired capitalization style. Valid options are:
               'title'    (Default): Capitalizes the first letter of each word.
               'sentence': Capitalizes only the first letter of the first word.
               'upper'   : Converts the entire text to UPPERCASE.
               'lower'   : Converts the entire text to lowercase.

    Returns:
        The formatted string, or an empty string if input is not a valid string.
        Defaults to 'title' case if an invalid style is provided.
    """
    if not isinstance(text, str):
        return "" # Return empty for non-string input

    # Replace underscores and hyphens with a single space using regex
    processed_text = re.sub(r'[_-]+', ' ', text).strip() # Also strip leading/trailing spaces

    # Ensure style comparison is case-insensitive
    style_lower = style.lower()

    if style_lower == 'title':
        return string.capwords(processed_text)
    elif style_lower == 'sentence':
        if not processed_text:
            return ""
        # Lowercase the whole string first, then capitalize the first letter
        return processed_text[0].upper() + processed_text[1:].lower()
    elif style_lower == 'upper':
        return processed_text.upper()
    elif style_lower == 'lower':
        return processed_text.lower()
    else:
        # Default fallback for unknown style - return title case
        # Optionally, print a warning here:
        # print(f"Warning: Unknown style '{style}' provided. Defaulting to 'title'.")
        return string.capwords(processed_text)

# --- Type Aliases for Nested Structure (for clarity) ---
ModuleData = Dict[str, str]         # {'text': str, 'link': str}
SectionData = Dict[str, Any]        # {'name': str, 'link': str, 'modules': List[ModuleData]}
CourseData = Dict[str, Any]         # {'name': str, 'link': str, 'sections': List[SectionData]}
GroupData = Dict[str, Any]          # {'first_file': str, 'courses': Dict[str, CourseData]} # Key is original course name
CatalogStructure = DefaultDict[str, GroupData]

# --- Core Catalog Generation Logic ---

def generate_catalog(base_dir_str: str = BASE_DIR, max_level: int = MAX_LEVEL) -> Optional[str]:
    """
    Generates a multi-level Markdown catalog up to max_level, using nested numbered lists.
    """
    base_path: Path = Path(base_dir_str)
    if not base_path.is_dir():
         print(f"❌ Error: Base directory '{base_path.resolve()}' not found.")
         print(f"ℹ️ Please run this script from the root of your repository.")
         return None

    catalog_data: CatalogStructure = defaultdict(lambda: {'first_file': None, 'courses': {}})

    print(f"🔍 Scanning directory: {base_path.resolve()}")
    md_files = sorted(list(base_path.rglob("*.md")))

    if not md_files:
        print(f"🟡 No markdown files found in '{base_dir_str}'.")
        return "# Courses Catalog 🗺️\n\nNo courses found.\n"

    # --- File Processing Loop ---
    for md_file in md_files:
        relative_file_path: str = md_file.as_posix()
        parent_dir_name: str = md_file.parent.name if md_file.parent != base_path else base_path.name
        group_entry = catalog_data[parent_dir_name]
        if group_entry['first_file'] is None: group_entry['first_file'] = relative_file_path
        current_course_ref: Optional[CourseData] = None
        current_section_ref: Optional[SectionData] = None
        try:
            print(f"   Processing: {relative_file_path}")
            with open(md_file, 'r', encoding='utf-8') as f:
                line_num = 0
                for line_num, line in enumerate(f, 1):
                    heading_info = extract_heading_info(line)
                    if not heading_info: continue
                    level, text = heading_info
                    if level > max_level: continue
                    anchor = generate_anchor(text)
                    link = f"{relative_file_path}#{anchor}"
                    if level == 2:
                        course_name_key = text
                        current_section_ref = None
                        if course_name_key not in group_entry['courses']:
                            group_entry['courses'][course_name_key] = {'name': text, 'link': link, 'sections': []}
                        current_course_ref = group_entry['courses'][course_name_key]
                    elif level == 3 and current_course_ref and max_level >= 3:
                        new_section: SectionData = {'name': text, 'link': link, 'modules': []}
                        current_course_ref['sections'].append(new_section)
                        current_section_ref = new_section
                    elif level == 4 and current_section_ref and max_level >= 4:
                         new_module: ModuleData = {'text': text, 'link': link}
                         current_section_ref['modules'].append(new_module)
                    # Resetting context is tricky, better handled by checking parent ref validity
                    # if level <= 3: current_section_ref = None
                    # if level <= 2: current_course_ref = None
        except Exception as e:
            ln_context = f"(line ~{line_num})" if line_num > 0 else ""
            print(f"  ❌ Error processing file {md_file} {ln_context}: {e}")
            continue

    # --- Markdown Output Generation (Numbered List Format) ---
    output_lines: List[str] = ["# Courses Catalog 🗺️", ""]
    output_lines.append("")
    
    timestamp_str = get_timestamp()
    output_lines.append(f"_Generated: {timestamp_str} | Includes details up to Level H{max_level}_")
    output_lines.append("")

    if not any(group['courses'] for group in catalog_data.values()):
         output_lines.append("No course content (H2/H3/H4 headings) found in markdown files.")
         return "\n".join(output_lines) + "\n"

    # Sort Groups (H1) alphabetically
    for group_name in sorted(catalog_data.keys()):
        group_info = catalog_data[group_name]
        first_file_link = group_info['first_file']
        courses_dict = group_info['courses']

        if not courses_dict: continue

        display_group_name = format_display_name(group_name, style='upper')
        # --- H1: Group Heading ---
        output_lines.append(f"# [{display_group_name}]({first_file_link if first_file_link else ''})")
        output_lines.append("") # Blank line after H1

        # Sort Courses (L2) alphabetically by original name (dict key)
        for course_index, course_name_key in enumerate(sorted(courses_dict.keys()), start=1):
            course_info = courses_dict[course_name_key]
            display_course_name = format_display_name(course_info['name'])
            # --- L2: Course Item (Numbered) ---
            output_lines.append(f"{course_index}. [{display_course_name}]({course_info['link']})")

            if max_level >= 3:
                # Iterate Sections (L3) in natural order
                sections_list = course_info.get('sections', [])
                if isinstance(sections_list, list):
                    for section_index, section_info in enumerate(sections_list, start=1):
                        display_section_name = format_display_name(section_info['name'])
                        # --- L3: Section Item (Indented & Numbered) ---
                        output_lines.append(f"{INDENT_SPACES}{section_index}. [{display_section_name}]({section_info['link']})")

                        if max_level >= 4:
                            # Iterate Modules (L4) in natural order
                            modules_list = section_info.get('modules', [])
                            if isinstance(modules_list, list):
                                for module_index, module_info in enumerate(modules_list, start=1):
                                    display_module_name = format_display_name(module_info['text'])
                                    # --- L4: Module Item (Further Indented & Numbered) ---
                                    output_lines.append(f"{INDENT_SPACES}{INDENT_SPACES}{module_index}. [{display_module_name}]({module_info['link']})")
            # No extra blank line needed between course items for tighter list

        # Removed blank line after group list for tighter output

    return "\n".join(output_lines) + "\n"

# --- Main Execution Block ---
def update_courses_catalog():
    print(f"🚀 Starting course catalog generation (Max Level: {MAX_LEVEL}, List Format)...")
    catalog_markdown = generate_catalog(max_level=MAX_LEVEL)

    if catalog_markdown:
        print(f"\n--- Generated Markdown Catalog Preview (Max Level: {MAX_LEVEL}) ---")
        preview_lines = catalog_markdown.splitlines()
        print("\n".join(preview_lines[:25]))
        if len(preview_lines) > 25:
             print("...")
        print("-----------------------------------------------------------\n")

        output_file_path = Path(OUTPUT_FILENAME)
        try:
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(catalog_markdown)
            print(f"✅ Catalog successfully written to: {output_file_path.resolve()}")
        except Exception as e:
            print(f"❌ Error writing catalog to file {output_file_path}: {e}")
    else:
        print("🔴 Catalog generation failed.")