def generate_markdown_report(changes:dict[list[str]]) -> str:
    output_file = "report.md"

    report_lines = ["Test line"]

    for file,line in changes.items():
        report_lines.append(file + " ## " + line)

    # Write the report to the file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        
    return output_file