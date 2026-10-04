"""Generated from Smithy shape ``com.amazonaws.sagemaker#DatabaseConfigurationRollbackStatus``."""

from typing import Literal, TypeAlias, cast

DatabaseConfigurationRollbackStatus: TypeAlias = Literal[
    "NotApplicable",
    "Reverted",
    "RevertFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseConfigurationRollbackStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseConfigurationRollbackStatus:
    return cast(DatabaseConfigurationRollbackStatus, data)
