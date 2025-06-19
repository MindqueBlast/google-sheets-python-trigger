Here’s a complete `README.md` file for your GitHub repo. It includes an overview, setup instructions, Google Sheets + Render integration steps, and deployment instructions so **anyone can use your project**.

---

### 📄 `README.md`

```markdown
# 🔄 Google Sheets Triggered Python Script (Auto Add Numbers)

This project allows you to automatically run a Python script every time a row in a Google Sheet is marked `"in progress"` — then update the sheet with the result and change the status to `"complete"`.

### ✅ What it does:
- Monitors your Google Sheet for any row where the status is `"in progress"`.
- Sends two values (`arg1`, `arg2`) to a hosted Python API.
- The API returns the sum.
- The script writes the sum in a result column and marks the task as `"complete"`.

---

## 📁 File Structure

```

├── app.py                # Flask app that receives and processes data
├── requirements.txt      # Flask dependency list
└── README.md             # You're here

````

---

## ⚙️ How It Works

### 🧾 Google Sheet Setup

| Arg 1 | Arg 2 | Status       | Result |
|-------|--------|--------------|--------|
|   3   |   4    | in progress  |        |

- Column A (1): First number
- Column B (2): Second number
- Column C (3): Status (dropdown: `not started`, `in progress`, `complete`)
- Column D (4): Result (auto-filled by the script)

---

### ☁️ Hosting the Python Script on Render

1. **Create a Render account**: https://render.com
2. **New Web Service → Connect your GitHub repo**
3. Use these settings:
   - **Environment**: Python
   - **Start command**: `python app.py`
   - **Build command**: `pip install -r requirements.txt`
4. Render automatically assigns a port. Make sure `app.py` uses:

```python
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
````

---

### 🧠 Google Apps Script Setup

1. In your Google Sheet, go to `Extensions > Apps Script`
2. Paste the Apps Script code from this repo (see below)
3. Replace:

   * Sheet name (e.g. `"Sheet1"`)
   * Your hosted API URL (from Render)
4. Save and deploy

---

### ⏰ Add a Time Trigger

1. In Apps Script, click the ⏰ **Triggers icon**
2. Add a trigger:

   * Function: `checkRowsAndProcess`
   * Event type: Time-driven
   * Frequency: Every 5 minutes (or as needed)

---

## 💻 Flask API Overview

```python
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = int(data["arg1"]) + int(data["arg2"])
    return jsonify({"status": "complete", "sum": result})
```

---

## 🧪 Testing

1. Enter two numbers in Arg1 and Arg2
2. Set Status to `"in progress"`
3. Wait 1–5 minutes (or manually run script)
4. Status should change to `"complete"` and Result should be filled

---

## 📦 Requirements

**requirements.txt**

```
flask
```

Install locally with:

```bash
pip install -r requirements.txt
```

## 📄 License

MIT License

```

