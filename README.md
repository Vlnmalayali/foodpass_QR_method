# 🍽️ FoodPass QR System — Setup Guide

---

## ✅ Step 1: Create the Google Sheet

1. Open [Google Sheets](https://sheets.google.com) and create a new sheet.

2. Name it exactly: **FoodPass**

3. <img width="330" height="47" alt="image" src="https://github.com/user-attachments/assets/a8cb4db2-f957-4396-ac6e-b66b830e8ce2" />


4. In the **first sheet (default tab)**, add these column headings:

   `````````````````````````````````````````````````````````````````````
   | ID | NAME | Phone Number | QR | Status | Timestamp | Whatsapp |
   ``````````````````````````````````````````````````````````````````

5. Add a **new sheet** (tab) inside the same file.

   * Name it: **Scanlog**
   * Add these column headings:

   ``````````````````````````````````````````
   | Name | Phone Number | ID | Timestamp |
   ``````````````````````````````````````````

---

## ✅ Step 2: Add the Google Apps Script

1. In the sheet, go to **Extensions → Apps Script**.
2. Delete any existing code, then paste your script (App Script code).
3. Replace placeholders in the script:

   * `YOUR_SPREADSHEET_ID` → copy your sheet ID from the URL
     (looks like: `1aBcD3FGhIJkLmnopQRsTuvWXyZ1234567890`)
   * Update sheet/tab names if needed (`FoodPass`, `Scanlog`)
   * Replace the event logo link if you want a custom logo.
   * change the line 82 from App Script Code (it's a logo so paste other url of you logo there) 
---

## ✅ Step 3: Deploy the Script as a Web App

1. Click **Deploy → Manage Deployments**
2. Click **New deployment**
3. Select **Web app**
4. Set:

   * **Execute as**: *Me*
   * **Who has access**: *Anyone* (or *Anyone with the link*)
5. Click **Deploy** → copy the **Web App URL**

   Example:

   ```
   https://script.google.com/macros/s/AKfycbxz8cpc9IH5x0uodrnn_4vdKcuDG_pU03ZVdtjChqiYp5zUhhLg8CLkgEqVrOjgZIEn/exec
   ```

   🔑 Keep the **web app ID** (`AKfycbxz8cpc9IH5x0uodrnn_4vdKcuDG_pU03ZVdtjChqiYp5zUhhLg8CLkgEqVrOjgZIEn`) safe.

---

## ✅ Step 4: Generate QR Codes

1. In the **FoodPass sheet**, go to the `QR` column.
2. Enter this formula (adjust column references if needed):

   ```excel
   =IMAGE("https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=" & ENCODEURL("https://script.google.com/macros/s/(webappid)/exec?code=" & A2))
   ```

   * Replace **`(webappid)`** with your real Web App ID.
   * `A2` refers to the **ID column** of the first row.
3. Drag down the formula to auto-generate QR codes for all rows.

---

## ✅ Step 5: Export QR Codes to Google Drive

1. In Apps Script, next to **Run / Debug**, select the function **`exportQRsToDrive`** (instead of `doGet`).
2. <img width="545" height="263" alt="image" src="https://github.com/user-attachments/assets/4b523003-4996-42b4-9a34-a9564780a06d" />

3. Click **Run**.
4. Wait until the script finishes — all QR codes will be saved to your **Google Drive**.

---

## ✅ Step 6: Build the Final FoodPass

1. from Google Drive download localy , create a folder structure like:

   ```
   FoodPass
   ├── Output          (final generated passes)
   ├── Qr_images       (all QR codes)
   ├── foodpasscode    (the script/code for generation)
   └── pass            (the background template image)
   ```

2. Place your background pass design in the **pass** folder.

3. Run the **foodpasscode** script to automatically generate **complete FoodPasses** with embedded QR codes.

---

✨ Now you have a **working FoodPass system** with QR generation, scan logging, and automated pass creation!

---
