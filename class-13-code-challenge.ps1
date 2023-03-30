#!/usr/bin/env python3

# Script: Ops 301d6 Class 13 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/29/2023
# Purpose: Powershell AD Automation
# Resources: Chat GPT


# Start

# Set up variables for user attributes
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$userName = "ferdi"
$office = "Springfield"
$company = "GlobeX USA"
$department = "TPS"
$email = "ferdi@GlobeXpower.com"
$password = "Password1!" #Replace this with a secure password for the new user

# Create a new user object with the specified attributes
New-ADUser -Name $displayName `
           -GivenName $firstName `
           -Surname $lastName `
           -DisplayName $displayName `
           -SamAccountName $userName `
           -UserPrincipalName "$userName@yourdomain.com" `
           -Path "OU=TPS,OU=Users,DC=yourdomain,DC=com" `
           -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force) `
           -Enabled $true `
           -Office $office `
           -Company $company `
           -Department $department `
           -EmailAddress $email

# Verify that the user was created correctly
Get-ADUser $userName -Properties * | Format-List *

# End