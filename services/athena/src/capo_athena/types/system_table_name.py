"""Generated from Smithy shape ``com.amazonaws.athena#SystemTableName``."""

from typing import Literal, TypeAlias, cast

SystemTableName: TypeAlias = Literal["ALL",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTableName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SystemTableName:
    return cast(SystemTableName, data)
