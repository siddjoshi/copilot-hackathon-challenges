function Get-CRC32Checksum {
  param (
    [Parameter(Mandatory=$true)]
    [string]$FilePath
  )

  if (-Not (Test-Path -Path $FilePath)) {
    throw "File not found: $FilePath"
  }

  $crc32Table = @(0..255 | ForEach-Object {
    [uint32]$crc = $_
    0..7 | ForEach-Object {
      if ($crc -band 1) {
        $crc = [uint32]([uint32]($crc) -shr 1) -bxor 0xEDB88320
      } else {
        $crc = [uint32]($crc -shr 1)
      }
    }
    $crc
  })

  [uint32]$crc32 = 4294967295
  $fileStream = [System.IO.File]::OpenRead($FilePath)
  try {
    while (($byte = $fileStream.ReadByte()) -ne -1) {
      $crc32 = [uint32]([uint32]($crc32) -shr 8) -bxor $crc32Table[[uint32]($crc32 -bxor $byte) -band 0xFF]
    }
  } finally {
    $fileStream.Close()
  }

  $crc32 = $crc32 -bxor 0xFFFFFFFF
  return "{0:X8}" -f $crc32
}

# Example Usage
$FilePath = "C:\Users\z004v6fu\Desktop\GHCP\ghcpnew2\copilot-hackathon-challenges\challenge-4\azure-overview.png"

Write-Output "Calculating CRC32 checksum for file: $FilePath"

if (Test-Path -Path $FilePath) {
  $checksum = Get-CRC32Checksum -FilePath $FilePath
  Write-Output "CRC32 checksum: $checksum"
} else {
  Write-Output "File Not Found: $FilePath"
}