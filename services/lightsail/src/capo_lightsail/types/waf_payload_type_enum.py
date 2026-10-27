"""Generated from Smithy shape ``com.amazonaws.lightsail#WafPayloadTypeEnum``."""

from typing import Literal, TypeAlias, cast

WafPayloadTypeEnum: TypeAlias = Literal[
    "JSON",
    "FORM_ENCODED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafPayloadTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WafPayloadTypeEnum:
    return cast(WafPayloadTypeEnum, data)
