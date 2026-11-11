"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionStatus``."""

from typing import Literal, TypeAlias, cast

ExtensionStatus: TypeAlias = Literal[
    "Creating",
    "Active",
    "CreateFailed",
    "Updating",
    "Deleting",
    "DeleteFailed",
    "Degraded",
    "UpdateFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExtensionStatus:
    return cast(ExtensionStatus, data)
