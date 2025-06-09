<#
.SYNOPSIS
Creates Active Directory users in bulk from a CSV file.

.DESCRIPTION
This script reads user data from a CSV and creates Active Directory accounts in the specified OU.

.PARAMETER CsvPath
Path to the CSV file containing user details.

.PARAMETER OU
Distinguished Name (DN) of the Organizational Unit where users will be created.

.EXAMPLE
.\AD-Bulk-User-Creation.ps1 -CsvPath "C:\Users.csv" -OU "OU=Staff,DC=example,DC=local"
#>

param (
    [Parameter(Mandatory = $true)]
    [string]$CsvPath,

    [Parameter(Mandatory = $true)]
    [string]$OU
)

Import-Module ActiveDirectory

if (!(Test-Path $CsvPath)) {
    Write-Error "CSV file not found at $CsvPath"
    exit 1
}

$users = Import-Csv -Path $CsvPath

foreach ($user in $users) {
    $userPrincipalName = "$($user.SamAccountName)@yourdomain.local"

    try {
        New-ADUser `
            -Name "$($user.FirstName) $($user.LastName)" `
            -SamAccountName $user.SamAccountName `
            -UserPrincipalName $userPrincipalName `
            -GivenName $user.FirstName `
            -Surname $user.LastName `
            -AccountPassword (ConvertTo-SecureString $user.Password -AsPlainText -Force) `
            -Path $OU `
            -Enabled $true `
            -ChangePasswordAtLogon $false

        Write-Host "Created user: $($user.SamAccountName)" -ForegroundColor Green
    }
    catch {
        Write-Warning "Failed to create $($user.SamAccountName): $_"
    }
}
