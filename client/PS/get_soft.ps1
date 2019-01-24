Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher, Size, InstallDate | ft DisplayName, DisplayVersion, Publisher, Size, InstallDate >> $PSScriptRoot\soft_32.txt
Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher, Size, InstallDate | ft DisplayName, DisplayVersion, Publisher, Size, InstallDate >> $PSScriptRoot\soft_64.txt