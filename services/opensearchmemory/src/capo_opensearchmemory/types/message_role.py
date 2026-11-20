"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MessageRole``."""

from typing import Literal, TypeAlias, cast

"""<p>The author of a turn.</p>"""
MessageRole: TypeAlias = Literal[
    "USER",
    "ASSISTANT",
    "SYSTEM",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageRole) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MessageRole:
    return cast(MessageRole, data)
