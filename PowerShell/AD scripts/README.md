# AD Bulk User Creation Script

This PowerShell script automates the creation of Active Directory users in bulk from a CSV file.

## Prerequisites

- PowerShell with the ActiveDirectory module.
- Permissions to create users in Active Directory.
- Run on a domain-joined machine.

## CSV Format

The input CSV should follow this structure:
```
FirstName,LastName,SamAccountName,Password

Alice,Johnson,ajohnson,Pa$$word123

Carol,Williams,cwilliams,Pa$$word123
```
## Usage

Run the script with parameters like this:

```console
.\AD-Bulk-User-Creation.ps1 -CsvPath "C:\Path\To\users.csv" -OU "OU=Users,DC=example,DC=com"
```
Parameters
-CsvPath: Full path to the CSV file.

-OU: Distinguished Name of the target OU (Organizational Unit).

✅ Sample Output

```
Created user: ajohnson
Created user: bsmith
Created user: cwilliams
```