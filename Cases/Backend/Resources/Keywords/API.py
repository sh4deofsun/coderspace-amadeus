from robot.api import logger
from robot.api.deco import keyword, library
# import json
import requests


@library(scope="TEST", version="0.1", auto_keywords=False)
class API:
    enpoints = {"TEST": "https://flights-api.buraky.workers.dev/"}

    @keyword
    def call_api(self,
                 enviroment: str,
                 method="GET",
                 expected_status_code=200) -> dict:
        if enviroment.upper() in self.enpoints.keys():
            endpoint = self.enpoints[enviroment.upper()]
        elif enviroment.startswith("http"):
            endpoint = enviroment
            logger.info(f"Custom Enviroment: {enviroment}")
        else:
            logger.warn(f"Incorrect Enviroment: {enviroment}")
            raise ValueError("-99")

        if method == "GET":
            response = requests.get(url=endpoint)
            logger.info(f"GET Request send to: {endpoint}")
        else:
            logger.warn(f"Unknown Method: {method}")
            raise ValueError("-99")

        if response.status_code == expected_status_code:
            logger.info(f"Response: {response.text}")
            return {
                "ResponseData": response.json(),
                "ResponseHeader": response.headers
            }
        else:
            logger.warn(f"Unexpected Status Code: {response.status_code}")
            raise ValueError("-99")
