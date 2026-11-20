"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemorySortField``."""

from typing import Literal, TypeAlias, cast

"""<p>The timestamp that <code>ListMemories</code> sorts by.</p>"""
MemorySortField: TypeAlias = Literal[
    "CREATED_AT",
    "UPDATED_AT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemorySortField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MemorySortField:
    return cast(MemorySortField, data)
