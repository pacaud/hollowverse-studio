# soulscript: pkws helper (PowerShell)
# Usage:
#   .\soulscripts\ss_git.ps1                 -> git status (default)
#   .\soulscripts\ss_git.ps1 status          -> git status
#   .\soulscripts\ss_git.ps1 pull            -> git pull origin master
#   .\soulscripts\ss_git.ps1 git pull        -> same as above

param(
    [string]$arg1,
    [string]$arg2
)

# Detect repo root using git
$repoRoot = git rev-parse --show-toplevel 2>$null

if (-not $repoRoot) {
    $repoRoot = Get-Location
}

Set-Location $repoRoot

# --- Simple domain + command parsing (git only for now) ---

$domain = $null
$cmd    = $null

if (-not $arg1) {
    # No args: default to git status
    $domain = "git"
    $cmd    = "status"
}
elseif ($arg1 -eq "git") {
    # Explicit git domain
    $domain = "git"
    if ($arg2) {
        $cmd = $arg2
    }
    else {
        $cmd = "status"
    }
}
else {
    # For now, treat anything else as a git subcommand
    $domain = "git"
    $cmd    = $arg1
}

switch ($domain) {
    "git" {
        switch ($cmd) {
            "pull" {
                Write-Host "[ss][git] git pull origin master"
                git pull origin master
            }
            "push" {
                Write-Host "[ss][git] git push origin master"
                git push origin master
            }
            "pushall" {
                Write-Host "[ss][git] git push origin master"
                git push origin master
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "[ss][git] git push github master"
                    git push github master
                }
            }
            "pullall" {
                Write-Host "[ss][git] git pull origin master"
                git pull origin master
                Write-Host "[ss][git] git pull github master"
                git pull github master
            }
            "status" {
                Write-Host "[ss][git] git status -sb"
                git status -sb
            }
            Default {
                Write-Host "[ss][git] Unknown git command: $cmd"
                Write-Host "Usage: .\soulscripts\ss_git.ps1 [git] {pull|push|pushall|pullall|status}"
            }
        }
    }
    Default {
        Write-Host "[ss] Unknown domain: $domain"
        Write-Host "Current domains: git"
    }
}
