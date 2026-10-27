"""Generated from Smithy shape ``com.amazonaws.lightsail#WafInspectionLevelEnum``."""

from typing import Literal, TypeAlias, cast

WafInspectionLevelEnum: TypeAlias = Literal[
    "COMMON",
    "TARGETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafInspectionLevelEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WafInspectionLevelEnum:
    return cast(WafInspectionLevelEnum, data)
