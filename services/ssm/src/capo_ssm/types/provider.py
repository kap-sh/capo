"""Generated from Smithy shape ``com.amazonaws.ssm#Provider``."""

from typing import Literal, TypeAlias, cast

Provider: TypeAlias = Literal[
    "Azure",
    "GCP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Provider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Provider:
    return cast(Provider, data)
