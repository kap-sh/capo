"""Generated from Smithy shape ``com.amazonaws.agentregistry#RegistryRecordFilterName``."""

from typing import Literal, TypeAlias, cast

"""<p> The attribute to filter registry records on.</p>"""
RegistryRecordFilterName: TypeAlias = Literal[
    "recordType",
    "descriptorType",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordFilterName) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordFilterName:
    return cast(RegistryRecordFilterName, data)
