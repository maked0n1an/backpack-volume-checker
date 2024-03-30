class AccountInfo:
    def __init__(
        self,
        account_id: str | int,
        cookies: str,
        proxy: str | None = None,
    ) -> None:
        self.account_id = account_id
        self.cookies = cookies
        self.proxy = proxy
