"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthStatusDetailName``."""

from typing import Literal, TypeAlias, cast

InstanceHealthStatusDetailName: TypeAlias = Literal["reachability",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthStatusDetailName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthStatusDetailName:
    return cast(InstanceHealthStatusDetailName, data)
