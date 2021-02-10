import json
from pathlib import Path

import pytest

from valarpy import for_write, for_read, WriteNotEnabledError, UnsupportedOperationError

CONFIG_PATH = Path(__file__).parent / "resources" / "connection.json"
CONFIG_DATA = json.loads(CONFIG_PATH.read_text(encoding="utf8"))


class TestModel:
    def test_cannot_truncate(self):
        with for_write(CONFIG_DATA) as model:
            model.conn.enable_write()
            from valarpy.model import Refs

            with pytest.raises(UnsupportedOperationError):
                Refs.truncate_table()
            with pytest.raises(UnsupportedOperationError):
                Refs.drop_table()

    def test_write_disabled_by_default(self):
        with for_read(CONFIG_DATA):
            from valarpy.model import Refs

            ref = Refs(name="test_write_disabled_by_default")
            with pytest.raises(WriteNotEnabledError):
                ref.save()
            # transaction should commit
            assert "test_write_disabled_by_default" not in {r.name for r in Refs.select()}

    def test_write_enable_disable(self):
        with for_write(CONFIG_DATA) as model:
            model.conn.enable_write()
            from valarpy.model import Refs

            ref = Refs(name="test_write_enable_disable")
            ref.save()
            model.conn.disable_write()
            with pytest.raises(WriteNotEnabledError):
                ref.delete_instance()
            # transaction should commit
            assert "test_write_enable_disable" in {r.name for r in Refs.select()}
            model.conn.enable_write()
            ref.delete_instance()
            assert "test_write_enable_disable" not in {r.name for r in Refs.select()}


if __name__ == ["__main__"]:
    pytest.main()
