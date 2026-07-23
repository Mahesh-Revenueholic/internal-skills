
## To Install

```mermaid
%% Install flow - simple, no loops
flowchart LR
  A["curl install.sh | bash"] --> B["Clone repo"]
  B --> C["Copy .md + .py files"]
  C --> D["Report what loaded"]
  D --> E["Paste: Run the SEO blog pipeline"]
```

**Mac/Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/Mahesh-Revenueholic/internal-skills/main/install.sh | bash
```

**Windows:**
```powershell
irm https://raw.githubusercontent.com/Mahesh-Revenueholic/internal-skills/main/install.ps1 | iex
```

**Then in your AI tool:** *"Run the SEO blog pipeline."*
---
