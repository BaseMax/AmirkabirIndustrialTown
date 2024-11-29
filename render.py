import json

file = open('clean.json', 'r', encoding='utf-8')
data = json.load(file)

columns = ["نام شرکت", "برند", "زمینه فعالیت", "نام مدیریت", "تلفن ثابت", "نشانی", "کدپستی", "پلاک"]
rows = data["data"]

html_content = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>جدول اطلاعات</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h2 class="text-center mb-4">جدول اطلاعات</h2>
    <table class="table table-bordered table-hover text-center">
        <thead class="table-dark">
            <tr>
"""

for column in columns:
    html_content += f"                <th>{column}</th>\n"

html_content += """            </tr>
        </thead>
        <tbody>
"""

for row in rows:
    html_content += "            <tr>\n"
    for cell in row[1:]:
        html_content += f"                <td>{cell if cell else ''}</td>\n"
    html_content += "            </tr>\n"

html_content += """        </tbody>
    </table>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

file = open('table.html', 'w', encoding='utf-8')
file.write(html_content)

print("HTML table has been generated as 'table.html'.")
