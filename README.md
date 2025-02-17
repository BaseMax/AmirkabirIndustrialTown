# Amirkabir Industrial Town Database بانک اطلاعات شهرک صنعتی امیرکبیر کاشان ایران

This repository contains a SQL/JSON dataset of businesses located in the Amirkabir Industrial Town in Kashan, Iran. The dataset includes details about various companies, their activities, contact information, and locations.

Demo: https://basemax.github.io/AmirkabirIndustrialTown/

## Dataset Structure

The dataset follows the structure below:

```json
[
    "7",
    "بهرو سیکلت",
    "",
    "مونتاژ موتور سیکلت",
    "سید محسن عزیزی کاشی",
    "۵۵۵۰۳۳۵۷-۸",
    "کمربندی جنوبی",
    "۸۷۳۵۱۷۷۱۱۴",
    "۱۰۱"
]
```

### Fields Explanation:

- **ID**: A unique identifier for each business.
- **Company Name (فارسی)**: The name of the company in Persian.
- **Brand Name**: The commercial name or brand (if available).
- **Activity**: The main business activity (e.g., manufacturing, assembly, etc.).
- **Owner Name (فارسی)**: The name of the business owner in Persian.
- **Phone**: The company's contact phone number.
- **Address (فارسی)**: The location of the business within the industrial town.
- **Postal Code**: The postal code for the business's address.

## Sample Data

Here is an example of a record from the dataset:

| ID  | Company Name      | Brand | Activity               | Owner Name              | Phone          | Address       | Postal Code  |
|-----|-------------------|-------|------------------------|-------------------------|----------------|---------------|--------------|
| 7   | بهرو سیکلت        |       | مونتاژ موتور سیکلت    | سید محسن عزیزی کاشی    | ۵۵۵۰۳۳۵۷-۸     | کمربندی جنوبی | ۸۷۳۵۱۷۷۱۱۴ |
## How to Use

Clone the repository:

```bash
git clone https://github.com/BaseMax/AmirkabirIndustrialTown.git
```

Access the dataset file in JSON/SQL format to integrate or analyze as needed.

## Contributing

Contributions are welcome! If you have updated information or corrections, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the GPL3 License.

Source: https://amirkabirip.com/

## Contact

If you have any questions, feel free to contact the repository maintainer: @BaseMax

Copyright 2024, Max Base
