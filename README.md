# 🤖 Accessibility Bot POC

An automated accessibility reviewer for [TU Delft interactive textbook PRs](https://books.open.tudelft.nl/home/catalog/category/interactive-textbooks). This bot uses LLMs to analyze Pull Request diffs and provide actionable feedback on accessibility standards.

Created as part of [TU Delft First AI Guild Hackathon “AI-in-Practice"](https://www.eventbrite.com/e/tu-delft-first-ai-guild-hackathon-ai-in-practice-tickets-1981860882249), winning first place. 

Team members:
- [Cosmin Andrei Vasilescu](https://github.com/SirbayC)

Example usage is available in [PR](https://github.com/SirbayC/AIGuildHackathon-Demo-MathQuantPhysics/pull/8).

---

## 🚀 Features
* **Diff-Aware:** Only analyzes new or modified lines in `.md` files to keep CI runs fast.
* **AI-Powered:** Detects nuanced issues like missing alt text, skipped header levels, and poor link descriptions using OpenAI.
* **Automated Feedback:** Posts a detailed report directly as a comment on the Pull Request.
* **Scoring System:** Provides an accessibility score (0-100) based on severity-based penalties.

---

## 🛠️ How it Works

The bot follows a 4-step pipeline whenever a Pull Request is managed:

1. **Trigger:** A developer opens or updates a Pull Request.
2. **Diff Parsing:** A Python script (`check_diff.py`) extracts the "added" lines from the PR diff via the GitHub CLI.
3. **AI Analysis:** The `reviewer.py` module sends the content to OpenAI (GPT-4o-mini) for a structured review.
4. **Reporting:** `bot_reporter.py` generates a `report.md`, which is then posted back to the PR as a comment.


The entire code is contained in `./github` and `a11y_bot`.

---

## ⚙️ Setup

### 1. Repository Secrets
To use this bot, you must add your OpenAI API key to your GitHub repository:
1.  Navigate to your repository on GitHub.
2.  Go to **Settings > Secrets and variables > Actions**.
3.  Click **New repository secret**.
4.  **Name:** `OPENAI_API_KEY`
5.  **Secret:** `your_actual_openai_api_key`

### 2. Workflow Permissions
The bot requires permission to write comments to your Pull Requests. This is already configured in the `.github/workflows/accessibility-bot.yml` via:
```yaml
permissions:
  pull-requests: write
  contents: read
