# soulscript: pkws ssh helper (PowerShell)
# Usage:
#   ss shrine              -> ssh into Shrine of Memories (droplet)
#   ss vault               -> ssh into Vault of Memories (Pi)
#   ss shrine <extra args> -> ssh root@... <extra args>
#   ss vault <extra args>  -> ssh kevin@... <extra args>

# Use automatic $args from PowerShell
$allArgs = @($args)

if (-not $allArgs -or $allArgs.Count -eq 0) {
    Write-Host "[ss][ssh] Usage: ss shrine | ss vault"
    exit 1
}

$target = $allArgs[0]
$rest   = @()
if ($allArgs.Count -gt 1) {
    $rest = $allArgs[1..($allArgs.Count - 1)]
}

# Hosts — update if you change names/IPs later
$shrineHost = "root@134.122.40.163"          # Shrine of Memories (droplet)
$vaultHost  = "kevin@PkW-Vault-Of-Memories"  # Vault of Memories (Pi)

$sshHost = $null

switch ($target) {
    "shrine" {
        $sshHost = $shrineHost
    }
    "vault" {
        $sshHost = $vaultHost
    }
    default {
        Write-Host "[ss][ssh] Unknown target: $target"
        Write-Host "[ss][ssh] Use: ss shrine  or  ss vault"
        exit 1
    }
}

if ($rest.Count -gt 0) {
    $extra = $rest -join ' '
    Write-Host "[ss][ssh] ssh $sshHost $extra"
    ssh $sshHost @rest
}
else {
    Write-Host "[ss][ssh] ssh $sshHost"
    ssh $sshHost
}
