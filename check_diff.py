import sys
import re

def parse_diff(diff_content):
    """Parses a unified diff and returns a dictionary of added lines per file with line numbers."""
    changed_files = {}
    current_file = None
    current_line_number = None
    lines = diff_content.split('\n')
    
    for line in lines:

        # Detect which file we are currently looking at
        if line.startswith('+++ b/'):
            current_file = line.replace('+++ b/', '')
            # We only care about markdown files for accessibility checks
            if current_file.endswith('.md'):
                changed_files[current_file] = []
            else:
                current_file = None # Ignore non-markdown files
        
        # Parse the @@ line to get starting line numbers
        elif current_file and line.startswith('@@'):
            # Extract line numbers from @@ -start,count +start,count @@
            match = re.search(r'\+(\d+)', line)
            if match:
                current_line_number = int(match.group(1))
            
        # If we are inside a markdown file and the line was ADDED
        elif current_file and line.startswith('+') and not line.startswith('+++'):
            # Remove the leading '+' to get the actual content
            actual_content = line[1:]
            changed_files[current_file].append({
                'line_number': current_line_number,
                'content': actual_content
            })
            current_line_number += 1
        
        # Track line numbers for context lines (unchanged lines)
        elif current_file and current_line_number is not None:
            if line.startswith('-') and not line.startswith('---'):
                # Deleted line, don't increment
                pass
            elif line and not line.startswith('+') and not line.startswith('-') and not line.startswith('\\'):
                # Context line (unchanged), increment line number
                current_line_number += 1

    return changed_files

def analyze_diff(diff_file_path):
    with open(diff_file_path, 'r', encoding='utf-8') as file:
        diff_content = file.read()

    # Parse the diff
    parsed_changes = parse_diff(diff_content)
    
    # Print the results
    print("--- PARSED DIFF RESULTS ---")
    for filename, added_lines in parsed_changes.items():
        print(f"\nFile: {filename}")
        print(f"Total new lines added: {len(added_lines)}")
        
        # Now we can run our accessibility checks on these specific lines!
        for item in added_lines:
            line_num = item['line_number']
            content = item['content']
            print(f"  Line {line_num}: {content}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_diff.py <path_to_diff_file>")
        sys.exit(1)
        
    diff_path = sys.argv[1]
    analyze_diff(diff_path)