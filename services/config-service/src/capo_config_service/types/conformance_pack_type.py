"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackType``."""

from typing import Literal, TypeAlias, cast

ConformancePackType: TypeAlias = Literal[
    "CUSTOM",
    "MANAGED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConformancePackType:
    return cast(ConformancePackType, data)
