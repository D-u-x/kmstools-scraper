# 🛠️ KMS Tools Product Scraper

This is a Python script that scrapes product data from the Canadian website [kmstools.com](https://www.kmstools.com/hand-tools), specifically from the "Hand Tools" category.

The script uses the site's public **Searchspring API** to collect structured product information and saves it to both **CSV** and **JSONL** formats.

---

## ✅ Features

- Automatically scrapes **all pages** of the category
- Extracts key product information:
  - 🏷️ Product name  
  - 💲 Price  
  - 🆔 SKU (item code)  
  - ✅ Stock availability  
  - 🔗 Product URL  
  - 🖼️ Image URL  
- Saves data in:
  - `kmstools_data.csv` — standard spreadsheet format
  - `kmstools_data.jsonl` — newline-delimited JSON for advanced data processing
- Adds a **1-second delay** between requests to avoid server overload
- Tolerates request failures — previous pages are saved incrementally

---

## 📦 Technologies Used

- **Python 3.x**
- `requests` — for HTTP requests
- `csv` and `json` — for data export
- `time` — to pause between requests

> ⚠️ No third-party libraries are required — it's built entirely with Python's standard library.

---

## 🚀 How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/kmstools-scraper.git
   cd kmstools-scraper
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Run the script**:
   ```bash
   python main.py
   ```

4. **Check the output**:
   - `kmstools_data.csv` — tabular product data
   - `kmstools_data.jsonl` — newline-delimited JSON records

### 📂 Example Output

> Sample CSV structure:

| name                | price | item_code | in_stock | url                                     | image_url            |
|---------------------|-------|-----------|----------|------------------------------------------|-----------------------|
| Milwaukee Hammer    | 29.99 | MILW-1234 | True     | https://www.kmstools.com/...             | https://...jpg        |
| Stanley Screwdriver | 9.49  | STAN-5678 | False    | https://www.kmstools.com/...             | https://...jpg        |

> Sample JSONL entry:
```json
{
  "name": "Milwaukee Hammer",
  "price": "29.99",
  "item_code": "MILW-1234",
  "in_stock": true,
  "url": "https://www.kmstools.com/milwaukee-hammer",
  "image_url": "https://cdn.kmstools.com/images/milw-1234.jpg"
}
```

---

## 📄 License

This project is provided for educational and personal portfolio purposes.  
Always respect a website's terms of service before scraping any data.

---

## 👨‍💻 Author

**Vladyslav Prokopiv**  
Python Developer | Data Automation Enthusiast  
🇺🇦 Based in Canada
