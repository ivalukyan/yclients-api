import aiohttp

from tools.logger import log


class AuthAPI:
    def __init__(self, bearer_token: str, user_token: str, company_id: int):
        self.company_id = company_id
        self.headers = {
            "Accept": "application/vnd.yclients.v2+json",
            "Authorization": f"Bearer {bearer_token}, User {user_token}",
            "Cache-Control": "no-cache",
        }

    async def get_user_token(self, login: str, password: str) -> str:
        """Get user token
        """
        url = "https://api.yclients.com/api/v1/auth"
        params = {
            "login": login,
            "password": password,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers, params=params) as response:
                res = await response.text()
        if res["success"]:
            log.info(f"Success getting user token for user {login}")
            return res["data"]["user_token"]
        raise Exception(f"Error getting user token for user {login}")
