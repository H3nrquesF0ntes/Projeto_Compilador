# Gera lexer/parser Python a partir da gramática ANTLR4
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$grammar = Join-Path $root "grammar\SimpleLang.g4"
$out = Join-Path $root "src\generated"

function Get-Antlr4Command {
    $cmd = Get-Command antlr4 -ErrorAction SilentlyContinue
    if ($cmd) {
        return $cmd.Source
    }

    $exe = py -3.13 -c @"
import os, site, sys, sysconfig
candidates = [
    os.path.join(site.USER_BASE, f'Python{sys.version_info.major}{sys.version_info.minor}', 'Scripts', 'antlr4.exe'),
    os.path.join(sysconfig.get_path('scripts'), 'antlr4.exe'),
]
for path in candidates:
    if os.path.isfile(path):
        print(path)
        break
"@
    if ($LASTEXITCODE -ne 0) {
        throw "Python 3.13 nao encontrado. Instale o Python ou ajuste o script."
    }

    $exe = $exe.Trim()
    if (Test-Path $exe) {
        return $exe
    }

    throw "antlr4 não encontrado. Instale com: py -3.13 -m pip install -r requirements.txt"
}

if (-not (Test-Path $out)) {
    New-Item -ItemType Directory -Path $out | Out-Null
}

$antlr4 = Get-Antlr4Command
Write-Host "Gerando parser em $out ..."
& $antlr4 -Dlanguage=Python3 -visitor -no-listener -o $out $grammar
Write-Host "Concluido."
