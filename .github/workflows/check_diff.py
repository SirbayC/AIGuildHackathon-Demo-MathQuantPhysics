import sys

def analyze_diff(diff_file_path):
    # Open and read the diff file
    with open(diff_file_path, 'r') as file:
        diff_content = file.read()

    print("--- SUCCESSFULLY LOADED DIFF INTO PYTHON ---")
    print(f"Diff length: {len(diff_content)} characters")
    
    # POC: Just print the first 15 lines of the diff to prove we have it
    lines = diff_content.split('\n')
    for line in lines:
        print(line)
        
    print("--------------------------------------------")
    
    # Here is where you will eventually add your logic to score the accessibility!

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_diff.py <path_to_diff_file>")
        sys.exit(1)
        
    diff_path = sys.argv[1]
    analyze_diff(diff_path)