"""Generated from Smithy shape ``com.amazonaws.devopsagent#IncludedData``."""

from typing import Literal, TypeAlias, cast

"""<p>How much data to include in the response. Defaults to ALL_DATA.</p>"""
IncludedData: TypeAlias = Literal[
    "METADATA_ONLY",
    "ALL_DATA",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludedData) -> str:
    return value


def deserialize_json(data: str) -> IncludedData:
    return cast(IncludedData, data)
