$exclude = @("venv", "bot_pesquisa_vagas.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_pesquisa_vagas.zip" -Force