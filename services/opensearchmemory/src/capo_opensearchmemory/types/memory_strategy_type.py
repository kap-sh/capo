"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemoryStrategyType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of memory a strategy extracts.</p>"""
MemoryStrategyType: TypeAlias = Literal[
    "SEMANTIC",
    "SUMMARY",
    "CUSTOM",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemoryStrategyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MemoryStrategyType:
    return cast(MemoryStrategyType, data)
