"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ClientTypeType``."""

from typing import Literal, TypeAlias, cast

ClientTypeType: TypeAlias = Literal[
    "REGULAR",
    "DCR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientTypeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientTypeType:
    return cast(ClientTypeType, data)
