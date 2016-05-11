# adapted from http://stackoverflow.com/a/34114767/452281

import asyncio
import sys
from asyncio.subprocess import PIPE, STDOUT

IP = '10.0.0.8'
USER = 'gal'
PASSWORD = '1234'
COMMAND = 'df -h'

def do_something(raw):
    data = raw.decode("utf-8")
    lines = data.splitlines()
    for i in lines:
        print(i)

async def run_command(*args, timeout=None):
    # start child process
    # NOTE: universal_newlines parameter is not supported
    process = await asyncio.create_subprocess_exec(*args,
            stdout=PIPE, stderr=STDOUT)

    # read line (sequence of bytes ending with b'\n') asynchronously
    while True:
        try:
            line = await asyncio.wait_for(process.stdout.read(), timeout)
        except asyncio.TimeoutError:
            print("timeout occurred")
        else:
            if not line: # EOF
                break
            elif do_something(line):
                continue # while some criterium is satisfied
        process.kill() # timeout or some criterium is not satisfied
        break
    return await process.wait() # wait for the child process to exit


if sys.platform == "win32":
    loop = asyncio.ProactorEventLoop() # for subprocess' pipes on Windows
    asyncio.set_event_loop(loop)
else:
    loop = asyncio.get_event_loop()

# returncode = loop.run_until_complete(run_command("plink.exe", "-ssh", "root@10.18.134.101", "-pw 123456",
#                                                  " ".join(sys.argv[1:]),  timeout=10))
returncode = loop.run_until_complete(run_command("plink.exe",
                                                 "{}@{}".format(USER, IP),
                                                 "-ssh", " ".join(COMMAND),  timeout=10))

loop.close()