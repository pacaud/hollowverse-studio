# soulscript: pkws git helper (PowerShell)
# Usage:
#   ss git status
#   ss git pull
#   ss git push
#   ss git pushall
#   ss git pullall
#   ss git add .
#   ss git add <file> [...]
#   ss git commit "message here"

# All command-line args come from $args
$allArgs = @($args)

# Detect repo root using git
$repoRoot = git rev-parse --show-toplevel 2>$null

if (-not $repoRoot) {
    $repoRoot = Get-Location
}

Set-Location $repoRoot

$domain = $null
$cmd    = $null
$rest   = @()

if (-not $allArgs -or $allArgs.Count -eq 0) {
    # No args: default to git status
    $domain = "git"
    $cmd    = "status"
}
elseif ($allArgs[0] -eq "git") {
    # Explicit git domain: ss git <cmd> [args...]
    $domain = "git"

    if ($allArgs.Count -gt 1) {
        $cmd = $allArgs[1]
    }
    else {
        $cmd = "status"
    }

    if ($allArgs.Count -gt 2) {
        $rest = $allArgs[2..($allArgs.Count - 1)]
    }
}
else {
    # For now, treat anything else as a git subcommand
    # ss add . / ss commit "msg" / etc.
    $domain = "git"
    $cmd    = $allArgs[0]

    if ($allArgs.Count -gt 1) {
        $rest = $allArgs[1..($allArgs.Count - 1)]
    }
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
            "add" {
                if ($rest.Count -gt 0) {
                    $targets = $rest
                    Write-Host "[ss][git] git add $($targets -join ' ')"
                    git add @targets
                }
                else {
                    Write-Host "[ss][git] git add ."
                    git add .
                }
            }
            "commit" {
                if ($rest.Count -gt 0) {
                    $message = [string]::Join(" ", $rest)
                    Write-Host "[ss][git] git commit -m `"$message`""
                    git commit -m "$message"
                }
                else {
                    Write-Host "[ss][git] git commit"
                    git commit
                }
            }
            "status" {
                Write-Host "[ss][git] git status -sb"
                git status -sb
            }
            Default {
                Write-Host "[ss][git] Unknown git command: $cmd"
                Write-Host "Usage: ss git {status|pull|push|pushall|pullall|add|commit}"
            }
        }
    }
    Default {
        Write-Host "[ss] Unknown domain: $domain"
        Write-Host "Current domains: git"
    }
}
