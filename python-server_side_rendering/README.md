# 📁 Flask Server-Side Rendering — Tasks 0 to 4

This project showcases a set of server-side rendering tasks using Flask and Jinja2. It includes basic templating, reusable HTML components, conditional rendering, data fetching from JSON/CSV files, and database interaction with SQLite.

## ✅ Task Overview

### Task 0: Simple Template Rendering
**File:** `task_00_intro.py`

- Implements a function `generate_invitations(template, attendees)` that:
  - Replaces placeholders (`{name}`, `{event_title}`, etc.) in a template string.
  - Outputs personalized text files (e.g. `output_1.txt`) for each attendee.
  - Handles edge cases like empty inputs, invalid types, and missing data.

➡️ Example usage:
```python
generate_invitations(template_content, attendees)
```

---

### Task 1: Basic HTML Template with Flask
**File:** `task_01_jinja.py`

- Serves an HTML page using Flask and Jinja2.
- Adds three routes:
  - `/` (index)
  - `/about`
  - `/contact`
- Uses `header.html` and `footer.html` as reusable components included in all pages.

➡️ Folder structure:
```
templates/
├── index.html
├── about.html
├── contact.html
├── header.html
└── footer.html
```

---

### Task 2: Conditional Rendering in Templates
**File:** `task_02_logic.py`

- Displays a list of items dynamically using Jinja2.
- If the list is empty, it shows a fallback message like `"No items found."`
- URL: `/items`

➡️ Example logic in template:
```jinja
{% if items %}
  <ul>{% for item in items %}<li>{{ item }}</li>{% endfor %}</ul>
{% else %}
  <p>No items found.</p>
{% endif %}
```

---

### Task 3: Displaying Data from JSON or CSV
**File:** `task_03_files.py`

- Route: `/products`
- Accepts two query parameters:
  - `source`: `json` or `csv`
  - `id` (optional): filter a product by its ID
- Displays products in an HTML table using a shared template (`product_display.html`)
- Handles edge cases:
  - Invalid source → “Wrong source”
  - Invalid/missing ID → “Product not found”

➡️ Example URLs:
```
/products?source=json
/products?source=csv&id=1
/products?source=xml         → error
```

➡️ Data files:
- `products.json`
- `products.csv`

---

### Task 4: Extending to SQLite
**File:** `task_04_db.py`

- Adds SQLite support (`source=sql`) to `/products` route.
- Uses the same template as Task 3.
- Database: `products.db` with a `Products` table.
- Includes a setup script: `create_db.py`

➡️ Run once to create DB:
```bash
python3 create_db.py
```

➡️ Example URLs:
```
/products?source=sql
/products?source=sql&id=2
/products?source=sql&id=99   → Product not found
```

---

## 🧪 How to Run

```bash
pip install Flask
python3 task_XX_xxx.py   # Replace XX with the task number
```

Visit `http://localhost:5000` in your browser and navigate the routes depending on the task.

---

## 💡 Features Summary

- ✅ Dynamic rendering with Jinja2
- ✅ Reusable templates (header/footer)
- ✅ Query parameter handling
- ✅ Conditional logic in templates
- ✅ File I/O: JSON & CSV
- ✅ SQLite3 integration with error handling

---

## 📁 Repository Structure

```
python-server_side_rendering/
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── create_db.py
├── products.json
├── products.csv
├── products.db
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── list.html
    └── product_display.html
```

---

## 🏁 Author

Project completed at [Holberton School](https://www.holbertonschool.com/).
```

---

Nicolas Lassouane