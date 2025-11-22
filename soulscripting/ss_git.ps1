# soulscript: pkws helper (PowerShell)
# Usage:
#   .\soulscripts\ss_git.ps1                 -> git status (default)
#   .\soulscripts\ss_git.ps1 status          -> git status
#   .\soulscripts\ss_git.ps1 pull            -> git pull origin master
#   .\soulscripts\ss_git.ps1 git pull        -> same as above
#   (future) .\soulscripts\ss_git.ps1 ssh ... -> other domain

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
    $cmd    = ($arg2 ? $arg2 : "status")
}
else {
    # For now, treat anything else as a git subcommand
    # (future: if ($arg1 -eq "ssh") { $domain = "ssh"; ... })
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
