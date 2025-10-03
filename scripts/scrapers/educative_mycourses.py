from bs4 import BeautifulSoup
import pandas as pd
import re # Import regular expressions module

# --- Configuration for Level Sorting ---
LEVEL_ORDERING = {
    "beginner": "1-beginner",
    "foundational": "1-foundational",
    "intermediate": "2-intermediate",
    "advanced": "3-advanced",
    "expert": "4-expert",
}
DEFAULT_PREFIX_FOR_UNMAPPED_LEVEL = "99-"
PREFIX_FOR_NA_LEVEL = "99-N/A"

def process_duration(duration_str):
    """
    Converts duration string (e.g., '8 h', '1 h 30 min', '45 min')
    to a numerical value in hours (float).
    """
    if not duration_str or duration_str.strip().lower() == 'n/a':
        return None

    total_hours = 0.0
    processed_string = duration_str.lower() # Work with lowercase

    # Regex to find hours (allows for decimals in hours, e.g., "1.5 h")
    # Looks for a number followed by h, hr, hour, or hours
    hour_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:h|hr|hour|hours)', processed_string)
    if hour_match:
        try:
            total_hours += float(hour_match.group(1))
            # Remove the matched part to avoid re-processing if minutes are also just a number
            processed_string = processed_string.replace(hour_match.group(0), "").strip()
        except ValueError:
            pass # Could not convert, proceed to check minutes or other formats

    # Regex to find minutes
    # Looks for a number followed by m, min, minute, or minutes
    minute_match = re.search(r'(\d+)\s*(?:m|min|minute|minutes)', processed_string)
    if minute_match:
        try:
            total_hours += float(minute_match.group(1)) / 60.0
            processed_string = processed_string.replace(minute_match.group(0), "").strip()
        except ValueError:
            pass

    # If after processing h/min, the remaining string is just a number,
    # and no hours/minutes were explicitly found yet, assume it's hours.
    # This also handles the case where the input is *just* a number like "8".
    if total_hours == 0 and processed_string:
        # Check if the original string (or what's left of it) is just a number
        plain_number_match = re.fullmatch(r'(\d+(?:\.\d+)?)', processed_string)
        if plain_number_match:
            try:
                return float(plain_number_match.group(1))
            except ValueError:
                return None # Should not happen with this regex but good for safety

    return total_hours if total_hours > 0 else None


def process_level(level_str):
    """Converts level string to a sortable prefixed string."""
    if not level_str or level_str.strip().lower() == 'n/a':
        return PREFIX_FOR_NA_LEVEL

    level_lower = level_str.lower().strip()
    if level_lower in LEVEL_ORDERING:
        return LEVEL_ORDERING[level_lower]
    else:
        return f"{DEFAULT_PREFIX_FOR_UNMAPPED_LEVEL}{level_lower}"

# Read HTML from file
try:
    with open('content.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    print("Error: 'some.html' not found. Please make sure the file exists in the same directory as the script.")
    exit()

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all course cards
course_cards = soup.find_all('div', class_='CourseTile_tile__2MxhG')

# Lists to store extracted data
course_names = []
original_durations = []
processed_durations = []
processed_levels = []

# Extract data from each card
for card in course_cards:
    # Course Name
    name_tag = card.find('p', class_='CourseTile_desktopTitle__BfqOj')
    course_names.append(name_tag.text.strip() if name_tag else 'N/A')

    # Course Duration
    duration_text_original = 'N/A'
    duration_tag_container = card.find('div', class_='CourseTile_completionTime__nyGKm')
    if duration_tag_container:
        duration_div = duration_tag_container.find('div')
        if duration_div:
            duration_text_original = duration_div.text.strip()
    original_durations.append(duration_text_original)
    processed_durations.append(process_duration(duration_text_original))

    # Course Level
    level_text = 'N/A'
    level_tag = card.find('p', class_='CourseTile_targetAudience__J4bDQ')
    if level_tag:
        level_text = level_tag.text.strip()
    processed_levels.append(process_level(level_text))

# Create DataFrame
df = pd.DataFrame({
    'Course Name': course_names,
    'Original Duration': original_durations,
    'Duration (Hours)': processed_durations,
    'Level': processed_levels
})

# Save to Excel
try:
    # Using the same filename as the previous version that included original duration
    df.to_excel('courses_processed_with_original_duration.xlsx', index=False)
    print("Successfully extracted and processed courses to courses_processed_with_original_duration.xlsx")
except Exception as e:
    print(f"Error saving to Excel: {e}")