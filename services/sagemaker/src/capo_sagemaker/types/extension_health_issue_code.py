"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionHealthIssueCode``."""

from typing import Literal, TypeAlias, cast

ExtensionHealthIssueCode: TypeAlias = Literal[
    "InvalidConfiguration",
    "ConfigurationConflict",
    "AccessDenied",
    "ResourceNotFound",
    "DependencyUnreachable",
    "ExtensionUnhealthy",
    "InternalFailure",
    "Other",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionHealthIssueCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExtensionHealthIssueCode:
    return cast(ExtensionHealthIssueCode, data)
