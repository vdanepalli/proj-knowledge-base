# -*- coding: utf-8 -*-
import csv
import os
import re
import unicodedata
from pathlib import Path
from collections import defaultdict

# --- Configuration ---

CSV_FILENAME = "courses/courses.csv"
OUTPUT_FILENAME = "courses.md"
ROOT_DIR = Path.cwd()
COURSES_SUBDIR = "courses"


MAIN_TITLE = "🧭 The Knowledge Compass"
TOC_TITLE = "📍 Waypoints"

# --- Helper Functions ---

def generate_anchor(text):
    """Generates a GitHub-style Markdown anchor from heading text."""
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    try:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    except TypeError:
        pass
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    # text = text.strip('-')
    if not text:
        return "section"
    return text

def build_heading_hierarchy(filepath: Path):
    """Builds hierarchical structure from Markdown headings."""
    hierarchy = []
    node_stack = []
    anchors_in_file = defaultdict(int)
    in_code_block = False
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content_lines = f.readlines()
    except Exception as e:
        print(f"  [Warning] Error reading {filepath}: {e}")
        return []
    for line_num, line in enumerate(content_lines):
        stripped_line_for_fence_check = line.strip()
        if stripped_line_for_fence_check.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        match = re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            level = len(match.group(1))
            raw_text = match.group(2).rstrip()
            link_match = re.match(r'^\[([^\]]+)\]\(.*\)$', raw_text.strip())
            if link_match:
                display_text = link_match.group(1).strip()
            else:
                display_text = raw_text
            base_anchor = generate_anchor(raw_text)
            anchors_in_file[base_anchor] += 1
            count = anchors_in_file[base_anchor]
            anchor = f"{base_anchor}-{count-1}" if count > 1 else base_anchor
            node = {'level': level, 'text': display_text, 'anchor': anchor, 'children': []}
            while node_stack and node_stack[-1]['level'] >= level:
                node_stack.pop()
            if not node_stack:
                hierarchy.append(node)
            else:
                node_stack[-1]['children'].append(node)
            node_stack.append(node)
    return hierarchy

# --- Markdown Generation Function ---

def generate_markdown_output(courses, root_dir, courses_subdir):
    """Generates the list of lines for the output MD file with correct linking."""
    
    main_title_anchor = generate_anchor(MAIN_TITLE) # Not used in current output, but generated
    toc_anchor_target_name = generate_anchor(TOC_TITLE) # Used for H2 number links
    
    output_lines = [f"# {MAIN_TITLE}\n"]
    courses_base_path = root_dir / courses_subdir

    # --- Pre-calculate data for TOC ---
    toc_data = []
    print("\n--- Preparing TOC Data ---")
    for course_index, course in enumerate(courses):
        course_name = course.get('course_name', '').strip()
        course_description = course.get('course_description', '').strip()
        if not course_name or not course_description: continue
        course_dir = courses_base_path / course_name
        num_files = 0; file_plural = "files"
        if course_dir.is_dir():
            try:
                md_files_list = [f for f in course_dir.iterdir() if f.is_file() and f.suffix.lower() == '.md']
                num_files = len(md_files_list)
                file_plural = "file" if num_files == 1 else "files"
            except Exception as e:
                print(f"  [Warning] Could not read directory {course_dir} for file count: {e}")
                num_files = 0; file_plural = "files"
        # Construct the exact heading text including count (if > 0) for anchor generation
        full_heading_text_h2 = course_description
        if num_files > 0: full_heading_text_h2 += f" ({num_files} {file_plural})"
        heading_anchor_h2 = generate_anchor(full_heading_text_h2) # Anchor for H2 heading

        toc_data.append({'description': course_description, 'anchor': heading_anchor_h2})
        print(f"  Desc='{course_description}', Full='{full_heading_text_h2}', Anchor='{heading_anchor_h2}'")
    print("--- TOC Data Prepared ---\n")

    # --- Generate TOC ---
    output_lines.append(f"## {TOC_TITLE}\n")
    for item in toc_data:
        output_lines.append(f"- [{item['description']}](#{item['anchor']})\n")
    output_lines.append("<br/>\n") # Space after TOC

    # --- Generate Course Content ---
    for course_index, course in enumerate(courses):
        course_name = course.get('course_name', '').strip()
        course_description = course.get('course_description', '').strip()
        if not course_name or not course_description: continue

        # Get the pre-calculated anchor for this course H2 heading (target for H3 number links)
        course_anchor_target_for_h3_link = f"#{toc_data[course_index]['anchor']}" # Use '#' prefix now

        course_dir = courses_base_path / course_name
        print(f"\n- Processing: {course_description} (folder: {courses_subdir}/{course_name})")

        # --- Course Heading (H2) ---
        num_files = 0; md_files = []
        if course_dir.is_dir():
             try:
                 md_files = sorted([f for f in course_dir.iterdir() if f.is_file() and f.suffix.lower() == '.md'])
                 num_files = len(md_files)
             except Exception as e: print(f"  [Warning] Could not read directory {course_dir} for file list: {e}"); num_files = 0; md_files = []
        file_plural = "file" if num_files == 1 else "files"
        heading_text_h2 = course_description
        if num_files > 0: heading_text_h2 += f" ({num_files} {file_plural})"
        # Output H2 heading text - Anchor is implicitly generated by Markdown processor
        output_lines.append(f"## [{heading_text_h2}](#{toc_anchor_target_name})\n")

        if not course_dir.is_dir():
             output_lines.append(f"*Directory <code>{courses_subdir}/{course_name}</code> not found.*\n")
             output_lines.append("<br/>\n")
             continue
        if not md_files:
            output_lines.append("<br/>\n")
            continue

        # --- Process Files ---
        for file_index, md_file_path in enumerate(md_files):
            file_number = file_index + 1
            print(f"  - Parsing {file_number}. {md_file_path.name}")
            hierarchy = build_heading_hierarchy(md_file_path)
            relative_file_path = md_file_path.relative_to(root_dir).as_posix()
            h1_nodes = [node for node in hierarchy if node['level'] == 1]

            # --- File Heading (H3) ---
            h1_link_target = relative_file_path # Default link target if no H1
            full_h3_heading_text_for_anchor = f"{file_number}. {md_file_path.name} (No H1 Found)" # Fallback text for anchor gen

            if not h1_nodes:
                print(f"    [Warning] No H1 heading found in {md_file_path.name}.")
                link_num_to_h2 = course_anchor_target_for_h3_link # Link number to parent H2
                output_lines.append(f"### [{file_number}.]({link_num_to_h2}) [{md_file_path.name}]({h1_link_target}) (No H1 Found)\n")
            else:
                h1_node = h1_nodes[0]
                if len(h1_nodes) > 1: print(f"    [Warning] Multiple H1 headings found. Using first.")
                num_h2s = sum(1 for node in h1_node['children'] if node['level'] == 2)
                h2_plural = "section" if num_h2s == 1 else "sections"
                h1_link_target = f"{relative_file_path}#{h1_node['anchor']}" # Link for title part
                h1_display_text = h1_node['text']
                if num_h2s > 0: h1_display_text += f" ({num_h2s} {h2_plural})"

                # --- Construct FULL H3 text and generate anchor for linking from H4 ---
                full_h3_heading_text_for_anchor = f"{file_number}. {h1_display_text}"
                # --------------------------------------------------------------------

                link_num_to_h2 = course_anchor_target_for_h3_link # Link number to parent H2 anchor
                output_lines.append(f"### [{file_number}.]({link_num_to_h2}) [{h1_display_text}]({h1_link_target})\n")

            # --- Generate the anchor for this H3 heading (needed by child H4s) ---
            parent_h3_anchor_target_for_h4_link = f"#{generate_anchor(full_h3_heading_text_for_anchor)}"
            # --------------------------------------------------------------------

            # --- Process H2+ hierarchy within the file ---
            if h1_nodes: # Only process children if H1 exists
                h2_nodes = [node for node in h1_node['children'] if node['level'] == 2]

                # --- H2 Heading (H4) ---
                for h2_index, h2_node in enumerate(h2_nodes):
                    h2_number_nested = f"{file_number}.{h2_index + 1}"
                    num_h3s = sum(1 for node in h2_node['children'] if node['level'] == 3)
                    h3_plural = "module" if num_h3s == 1 else "modules"
                    h2_link_target = f"{relative_file_path}#{h2_node['anchor']}" # Link for title part
                    h2_display_text = h2_node['text']
                    if num_h3s > 0: h2_display_text += f" ({num_h3s} {h3_plural})"

                    # Format H4: Link number prefix to parent H3 anchor, Link title+count to H2 anchor in file
                    link_num_to_h3 = parent_h3_anchor_target_for_h4_link # Use anchor of the actual H3 heading
                    output_lines.append(f"#### [{h2_number_nested}]({link_num_to_h3}) [{h2_display_text}]({h2_link_target})\n") # Dual linking for H4

                    h3_nodes = [node for node in h2_node['children'] if node['level'] == 3]

                    # --- H3 Numbered List Item ---
                    if h3_nodes:
                        for h3_list_index, h3_node in enumerate(h3_nodes):
                            num_h4plus = sum(1 for node in h3_node['children'] if node['level'] >= 4)
                            h4_plural = "lesson" if num_h4plus == 1 else "lessons"
                            h3_link = f"{relative_file_path}#{h3_node['anchor']}"
                            h3_display_text = h3_node['text']
                            if num_h4plus > 0: h3_display_text += f" ({num_h4plus} {h4_plural})"
                            output_lines.append(f"{h3_list_index + 1}. [{h3_display_text}]({h3_link})\n")

                            h4plus_nodes = [node for node in h3_node['children'] if node['level'] >= 4]
                            # --- H4+ Nested Numbered List ---
                            if h4plus_nodes:
                                for h4plus_list_index, h4plus_node in enumerate(h4plus_nodes):
                                    h4plus_link = f"{relative_file_path}#{h4plus_node['anchor']}"
                                    output_lines.append(f"    {h4plus_list_index + 1}. [{h4plus_node['text']}]({h4plus_link})\n")
                        output_lines.append("") # Blank line after H3 list

                    # Add space after H4 block if not last H2
                    if h2_index < len(h2_nodes) - 1:
                         output_lines.append("<br/>\n")

            # Add space after file block
            output_lines.append("<br/><br/><br>\n")

    # --- Final Cleanup ---
    while output_lines and (output_lines[-1] == "" or output_lines[-1].strip() == "<br/>"):
         output_lines.pop()
    if output_lines:
        output_lines.append("")

    return output_lines

# --- Main Execution ---
def main():
    print(f"Generating {OUTPUT_FILENAME} with corrected linking...")
    print(f"Looking for course folders inside '{COURSES_SUBDIR}/'")
    # --- Read Course Data ---
    csv_filepath = ROOT_DIR / CSV_FILENAME
    courses = []
    try:
        with open(csv_filepath, mode='r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or not all(col in reader.fieldnames for col in ['course_name', 'course_description']):
                 print(f"[Error] CSV file '{csv_filepath.name}' must contain 'course_name' and 'course_description' columns.")
                 return
            courses = list(reader)
        courses.sort(key=lambda x: x.get('course_description', ''))
        print(f"- Read {len(courses)} courses from '{csv_filepath.name}'.")
    except FileNotFoundError:
        print(f"[Error] CSV file not found: {csv_filepath}")
        return
    except Exception as e:
        print(f"[Error] Failed to read or parse CSV file '{csv_filepath.name}': {e}")
        return
    # --- Generate Markdown Output Lines ---
    output_lines = generate_markdown_output(courses, ROOT_DIR, COURSES_SUBDIR)
    # --- Write Output File ---
    output_file_path = ROOT_DIR / OUTPUT_FILENAME
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(output_lines))
        print(f"\nSuccessfully generated {output_file_path}")
    except Exception as e:
        print(f"\n[Error] Failed writing {output_file_path}: {e}")

if __name__ == "__main__":
    main()