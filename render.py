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
    <title>جدول اطلاعات شهرک صنعتی امیرکبیر</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css" rel="stylesheet" type="text/css">
    <style>
        body {{
            font-family: Vazirmatn, Arial, sans-serif;
        }}
        .search-input {{
            margin-bottom: 20px;
            max-width: 300px;
        }}
    </style>
</head>
<body>
<div class="container mt-5">
    <h2 class="text-center mb-4">جدول اطلاعات شهرک صنعتی امیرکبیر</h2>
    <input type="text" id="searchInput" class="form-control search-input" placeholder="جستجو در جدول..." onkeyup="filterTable()">
    <table id="dataTable" class="table table-bordered table-hover text-center">
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
<script>
    function filterTable() {
        const input = document.getElementById('searchInput');
        const filter = input.value.toLowerCase();
        const table = document.getElementById('dataTable');
        const rows = table.getElementsByTagName('tr');

        for (let i = 1; i < rows.length; i++) {
            const cells = rows[i].getElementsByTagName('td');
            let rowContainsFilter = false;

            for (let j = 0; j < cells.length; j++) {
                if (cells[j].innerText.toLowerCase().includes(filter)) {
                    rowContainsFilter = true;
                    break;
                }
            }

            rows[i].style.display = rowContainsFilter ? '' : 'none';
        }
    }
</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

file = open('table.html', 'w', encoding='utf-8')
file.write(html_content)

print("HTML table with search functionality has been generated as 'table.html'.")
