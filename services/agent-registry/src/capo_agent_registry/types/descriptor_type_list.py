"""Generated from Smithy shape ``com.amazonaws.agentregistry#DescriptorTypeList``."""

from typing import TypeAlias

DescriptorTypeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DescriptorTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> DescriptorTypeList:
    return [item for item in data if item is not None]
