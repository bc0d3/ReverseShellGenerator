# ReverseShellGenerator

This tool generates multiple reverse shells. The list of reverse shells is stored in a yml file, which you can modify to add more.
NOTE: This tool was focused on a PEN-300 student, to facilitate the reverse shell.
```
usage: rsg.py [-h] [--list] [--interface tun0] [--host 192.168.1.2] [--port 80] --generate

Reverse Shell Generator

options:
  -h, --help          show this help message and exit
  --list              List All Shell
  --interface tun0    Interface (Default=tun0)
  --host 192.168.1.2  IP Address (Default IP for interface tun0)
  --port 80           Port (Default=53)
  --generate          Generate Shell

```

