"""Generated from Smithy shape ``com.amazonaws.neptunedata#WriteBufferSize``."""

from typing import Literal, TypeAlias, cast

"""<p>Controls the buffer size used during an index rebuild to track concurrent write operations. Larger values allow the rebuild to tolerate heavier concurrent write traffic.</p>"""
WriteBufferSize: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: WriteBufferSize) -> str:
    return value


def deserialize_json(data: str) -> WriteBufferSize:
    return cast(WriteBufferSize, data)
