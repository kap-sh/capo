"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemoryType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a memory. Matches the type of the memory strategy that produced it.</p>"""
MemoryType: TypeAlias = Literal[
    "SEMANTIC",
    "SUMMARY",
    "CUSTOM",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemoryType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MemoryType:
    return cast(MemoryType, data)
