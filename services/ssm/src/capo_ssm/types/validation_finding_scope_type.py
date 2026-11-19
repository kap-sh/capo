"""Generated from Smithy shape ``com.amazonaws.ssm#ValidationFindingScopeType``."""

from typing import Literal, TypeAlias, cast

ValidationFindingScopeType: TypeAlias = Literal[
    "azure:tenant",
    "azure:subscription",
    "gcp:organization",
    "gcp:project",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationFindingScopeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationFindingScopeType:
    return cast(ValidationFindingScopeType, data)
