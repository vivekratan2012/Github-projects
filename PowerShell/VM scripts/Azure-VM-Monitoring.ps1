<#
.SYNOPSIS
Collects Azure VM power state and key performance metrics.

.DESCRIPTION
Fetches VM status, CPU average, available memory, and disk throughput using Azure Monitor.

.PARAMETER ResourceGroup
Azure Resource Group name.

.PARAMETER OutputCSV
Optional: Export results to a CSV file.

.EXAMPLE
.\Azure-VM-Monitoring.ps1 -ResourceGroup "Prod-RG" -OutputCSV "report.csv"
#>

param (
    [Parameter(Mandatory = $true)]
    [string]$ResourceGroup,

    [string]$OutputCSV
)

# Login
Connect-AzAccount -ErrorAction Stop

# Define time window (last 30 minutes)
$endTime = (Get-Date).ToUniversalTime()
$startTime = $endTime.AddMinutes(-30)
$timeGrain = "PT5M"  # 5-minute samples

# Fetch all VMs in the group
$vms = Get-AzVM -ResourceGroupName $ResourceGroup
$results = @()

foreach ($vm in $vms) {
    $vmStatus = (Get-AzVM -ResourceGroupName $ResourceGroup -Name $vm.Name -Status).Statuses |
                Where-Object { $_.Code -like "PowerState*" }

    $metrics = @(
        "Percentage CPU",
        "Available Memory Bytes",
        "Disk Read Bytes",
        "Disk Write Bytes"
    )

    $metricData = Get-AzMetric -ResourceId $vm.Id `
        -TimeGrain $timeGrain `
        -StartTime $startTime `
        -EndTime $endTime `
        -MetricName $metrics

    # Extract CPU
    $cpuAvg = ($metricData | Where-Object {$_.Name.Value -eq "Percentage CPU"}).Data |
              Where-Object { $_.Average -ne $null } |
              Measure-Object -Property Average -Average | Select-Object -ExpandProperty Average

    # Memory (convert bytes to MB)
    $memBytes = ($metricData | Where-Object {$_.Name.Value -eq "Available Memory Bytes"}).Data |
                Where-Object { $_.Average -ne $null } |
                Measure-Object -Property Average -Average | Select-Object -ExpandProperty Average
    $memMB = [math]::Round($memBytes / 1MB, 2)

    # Disk (bytes per second → MB per second)
    $readBytes = ($metricData | Where-Object {$_.Name.Value -eq "Disk Read Bytes"}).Data |
                 Where-Object { $_.Average -ne $null } |
                 Measure-Object -Property Average -Average | Select-Object -ExpandProperty Average

    $writeBytes = ($metricData | Where-Object {$_.Name.Value -eq "Disk Write Bytes"}).Data |
                  Where-Object { $_.Average -ne $null } |
                  Measure-Object -Property Average -Average | Select-Object -ExpandProperty Average

    $results += [PSCustomObject]@{
        VMName        = $vm.Name
        Location      = $vm.Location
        PowerState    = $vmStatus.DisplayStatus
        VMSize        = $vm.HardwareProfile.VmSize
        CPU_Avg       = [math]::Round($cpuAvg, 2)
        MemoryFree_MB = $memMB
        DiskRead_MBps = [math]::Round($readBytes / 1MB, 2)
        DiskWrite_MBps= [math]::Round($writeBytes / 1MB, 2)
    }
}

$results | Format-Table -AutoSize

if ($OutputCSV) {
    $results | Export-Csv -Path $OutputCSV -NoTypeInformation
    Write-Host "Report exported to $OutputCSV" -ForegroundColor Cyan
}
