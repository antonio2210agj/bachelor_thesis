# Baut main.pdf: pdflatex -> biber -> pdflatex -> pdflatex.
# -shell-escape ist für das minted-Paket der Lehrstuhlvorlage nötig.
Set-Location $PSScriptRoot
$latex = @('-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-synctex=1', 'main.tex')

pdflatex @latex | Out-Null
if ($LASTEXITCODE -ne 0) { Select-String -Path main.log -Pattern '^!' -Context 0, 4; exit 1 }
biber main | Out-Null
if ($LASTEXITCODE -ne 0) { Get-Content main.blg -Tail 20; exit 1 }
pdflatex @latex | Out-Null
pdflatex @latex | Out-Null
if ($LASTEXITCODE -ne 0) { Select-String -Path main.log -Pattern '^!' -Context 0, 4; exit 1 }

Select-String -Path main.log -Pattern 'Output written|undefined|Citation .* undefined' | ForEach-Object { $_.Line }
