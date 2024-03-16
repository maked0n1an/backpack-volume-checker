import asyncio
import sys
import aiohttp

from custom_logger import logger
from input_data.settings import IS_ACCOUNT_NAMES

with open('input_data/proxies.txt', 'r') as file:
    PROXIES = [row.strip() for row in file]

with open('input_data/cookies.txt', 'r') as file:
    COOKIES = [row.strip() for row in file]

with open('input_data/account_names.txt', 'r') as file:
    ACCOUNT_NAMES = [row.strip() for row in file]


def get_accounts():
    if IS_ACCOUNT_NAMES:
        accounts = [
            {
                "name": account_name,
                "cookies": cookies,
                "proxy": proxy
            } for account_name, cookies, proxy in zip(ACCOUNT_NAMES, COOKIES, PROXIES * len(COOKIES))
        ]
    else:
        accounts = [
            {
                "name": _id,
                "cookies": cookies,
                "proxy": proxy
            } for _id, (cookies, proxy) in enumerate(zip(COOKIES, PROXIES * len(PROXIES)), start=1)
        ]

    return accounts


async def fetch_data(url, params, proxy, cookies, headers):
    try:
        async with aiohttp.ClientSession() as session:
            request = await session.get(
                url=url,
                headers=headers,
                params=params,
                proxy=proxy,
                cookies=cookies,
            )
            return await request.json()
    except Exception as e:
        logger.error(f"An error occurred: {e}")

def is_bot_setuped_to_start():
    end_bot = False

    if len(COOKIES) == 0:
        logger.error("Don't imported COOKIES in 'cookies.txt'!")
        return end_bot
    if len(ACCOUNT_NAMES) == 0 and IS_ACCOUNT_NAMES:
        logger.error("Please insert names into account_names.txt")
        return end_bot
    if len(COOKIES) != len(ACCOUNT_NAMES) and IS_ACCOUNT_NAMES:
        logger.error(
            "The account names' amount must be equal to cookies' amount")
        return end_bot
    
    return True

async def main():
    if not is_bot_setuped_to_start():
        sys.exit()
    
    accounts = get_accounts()
    site = 'https://api.eu.backpack.exchange/wapi/v1/history/fills'

    params = {
        'limit': '100000000',
    }
    headers = {
        'authority': 'api.eu.backpack.exchange',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'fr-BE,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    tasks = []
    for account in accounts:
        cookies = str(account['cookies'])
        individual_cookies = cookies.split('; ')
        
        session_value = None
        aws_waf_token_value = None
        for cookie in individual_cookies:
            if cookie.startswith('session='):
                session_value = cookie.split('=')[1]
            elif cookie.startswith('aws-waf-token='):
                aws_waf_token_value = cookie.split('=')[1]
        
        if session_value and aws_waf_token_value:
            cookies = {
                'aws-waf-token': aws_waf_token_value,
                'session': session_value
            }
            
        task = fetch_data(site, params, account['proxy'], cookies, headers)
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    for account, result in zip(accounts, results):
        id = str(account['name'])
        cookies = str(account['cookies'])
        
        volume = fee = 0
        if result is None:
            continue           
            
        for fill_order in result:
            if fill_order["symbol"] != "USDT_USDC":
                volume += float(fill_order["quantity"]) * float(fill_order["price"])
                    
                if fill_order['side'] == "Bid":
                    fee += float(fill_order["fee"]) * float(fill_order['price'])
                else:
                    fee += float(fill_order['fee'])
        floated_volume = round(volume, 2)
        floated_fee = round(fee, 2)

        logger.info(f"{id:>9} | Total volume (without USDT_USDC pair): {floated_volume:>14} | Spent fee: {floated_fee:10}")

if __name__ == "__main__":
    asyncio.run(main())
