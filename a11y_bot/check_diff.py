import sys

from a11y_bot.bot_reporter import generate_accessibility_pr_report

def parse_diff(diff_content):
    """Parses a unified diff and returns a dictionary of added lines per file."""
    changed_files = {}
    current_file = None
    lines = diff_content.split('\n')
    
    for line in lines:

        # Detect which file we are currently looking at
        if line.startswith('+++ b/'):
            current_file = line.replace('+++ b/', '')
            # We only care about markdown files for accessibility checks
            if current_file.endswith('.md'):
                changed_files[current_file] = ""
            else:
                current_file = None # Ignore non-markdown files
                
        # If we are inside a markdown file and the line was ADDED
        elif current_file and line.startswith('+') and not line.startswith('+++'):
            # Remove the leading '+' to get the actual content
            actual_content = line[1:]

            if actual_content.strip(): 
                changed_files[current_file] = changed_files[current_file] + "\n" + actual_content

    return changed_files

def analyze_diff(diff_file_path):
    with open(diff_file_path, 'r', encoding='utf-8') as file:
        diff_content = file.read()

    parsed_changes = parse_diff(diff_content)

    print("--- Calling analyzer ---")
    generate_accessibility_pr_report(parsed_changes)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_diff.py <path_to_diff_file>")
        sys.exit(1)
        
    diff_path = sys.argv[1]
    analyze_diff(diff_path)