$process = Start-Process -FilePath "ssh" -ArgumentList "toriba@31.97.82.215" -NoNewWindow -PassThru -RedirectStandardInput "input.txt" -RedirectStandardOutput "output.txt" -RedirectStandardError "error.txt"
Start-Sleep -Seconds 3
Add-Content -Path "input.txt" -Value "d7ZzsveuawF2oT0SdSGZ"
$process.WaitForExit() 