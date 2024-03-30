
from backpack_lib.models.account_info import AccountInfo
from backpack_lib.models.custom_logger import logger
from backpack_lib.models.backpack import BackPack


async def get_all_volume(account_info: AccountInfo) -> float:
    backpack = BackPack(account_info)
    
    return await backpack.get_all_volume()

async def get_first_volume_and_fees(account_info: AccountInfo) -> float:
    backpack = BackPack(account_info)
    
    volume = await backpack.get_volume_for_first_season_first_phase()
    fees = await backpack.get_fees_before_end_of_first_phase()
    
    logger.info(
        f"{account_info.account_id:>9} | Before 18th March 2024: Total volume"
        f"{volume:>16} | Spent fee: {fees:10}"
    )

async def get_current_volume_and_fees(account_info: AccountInfo) -> float:
    backpack = BackPack(account_info)
    
    volume = await backpack.get_all_volume()
    fees = await backpack.get_fees_for_trades()
    
    logger.info(
        f"{account_info.account_id:>9} | For whole time: Total volume: "
        f"{volume:>16} | Spent fee: {fees:10}"
    )