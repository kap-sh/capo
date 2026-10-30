"""Generated from Smithy shape ``com.amazonaws.neptunedata#RebuildStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Indicates the current state of a rebuild operation.</p>"""
RebuildStatus: TypeAlias = Literal[
    "PREPARING",
    "REBUILDING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
    "CANCELLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RebuildStatus) -> str:
    return value


def deserialize_json(data: str) -> RebuildStatus:
    return cast(RebuildStatus, data)
