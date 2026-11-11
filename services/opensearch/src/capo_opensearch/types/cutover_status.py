"""Generated from Smithy shape ``com.amazonaws.opensearch#CutoverStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a cutover.</p>"""
CutoverStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: CutoverStatus) -> str:
    return value


def deserialize_json(data: str) -> CutoverStatus:
    return cast(CutoverStatus, data)
