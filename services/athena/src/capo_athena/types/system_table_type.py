"""Generated from Smithy shape ``com.amazonaws.athena#SystemTableType``."""

from typing import Literal, TypeAlias, cast

SystemTableType: TypeAlias = Literal["QUERY_EXECUTIONS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTableType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SystemTableType:
    return cast(SystemTableType, data)
