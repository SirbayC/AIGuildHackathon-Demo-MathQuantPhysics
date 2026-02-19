from __future__ import annotations

import json

import streamlit as st

from reviewer import build_professor_report, review_markdown_accessibility

DEFAULT_MODEL = "gpt-4o-mini"


st.set_page_config(page_title="Accessibility Review Agent", layout="wide")

st.title("Accessibility Review Agent")
st.write(
    "Upload a Markdown document and optionally a rules file. "
    "The agent reviews accessibility issues with context-aware reasoning and returns a professor-friendly report."
)

col1, col2 = st.columns(2)
with col1:
    markdown_file = st.file_uploader("Markdown file (.md)", type=["md"], accept_multiple_files=False)
with col2:
    rules_file = st.file_uploader(
        "Optional rules file (.md or .txt)", type=["md", "txt"], accept_multiple_files=False
    )

model_name = st.text_input("Model", value=DEFAULT_MODEL)
temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.1)

if st.button("Review Accessibility", type="primary"):
    if markdown_file is None:
        st.error("Please upload a Markdown file.")
    else:
        markdown_text = markdown_file.getvalue().decode("utf-8", errors="replace")
        rules_text = None
        if rules_file is not None:
            rules_text = rules_file.getvalue().decode("utf-8", errors="replace")

        try:
            with st.spinner("Running accessibility review..."):
                result = review_markdown_accessibility(
                    markdown_text=markdown_text,
                    rules_text=rules_text,
                    model=model_name.strip() or DEFAULT_MODEL,
                    temperature=temperature,
                )
                report_text = build_professor_report(result)

            st.subheader("Professor Report")
            st.markdown(report_text)

            st.subheader("Score")
            st.metric("Accessibility Score", result.score)

            st.subheader("Summary")
            for bullet in result.summary_bullets:
                st.write(f"- {bullet}")

            st.subheader("Issues")
            if result.issues:
                issue_rows = [
                    {
                        "id": issue.id,
                        "severity": issue.severity,
                        "title": issue.title,
                    }
                    for issue in result.issues
                ]
                st.dataframe(issue_rows, use_container_width=True)

                for issue in result.issues:
                    with st.expander(f"{issue.id} | {issue.severity.upper()} | {issue.title}"):
                        st.write(f"**Explanation:** {issue.explanation}")
                        st.write(f"**Evidence:** {issue.evidence}")
                        st.write(f"**Suggestion:** {issue.suggestion}")
            else:
                st.info("No issues reported.")

            st.subheader("Score Breakdown")
            st.write(f"- Base: {result.score_breakdown.base}")
            for item in result.score_breakdown.penalties:
                st.write(
                    f"- {item.severity.title()}: {item.count} x {item.penalty_per_item} = -{item.subtotal}"
                )
            st.write(f"- Final: {result.score_breakdown.final}")

            if result.applied_rules:
                st.subheader("Applied Rules")
                st.write(result.applied_rules)

            output_json = json.dumps(result.model_dump(), indent=2)
            st.download_button(
                label="Download Report (.md)",
                data=report_text,
                file_name="accessibility_review_report.md",
                mime="text/markdown",
            )
            st.download_button(
                label="Download JSON (Optional)",
                data=output_json,
                file_name="accessibility_review.json",
                mime="application/json",
            )
            with st.expander("Technical JSON (Optional)"):
                st.code(output_json, language="json")

        except Exception as exc:
            st.error(f"Review failed: {exc}")
