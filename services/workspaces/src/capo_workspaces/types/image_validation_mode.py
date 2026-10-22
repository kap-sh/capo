"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageValidationMode``."""

from typing import Literal, TypeAlias, cast

ImageValidationMode: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "SERVICE_MANAGED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageValidationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageValidationMode:
    return cast(ImageValidationMode, data)
