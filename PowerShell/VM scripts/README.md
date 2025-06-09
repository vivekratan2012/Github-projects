# Azure VM Monitoring Script

This PowerShell script monitors Azure Virtual Machines (VMs) and reports key metrics such as CPU, memory, and disk usage, along with VM status.

---

##  Prerequisites

- Azure PowerShell module installed (`Az` module).
- Appropriate Azure permissions to access VM metrics.
- You must be logged in to your Azure account (`Connect-AzAccount`).

---

##  Usage

```powershell
.\Azure-VM-Monitoring.ps1 -ResourceGroupName "YourResourceGroup" -OutputFile "C:\Path\To\output.csv"
```
Parameters

-```ResourceGroupName```: Name of the Azure resource group containing the VMs.

-```OutputFile```: Path where the output CSV file will be saved.

## Sample Output
```powershell

VMName      CPU_Usage(%)  Memory_Usage(%)  Disk_Usage(%)  Status
-------     ------------  ---------------  ------------   ------
VM01        15            60               40             Running
VM02        50            70               80             Stopped
VM03        10            45               25             Running
```
## Notes

- The script uses Azure Monitor metrics and may require configuring diagnostic settings on VMs.

- Memory and disk usage retrieval depend on the VM OS and installed agents.

- Modify the script as needed to add alerts or integration with other monitoring tools.
