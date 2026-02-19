def generate_markdown_report(changes:dict[list[str]]) -> str:
    output_file = "report.md"

    report_lines = ["Test line"]

    for file, lines in changes.items():
        # 'lines' is the list of strings for this specific file
        for line in lines:
            # Now 'line' is a single string
            report_lines.append(f"**{file}**: {line}")

    # Write the report to the file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        
    return output_file