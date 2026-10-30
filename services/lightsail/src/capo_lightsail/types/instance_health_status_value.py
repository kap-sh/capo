"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthStatusValue``."""

from typing import Literal, TypeAlias, cast

InstanceHealthStatusValue: TypeAlias = Literal[
    "ok",
    "impaired",
    "initializing",
    "insufficient-data",
    "not-applicable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthStatusValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthStatusValue:
    return cast(InstanceHealthStatusValue, data)
