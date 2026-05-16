param(
  [int]$Port = 1313,
  [switch]$Drafts
)

$ErrorActionPreference = "Stop"

$hugoArgs = @(
  "server",
  "--buildFuture",
  "--disableFastRender",
  "--bind", "127.0.0.1",
  "--baseURL", "http://localhost:$Port/",
  "--port", "$Port"
)

if ($Drafts) {
  $hugoArgs += "--buildDrafts"
}

Write-Host "Abrindo o blog em http://localhost:$Port/"
Write-Host "Posts futuros: ativados"

if ($Drafts) {
  Write-Host "Rascunhos: ativados"
}

hugo @hugoArgs
