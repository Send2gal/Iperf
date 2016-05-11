import asyncio, asyncssh, sys

@asyncio.coroutine
def run_client():
    with (yield from asyncssh.connect('10.0.0.16')) as conn:
        stdin, stdout, stderr = yield from conn.open_session('echo "Hello!"')

        output = yield from stdout.read()
        print(output, end='')

        yield from stdout.channel.wait_closed()

        status = stdout.channel.get_exit_status()
        if status:
            print('Program exited with status %d' % status, file=sys.stderr)
        else:
            print('Program exited successfully')

asyncio.get_event_loop().run_until_complete(run_client())