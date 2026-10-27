"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RegionScope``."""

from typing import Literal, TypeAlias, cast

RegionScope: TypeAlias = Literal[
    "CURRENT_REGION",
    "ALL_REGIONS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegionScope:
    return cast(RegionScope, data)
