import os
import json
from telethon import TelegramClient
from datetime import datetime
import logging
import asyncio
from time import sleep

# init logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def main():
        logger.info('Starting...')
        # Create the client and connect
        api_id = os.environ.get('API_ID')
        api_hash = os.environ.get('API_HASH')
        app_title = os.environ.get('APP_TITLE')
        client = TelegramClient(app_title, api_id, api_hash)

        logger.info('Connecting...')
        await client.connect()
        if not await client.is_user_authorized():
                phone_number = os.environ.get('PHONE_NUMBER')
                await client.send_code_request(phone_number)
                # wait for auth.code appears in data folder
                logger.info('Please, put auth code in data/auth.code file')
                while not os.path.exists('data/auth.code'):
                        sleep(1)
                logger.info('auth.code received')
                with open('data/auth.code', 'r') as f:
                        code = f.read().strip()
                logger.info('Sing in...')
                password = os.environ.get('PASSWORD')

                await client.sign_in(phone = phone_number)
                try:
                        await client.sign_in(code = code)
                except Exception as e:
                        logger.error('Error: {}'.format(e))
                        await client.sign_in(password = password)

                logger.info('Signed in')
        logger.info('Client is ready')

        # send status message
        await client.send_message('me', 'Collector is running')

        logger.info('Finished')


if __name__ == "__main__":
        asyncio.run(main())
