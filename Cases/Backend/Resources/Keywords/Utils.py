from robot.api import logger
from robot.api.deco import keyword, library


@library(scope="TEST", version="0.1", auto_keywords=False)
class Utils:

    @keyword
    def variable_type_should_be(self, type: str, variable: str | int) -> bool:
        match type:
            case 'str':
                if isinstance(variable, str):
                    logger.info(f"{variable} is {type}")
                    return True
            case 'int':
                if isinstance(variable, int):
                    logger.info(f"{variable} is {type}")
                    return True
            case _:
                logger.warn("Type not defined")
                raise ValueError("-99")
        logger.warn(f"{variable} is not {type}")
        raise TypeError("-99")
