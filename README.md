# internal-skills

Skills for Revenueholic's AI work.

## Install

### Mac / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/Mahesh-Revenueholic/internal-skills/main/install.sh | bash
```

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/Mahesh-Revenueholic/internal-skills/main/install.ps1 | iex
```

### Manual

```bash
git clone --depth 1 https://github.com/Mahesh-Revenueholic/internal-skills.git
cp internal-skills/*.md ~/.ai-skills/
```

## Use

The pipeline will get you a SEO / GEO / AEO friendly blog article. Paste this in your AI tool

```
Run the SEO blog pipeline

```
IF you cannot install this skill locally, run this

```
run seo-blog-pipeline.md from https://github.com/Mahesh-Revenueholic/internal-skills
 
### Step 1: Get the file listing
Scrape the repo root URL:
  https://github.com/{owner}/{repo}
The response contains a JSON payload. Find the `tree.items` array ,  
each item has `name`, `path`, and `contentType`. Collect all file paths.
 
### Step 2: Load each file
For each file from Step 1, scrape the blob URL:
  https://github.com/{owner}/{repo}/blob/main/{file_path}
The response contains the full file content in the rendered markdown 
and raw lines array.
 
### What does NOT work (do not attempt):
- raw.githubusercontent.com URLs → returns empty
- api.github.com URLs → returns empty
- search_and_scrape with site:github.com queries → returns empty
- Only github.com/{owner}/{repo} and github.com/{owner}/{repo}/blob/{branch}/{path} work reliably.
```


Provide:
- Client name
- Client website
- Primary keyword
- B2B or B2C

Everything else is auto-resolved.

- **AI Hygiene & Filtering:** Utilizing the `/fuck-slop` tool created by [JuliusBrussee](https://github.com/JuliusBrussee/skills) to maintain clean, human-centric repositories.

