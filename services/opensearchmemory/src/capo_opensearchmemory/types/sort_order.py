"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SortOrder``."""

from typing import Literal, TypeAlias, cast

"""<p>Sort direction for time-ordered listings.</p>"""
SortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SortOrder) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SortOrder:
    return cast(SortOrder, data)
