"""Generated from Smithy shape ``com.amazonaws.transfer#CommunicationMode``."""

from typing import Literal, TypeAlias, cast

CommunicationMode: TypeAlias = Literal[
    "CLIENT_TALK_FIRST",
    "SERVER_TALK_FIRST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommunicationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommunicationMode:
    return cast(CommunicationMode, data)
