import aiohttp

from tools.logger import log
from auth.auth_api import AuthAPI
from online_models import ParamsRecords


class OnlineAPI(AuthAPI):
    def __init__(self):
        super().__init__()

    async def get_sessetings(self, form_id: int) -> list[dict]:
        """Get settings for form
        """
        url = f"https://api.yclients.com/api/v1/bookform/{form_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                headers=self.headers,
            ) as response:
                res = await response.text()
        if res["success"]:
            log.info("Success getting settings for form")
            return res["data"]["steps"]
        raise Exception("Error getting settings for form")

    async def get_languages(self, lang_code: str = "ru-RU") -> dict[str, dict]:
        """Get params for language
        """
        url = f"https://api.yclients.com/api/v1/i18n/{lang_code}"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                headers=self.headers,
            ) as response:
                res = await response.text()
        if res["success"]:
            log.info("Success getting params for language")
            return res
        raise Exception("Error getting params for language")

    async def send_sms_for_ferification(self, phone: str, fullname: str = "name") -> dict:
        """Send sms for verification
        """
        url = f"https://api.yclients.com/api/v1/book_code/{self.company_id}"
        params = {
            "phone": phone,
        }
        if fullname:
            params = {
                "phone": phone,
                "fullname": fullname,
            }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=url,
                headers=self.headers,
                params=params
            ) as response:
                res = await response.text()

            if res is not None:
                log.info("Success sending sms for verification")
                return res
            raise Exception("Error sending sms for verification")

    async def check_params_record(self, appointments: list[ParamsRecords]) -> str:
        """Check params for record
        """
        url = f"https://api.yclients.com/api/v1/book_check/{self.company_id}"
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=url,
                headers=self.headers,
                params={
                    "appointments": appointments,
                }
            ) as response:
                res = await response.text()
        if res["success"]:
            log.info("Success checking params for record")
            return res["meta"]["message"]
        raise Exception("Error checking params for record")
