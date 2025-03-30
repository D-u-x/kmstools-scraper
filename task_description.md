# 📋 Project Description — KMS Tools Scraper

## 🎯 Objective

The goal of this project is to build a Python-based web scraper that collects product data from the "Hand Tools" category on the Canadian website [kmstools.com](https://www.kmstools.com/hand-tools).  
The scraper must be reliable, modular, and suitable for use in a freelance/portfolio context.

---

## 🛠️ Task Requirements

### ✅ Functional Requirements

- Connect to the public **Searchspring API** used by the website.
- Collect the following fields for each product:
  - Name
  - Price
  - SKU (item code)
  - Stock availability
  - Product URL
  - Image URL
- Handle **pagination** and retrieve all available products.
- Respect server load using delay (`time.sleep`).
- Write the results to:
  - `kmstools_data.csv` — for spreadsheet-friendly format
  - `kmstools_data.jsonl` — for structured, line-by-line JSON export

---

## 🔒 Error Handling

- If a page fails to load, continue with the next one.
- Data from previous pages must still be preserved.
- Ensure the script doesn't break mid-way and can be re-run.

---

## 🧱 Technical Constraints

- Use **only Python standard libraries**:
  - `requests`, `csv`, `json`, `time`
- No third-party packages allowed (e.g., no `pandas`, `scrapy`, etc.)
- Code must be modular, readable, and extensible

---

## 📂 Deliverables

- `main.py` — working and clean script
- `README.md` — project overview and usage instructions
- `task_description.md` — this task definition
- `.gitignore` — excludes local, cache, and output files

---

## 🧑‍💻 Author

Vladyslav Prokopiv  
Python Developer | Data Automation Enthusiast  
🇺🇦 Based in Canada
