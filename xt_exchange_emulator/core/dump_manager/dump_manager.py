from abc import ABC
import logging
from pathlib import Path

from typing import Sequence

import pandas as pd

class AbstractDumpManager(ABC):

    def get_list_of_receive_ts(self) -> Sequence: # type: ignore
        """
        Метод, который возвращает список ключей receive_ts

        Returns:
            Sequence: список ключей receive_ts
        """
        pass

    def get_dataframe_by_receive_ts(self, receive_ts: int) -> pd.DataFrame | None:
        """
        Метод, который возвращает dataframe по ключу receive_ts

        Args:
            receive_ts (int): ключ, по которому нужно вернуть dataframe

        Returns:
            pd.DataFrame | None: возвращает dataframe, если он есть, иначе None   
        """
        pass


class DumpManager(AbstractDumpManager):
    
    def __init__(self, filename: Path, delimeter: str = ";", group_by: str = "receive_ts") -> None:
        """
        Конструктор класса DumpManager

        Args:
            filename (Path): путь к файлу, который нужно загрузить
            delimeter (str, optional): разделитель в файле. Defaults to ";".
            group_by (str, optional): по какому столбцу нужно сгруппировать данные. Defaults to "receive_ts".

        Returns:
            None        
        """
        groups = pd.read_csv(filename, delimiter=delimeter).groupby(group_by)

        self.receive_ts_lists = [index for index, group in groups]
        self.message_packs = dict(tuple(groups))
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_list_of_receive_ts(self) -> Sequence:
        """
        Метод, который возвращает список ключей receive_ts

        Returns:
            Sequence: список ключей receive_ts
        """
        self.logger.debug("Запрос списка ключей receive_ts")
        return self.receive_ts_lists


    def get_dataframe_by_receive_ts(self, receive_ts: int) -> pd.DataFrame | None:
        """
        Метод, который возвращает dataframe по ключу receive_ts

        Args:
            receive_ts (int): ключ, по которому нужно вернуть dataframe

        Returns:
            pd.DataFrame | None: возвращает dataframe, если он есть, иначе None   
        """
        self.logger.debug(f"Запрос dataframe по ключу receive_ts: {receive_ts}")
        return self.message_packs.get(receive_ts)
