from pathlib import Path

from dump_manager import DumpManager


class DefinitionDumpManager(DumpManager):
    pass

file = Path(Path.cwd() / "dumps" / "definition.csv")
level_manager = DefinitionDumpManager(file)
ind10 = level_manager.get_list_of_receive_ts()[0]
print(level_manager.get_dataframe_by_receive_ts(ind10))