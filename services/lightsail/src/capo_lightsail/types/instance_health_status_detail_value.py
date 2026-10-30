"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthStatusDetailValue``."""

from typing import Literal, TypeAlias, cast

InstanceHealthStatusDetailValue: TypeAlias = Literal[
    "passed",
    "failed",
    "insufficient-data",
    "initializing",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthStatusDetailValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthStatusDetailValue:
    return cast(InstanceHealthStatusDetailValue, data)
