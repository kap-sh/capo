"""Generated from Smithy shape ``com.amazonaws.neptunedata#RebuildIdList``."""

from typing import TypeAlias

RebuildIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RebuildIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> RebuildIdList:
    return [item for item in data if item is not None]
