from pathlib import Path

from dump_manager import DumpManager


class LevelPairDumpManager(DumpManager):
    pass

file = Path(Path.cwd() / "dumps" / "level_pair.csv")
level_manager = LevelPairDumpManager(file)
ind10 = level_manager.get_list_of_receive_ts()[10]
print(level_manager.get_dataframe_by_receive_ts(ind10))