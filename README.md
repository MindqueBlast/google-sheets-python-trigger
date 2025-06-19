# 🔄 Google Sheets Triggered Python Script (Auto Add Numbers)

This project connects a Google Sheet to a Python backend. When a row is marked `"in progress"`, the script sends two values (`arg1`, `arg2`) to a hosted Flask API, calculates their sum, and updates the Google Sheet with the result and `"complete"` status.

---

## ✅ Features

- Google Sheets triggers a Python script based on cell value
- Hosted Flask API receives data and returns sum
- Result is written back into the sheet automatically
- Status updates to `"complete"` once processed

---

## 📁 File Structure

```
├── app.py                # Flask app that receives and processes data
├── requirements.txt      # Flask dependency list
└── README.md             # You're here
```

---

## 🧾 Google Sheet Setup

Set up your sheet like this:

| Arg 1 | Arg 2 | Status       | Result |
|-------|--------|--------------|--------|
|   3   |   4    | in progress  |        |

- **Column A**: First number (arg1)
- **Column B**: Second number (arg2)
- **Column C**: Status (`not started`, `in progress`, `complete`)
- **Column D**: Result (automatically filled in)

---

## ☁️ Deploy Flask API to Render

1. [Create a Render account](https://render.com)
2. Click **"New Web Service"**, connect your GitHub repo
3. Settings:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

4. Make sure your `app.py` ends with:

```python
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

5. After deployment, Render gives you a public URL like:

```
https://your-app-name.onrender.com
```

6. Your endpoint will be:

```
https://your-app-name.onrender.com/add
```

---

## 🧠 Google Apps Script Setup

1. In your Google Sheet, go to `Extensions > Apps Script`
2. Paste the following code:

```javascript
function checkRowsAndProcess() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName("Sheet1");  // Change this if your sheet has a different name
  if (!sheet) {
    Logger.log("Sheet not found!");
    return;
  }
  
  const statusCol = 3;  // Column C
  const resultCol = 4;  // Column D
  const lastRow = sheet.getLastRow();

  for (let row = 2; row <= lastRow; row++) {
    const status = sheet.getRange(row, statusCol).getValue();

    if (typeof status === "string" && status.trim().toLowerCase() === "in progress") {
      const arg1 = sheet.getRange(row, 1).getValue();
      const arg2 = sheet.getRange(row, 2).getValue();

      Logger.log(`Processing row ${row} with arg1=${arg1}, arg2=${arg2}`);

      const payload = {
        row: row,
        arg1: arg1,
        arg2: arg2
      };

      const options = {
        method: "post",
        contentType: "application/json",
        payload: JSON.stringify(payload)
      };

      try {
        const url = "https://your-app-name.onrender.com/add"; // Replace with your actual URL
        const response = UrlFetchApp.fetch(url, options);
        const result = JSON.parse(response.getContentText());

        Logger.log(`Server returned for row ${row}: ${JSON.stringify(result)}`);

        if (result.status === "complete") {
          if (result.sum !== undefined) {
            sheet.getRange(row, resultCol).setValue(result.sum);
            Logger.log(`Wrote sum ${result.sum} to row ${row}, column ${resultCol}`);
          }
          sheet.getRange(row, statusCol).setValue("complete");
          Logger.log(`Updated status to 'complete' at row ${row}, column ${statusCol}`);
        }
      } catch (err) {
        Logger.log(`Error processing row ${row}: ${err}`);
      }
    }
  }
}
```

3. Save the script.
4. Go to the clock icon (⏱️) in Apps Script > Add Trigger:
   - Choose `checkRowsAndProcess`
   - Select `Time-driven` > Every 5 minutes

---

## 🧪 Testing

1. Add values in column A and B
2. Change column C to `"in progress"`
3. Wait 1–5 minutes or run the script manually
4. Column D will show the result, and column C will change to `"complete"`

---

## 📦 requirements.txt

```
flask
```

Install with:

```
pip install -r requirements.txt
```

## 📄 License

MIT License
