# GitHub Repository Configuration for IA-PME Suite

## Pour votre fichier .gitignore:

```
# Dependencies
node_modules/
package-lock.json
yarn.lock

# Local development
.env.local
.env.*.local

# Editor
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*

# Build output (if using a build tool)
dist/
build/

# IDE
.idea/
.vscode/

# Keep the landing page files
!index.html
!style.css
```

---

## Pour votre .gitattributes:

```
# Auto detect text files and normalize line endings to LF
* text=auto

# HTML and CSS
*.html text eol=lf
*.css text eol=lf
*.js text eol=lf

# Markdown
*.md text eol=lf

# Documents
*.pdf binary
*.doc binary
*.docx binary
```

---

## Pour votre .github/dependabot.yml:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    allow:
      - dependency-type: "direct"
```

---

## Pour votre .github/pull_request_template.md:

```markdown
# Pull Request

## ⚠️ STOP

This is a **proprietary repository**. 

Pull requests are **NOT accepted**.

If you would like to contribute or have suggestions, please:

📧 **Email:** rudy@ia-pme.fr

---

## What You Cannot Do

- Fork this repository for commercial use
- Modify and reuse code
- Create competing products
- Submit pull requests

## What You Can Do

- Report security issues privately to: security@ia-pme.fr
- Contact for commercial licensing: rudy@ia-pme.fr
- Share the landing page URL
- Learn about our solution

---

Thank you for understanding.

**© 2025 IA-PME - Proprietary**
```

---

## Pour votre .github/issue_template/bug_report.md:

```markdown
---
name: Security Issue Report
about: Report a security vulnerability
title: "[SECURITY]"
labels: security
assignees: 'willoquetr'

---

## ⚠️ SECURITY ISSUE

Do not describe the vulnerability in detail in this form.

Instead, email: **security@ia-pme.fr**

We will respond within 24 hours.

---

**Please DO NOT:**
- Include exploit code
- Post details publicly
- Fork the repository to test
- Open public issues

Thank you for responsibly reporting security issues.
```

---

## Pour votre .github/issue_template/feature_request.md:

```markdown
---
name: Feature Request
about: Suggest a feature for IA-PME
title: "Feature Request: "
labels: enhancement
assignees: 'willoquetr'

---

## Feature Request

### Do You Have a Commercial License?

This repository is proprietary. Feature requests are for **licensed customers only**.

❓ **Are you a licensed customer?**
- [ ] Yes - I have a commercial license
- [ ] No - I'm interested in licensing

If "No", please contact: **rudy@ia-pme.fr**

---

### Your Feature Request

**Description:**


**Rationale:**


**Expected Outcome:**


---

Thank you!
```
