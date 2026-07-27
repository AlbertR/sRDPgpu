pyinstaller --noconfirm --onefile --windowed --name "sRDPgpu.1.2.1" --icon=RDapp_logo_v03.ico sRDPgpu.py


-= certificate renew =-
1.создать новый сертификат с тем же именем (FQDN) на RDG01 в IIS manager
2. закодировать его в base64
3. перепомпилировать исходним с новым сертификатом