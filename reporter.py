def generate_markdown_report(changes:dict[str, str]) -> str:
    output_file = "report.md"

    report_lines = ["Test line"]

    for file, change in changes.items():
        # 'lines' is the list of strings for this specific file
        report_lines.append("\nNEW CHANGE\n")
        report_lines.append(file)
        report_lines.append(change)

    # Write the report to the file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        
    return output_file