import asyncio
import sys
import time
from typing import List

from questionary import (
    questionary,
    Choice
)

from backpack_lib.models.account_info import AccountInfo
from backpack_lib.models.custom_logger import logger
from backpack_lib.utils.config import (
    ACCOUNT_NAMES, COOKIES, PROXIES
)
from backpack_lib.utils.utils import format_output
from user_data.settings.settings import IS_ACCOUNT_NAMES
from user_data.settings.modules_settings import (
    get_all_volume_and_fees,
    get_first_volume,
)


def greetings():
    name_label = "========= BackPack Volume and Fee Checker ========="
    brand_label = "========== Author: M A K E D 0 N 1 A N =========="
    telegram = "======== https://t.me/crypto_maked0n1an ========"

    print("")
    format_output(name_label)
    format_output(brand_label)
    format_output(telegram)


def end_of_work():
    exit_label = "========= The bot has ended it's work! ========="
    format_output(exit_label)
    sys.exit()


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


def get_accounts():
    accounts: List[AccountInfo] = []

    if IS_ACCOUNT_NAMES:
        for account_id, cookies in zip(ACCOUNT_NAMES, COOKIES):
            account = AccountInfo(
                account_id=account_id,
                cookies=cookies
            )
            accounts.append(account)
    else:
        for account_id, cookies in enumerate(COOKIES, start=1):
            account = AccountInfo(
                account_id=account_id,
                cookies=cookies
            )
            accounts.append(account)

    if PROXIES:
        for account, proxy in zip(accounts, PROXIES * len(accounts)):
            account.proxy = proxy

    return accounts


def get_module():
    result = questionary.select(
        "Select a method to get started",
        choices=[
            Choice("1) Get volume before 18th March 2024", get_first_volume),
            Choice("2) Get current volume and spent fees", get_all_volume_and_fees),
            Choice("3) Exit", "exit"),
        ],
        qmark="⚙️ ",
        pointer="✅ "
    ).ask()
    if result == "exit":
        exit_label = "========= Exited ========="
        format_output(exit_label)
        sys.exit()

    return result


def measure_time_for_all_work(start_time: float):
    end_time = round(time.time() - start_time, 2)
    seconds = round(end_time % 60, 2)
    minutes = int(end_time // 60) if end_time > 60 else 0
    hours = int(end_time // 3600) if end_time > 3600 else 0

    logger.info(
        (
            f"Spent time: "
            f"{hours} hours {minutes} minutes {seconds} seconds"
        )
    )


async def main(module):
    accounts = get_accounts()

    tasks = []
    for account in accounts:
        task = module(account)
        tasks.append(task)

    await asyncio.gather(*tasks)
        
        # id = str(account['name'])
        # cookies = str(account['cookies'])

        # volume = fee = 0
        # if result is None:
        #     continue

        # for fill_order in result:
        #     if fill_order["symbol"] != "USDT_USDC":
        #         volume += float(fill_order["quantity"]) * \
        #             float(fill_order["price"])

        #         if fill_order['side'] == "Bid":
        #             fee += float(fill_order["fee"]) * \
        #                 float(fill_order['price'])
        #         else:
        #             fee += float(fill_order['fee'])
        # floated_volume = round(volume, 2)
        # floated_fee = round(fee, 2)

        # logger.info(
        #     f"{id:>9} | Total volume (without USDT_USDC pair): {floated_volume:>14} | Spent fee: {floated_fee:10}")

if __name__ == "__main__":
    greetings()

    if not is_bot_setuped_to_start():
        exit_label = "========= The bot has ended it's work! ========="
        format_output(exit_label)
        sys.exit()

    module_data = get_module()

    start_time = time.time()

    logger.info("The bot started to measure time for all work")

    asyncio.run(main(module_data))

    measure_time_for_all_work(start_time)
    end_of_work()
