from datetime import datetime
import aiohttp

from backpack_lib.models.account_info import AccountInfo
from backpack_lib.models.custom_logger import logger


class BackPack:
    VOLUME_URL = 'https://api.backpack.exchange/wapi/v1/statistics/user/volume/quote/USDC'
    ORDER_HISTORY_URL = 'https://api.eu.backpack.exchange/wapi/v1/history/fills'

    def __init__(
        self,
        account_info: AccountInfo
    ):
        self.account_id = account_info.account_id
        self.cookies = account_info.cookies
        self.proxy = account_info.proxy

        self._init_headers()
        self._add_cookies(self.cookies)

    def _init_headers(self):
        self.headers = {
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

    def _add_cookies(self, cookies: str):
        self.headers['cookie'] = cookies

    async def get_all_volume(self) -> float:
        params = {
            'interval': 'seasonOnePhaseTwo'
        }

        response = await self._make_request(url=self.VOLUME_URL, params=params)
        volume = float(response[0]['volume'])
        volume = round(volume, 2)

        return volume

    async def get_fees_before_end_of_first_phase(self) -> float:
        params = {
            'limit': '1000000000'
        }

        response = await self._make_request(url=self.ORDER_HISTORY_URL, params=params)
        fee = 0
        snapshot_time = datetime(2024, 3, 18, 23, 0)

        for fill_order in response:

            if fill_order["symbol"] == "USDT_USDC":
                continue

            fill_order_timestamp = (
                datetime.strptime(
                    fill_order["timestamp"], "%Y-%m-%dT%H:%M:%S.%f")
                if '.' in fill_order["timestamp"]
                else datetime.strptime(fill_order["timestamp"], "%Y-%m-%dT%H:%M:%S")
            )

            if fill_order_timestamp <= snapshot_time:
                if fill_order['feeSymbol'] != "USDC":
                    fee += float(fill_order["fee"]) * \
                        float(fill_order['price'])
                else:
                    fee += float(fill_order['fee'])

        floated_fee = round(fee, 2)
        return floated_fee

    async def get_volume_for_first_season_first_phase(self) -> float:
        params = {
            'interval': 'seasonOnePhaseOne'
        }

        response = await self._make_request(url=self.VOLUME_URL, params=params)
        volume = float(response[0]['volume'])
        volume = round(volume, 2)

        return volume

    async def get_fees_for_trades(self) -> float:
        params = {
            'limit': '2000000000'
        }

        response = await self._make_request(url=self.ORDER_HISTORY_URL, params=params)
        fee = 0

        for fill_order in response:
            if fill_order["symbol"] == "USDT_USDC":
                continue

            if fill_order['feeSymbol'] != "USDC":
                fee += float(fill_order["fee"]) * float(fill_order['price'])
            else:
                fee += float(fill_order['fee'])
        floated_fee = round(fee, 2)

        return floated_fee

    async def _make_request(
        self,
        method: str = "GET",
        url: str = "",
        params: dict[str, any] = {}
    ):
        try:
            async with aiohttp.ClientSession() as session:
                request = await session.request(
                    method=method,
                    url=url,
                    params=params,
                    headers=self.headers,
                    proxy=self.proxy,
                )

                if request.status > 201:
                    logger.error(f"Not valid request: {request.text}")
                return await request.json()

        except Exception as e:
            logger.error(f"An error occurred: {e}")
