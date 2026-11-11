"""Generated from Smithy shape ``com.amazonaws.ssm#DHMCPermissionModel``."""

from typing import Literal, TypeAlias, cast

DHMCPermissionModel: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "SELF_MANAGED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DHMCPermissionModel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DHMCPermissionModel:
    return cast(DHMCPermissionModel, data)
