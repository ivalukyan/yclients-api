"""Module for API
"""

import aiohttp

from .__init__ import log
from typing import List


class Api:
    def __init__(self, bearer_token: str, company_id: int, user_token: str = "", language: str = "ru-RU") -> None:
        self.company_id = company_id
        self.headers = {
            "Accept": "application/vnd.yclients.v2+json",
            "Accept-Language": language,
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
            async with session.get(
                url=url,
                headers=self.headers,
                params=params,
            ) as response:
                response = await response.text()
        if response["success"]:
            log.info(
                f"Successfully got user token for user {login}"
            )
            return response["data"]["user_token"]
        raise Exception(f"Error getting user token for user {login}")

    async def get_book_services(self) -> None:
        """Book services
        """
        url = f"https://api.yclients.com/api/v1/book_services/{self.company_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                headers=self.headers,
            ) as response:
                response = await response.text()

        if response["success"]:
            log.info("Successfully booked services")
            return response["data"]["services"]
        raise Exception("Error booking services")

    async def get_book_dates(self, services_ids: List[int], staff_id: int) -> List[dict]:
        """Book dates
        """
        url = f"https://api.yclients.com/api/v1/book_dates/{self.company_id}"
        params = {
            "services_ids": services_ids,
            "staff_id": staff_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                headers=self.headers,
                params=params,
            ) as response:
                response = await response.text()
        if response["success"]:
            log.info(
                f"Successfully booked dates for services {services_ids}"
            )
            return response["data"]["booking_dates"]
        raise Exception("Error booking dates")

    async def get_staff(self, service_id: int) -> List[dict]:
        """Get staff function
        """
        url = f"https://api.yclients.com/api/v1/company/{self.company_id}/services/{service_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                headers=self.headers,
            ) as response:
                response = await response.text()
        if response["success"]:
            log.info("Successfully got staff")
            return response["data"]["staff"]
        raise Exception("Error getting staff")

    async def get_book_staff(self) -> List[dict]:
        """Get book staff function
        """
        url = f"https://api.yclients.com/api/v1/book_staff/{self.company_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as response:
                response = await response.text()
        if response["success"]:
            log.info("Successfully get booked staff")
            return response["data"]
        raise Exception("Error getting booked staff")

    async def get_book_category(self) -> List[dict]:
        """Get book category function
        """
        url = f"https://api.yclients.com/api/v1/book_services/{self.company_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as response:
                response = await response.text()
        if response["success"]:
            log.info("Successfully get booked category")
            return response["data"]["category"]
        raise Exception("Error getting booked category")

    async def get_book_times(self, staff_id: int, date: str) -> List[dict]:
        """Function for getting book times
        """
        url = f"https://api.yclients.com/api/v1/book_times/{self.company_id}/{staff_id}/{date}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as response:
                response = await response.text()
        if response["success"]:
            log.info("Successfully got booked times")
            return response["data"]
        raise Exception("Error getting booked times")
