# DataHive Automation Pipeline

## Overview

This automation pipeline downloads, processes, validates, and uploads inventory, sales, advertising, and marketplace performance data for Pattex across multiple platforms.

---

# Notebooks Executed

| Notebook                                     | Purpose                                                     |
| -------------------------------------------- | ----------------------------------------------------------- |
| `pattex_vendor_central_azure.ipynb`          | Downloads and processes Amazon Vendor Central reports       |
| `pattex_seller_central_azure_push.ipynb`     | Downloads and processes Amazon Seller Central reports       |
| `pattex_VC.ipynb`                            | Vendor Central data transformation and validation           |
| `pattex_SC.ipynb`                            | Seller Central data transformation and validation           |
| `flipkart_codes.ipynb`                       | Flipkart sales, inventory, and advertising data processing  |
| `instamart_codes.ipynb`                      | Instamart sales, inventory, and advertising data processing |
| `Zepto_codes.ipynb`                          | Zepto sales, inventory, and advertising data processing     |
| `dark_store_inventory_noon_min_pattex.ipynb` | Noon Minutes dark store inventory extraction                |
| `pattex_noon_minutes.ipynb`                  | Noon Minutes sales and advertising data processing          |
| `Kinetica.ipynb`                             | Data integration and upload processes                       |
| `pnl_ecom.ipynb`                             | E-commerce P&L generation and database upload               |

---

# Amazon Seller Central Requirements

## Reports to Download

* Sales Reports
* Inventory Reports

## Date Logic

* Download reports for the **current date**.

## Output

* Process downloaded files.
* Store processed output files in the designated output location.

---

# Amazon Vendor Central Requirements

## Reports to Download

* Sales Reports
* Inventory Reports

## Date Logic

* Download reports for **T-3** (Current Date - 3 Days).

### Month Change Logic

If a new month has started:

* Download reports for the **current month**.
* Download reports for the **previous month**.

## Output

* Process downloaded files.
* Store processed output files in the designated output location.

---

# Marketing / Advertising Requirements

## Platforms Covered

* Amazon Seller Central
* Amazon Vendor Central
* Flipkart
* Instamart
* Zepto
* Noon Minutes

## Reports to Download

* Bulk Advertising Reports
* Campaign Performance Reports
* Sponsored Ads Reports (where applicable)

## Date Logic

* Download advertising reports for the **current date**.

## Output

* Process and store all advertising reports.

---

# Noon Minutes Requirements

## Inventory

* Download inventory reports for the current date.

## Sales

* Download sales reports for the current date.

## Advertising

* Download advertising performance reports for the current date.

## Output

* Process and store all generated files.

---

# Output Requirements

* Store all processed files in their respective output directories.
* Maintain standardized file formats across platforms.
* Generate execution logs for every notebook.
* Log all failures with detailed error messages.
* Preserve historical outputs where applicable.

---

# Execution Sequence

```text
1. pattex_vendor_central_azure.ipynb
2. pattex_seller_central_azure_push.ipynb
3. pattex_VC.ipynb
4. pattex_SC.ipynb
5. flipkart_codes.ipynb
6. instamart_codes.ipynb
7. Zepto_codes.ipynb
8. dark_store_inventory_noon_min_pattex.ipynb
9. pattex_noon_minutes.ipynb
10. Kinetica.ipynb
11. pnl_ecom.ipynb
```

---

# Expected Result

Upon successful execution:

* All marketplace reports are downloaded.
* Sales, inventory, and advertising datasets are processed.
* Data is validated and transformed.
* Processed files are stored in output locations.
* Data is uploaded to the required destinations.
* E-commerce P&L tables are refreshed and updated.
* Execution logs are generated for monitoring and troubleshooting.
