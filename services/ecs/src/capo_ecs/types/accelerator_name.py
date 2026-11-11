"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorName``."""

from typing import Literal, TypeAlias, cast

AcceleratorName: TypeAlias = Literal[
    "a100",
    "inferentia",
    "k520",
    "k80",
    "m60",
    "radeon-pro-v520",
    "t4",
    "vu9p",
    "v100",
    "a10g",
    "h100",
    "t4g",
    "l40s",
    "l4",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceleratorName:
    return cast(AcceleratorName, data)
