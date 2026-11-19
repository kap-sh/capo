"""Generated from Smithy shape ``com.amazonaws.mgn#SourceServerArnsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.source_server_arn

SourceServerArnsFilter: TypeAlias = list[
    "capo_mgn.types.source_server_arn.SourceServerArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceServerArnsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> SourceServerArnsFilter:
    return [item for item in data if item is not None]
