class Api:
    def __init__(self, bearer_token: str, company_id: int, user_token: str = "", language: str = "ru-RU") -> None:
        self.company_id = company_id
        self.headers = {
            "Accept": "application/vnd.yclients.v2+json",
            "Accept-Language": language,
            "Authorization": f"Bearer {bearer_token}, User {user_token}",
            "Cache-Control": "no-cache",
        }

    async def get_user_token(self) -> str:
        ...
