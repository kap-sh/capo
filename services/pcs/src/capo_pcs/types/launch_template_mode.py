"""Generated from Smithy shape ``com.amazonaws.pcs#LaunchTemplateMode``."""

from typing import Literal, TypeAlias, cast

LaunchTemplateMode: TypeAlias = Literal[
    "CUSTOM",
    "MANAGED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LaunchTemplateMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LaunchTemplateMode:
    return cast(LaunchTemplateMode, data)
