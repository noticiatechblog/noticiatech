param(
  [int]$Port = 1313,
  [switch]$Drafts,
  [switch]$Network
)

$ErrorActionPreference = "Stop"

$bindAddress = "127.0.0.1"
$baseUrl = "http://localhost:$Port/"
$networkUrl = $null

if ($Network) {
  $wifiIp = Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object {
      $_.IPAddress -notlike "127.*" -and
      $_.IPAddress -notlike "169.254.*" -and
      $_.InterfaceAlias -match "Wi-Fi|Wireless|WLAN|Ethernet"
    } |
    Sort-Object { if ($_.InterfaceAlias -match "Wi-Fi|Wireless|WLAN") { 0 } else { 1 } } |
    Select-Object -First 1 -ExpandProperty IPAddress

  if (-not $wifiIp) {
    throw "Nao encontrei um IP da rede local. Confira se o Wi-Fi/Ethernet esta conectado."
  }

  $bindAddress = "0.0.0.0"
  $baseUrl = "http://${wifiIp}:$Port/"
  $networkUrl = $baseUrl
}

$hugoArgs = @(
  "server",
  "--buildFuture",
  "--disableFastRender",
  "--bind", $bindAddress,
  "--baseURL", $baseUrl,
  "--port", "$Port"
)

if ($Drafts) {
  $hugoArgs += "--buildDrafts"
}

Write-Host "Abrindo o blog no PC em http://localhost:$Port/"

if ($networkUrl) {
  Write-Host "Abrindo o blog no celular em $networkUrl"
}

Write-Host "Posts futuros: ativados"

if ($Drafts) {
  Write-Host "Rascunhos: ativados"
}

hugo @hugoArgs
