"""Generated from Smithy shape ``com.amazonaws.dynamodb#OutputTypeEnum``."""

from typing import Literal, TypeAlias, cast

OutputTypeEnum: TypeAlias = Literal[
    "ERROR",
    "CONDITION_CHECK_FAILURE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OutputTypeEnum:
    return cast(OutputTypeEnum, data)
