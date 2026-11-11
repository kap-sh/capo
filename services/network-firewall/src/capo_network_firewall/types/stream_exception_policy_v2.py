"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StreamExceptionPolicyV2``."""

from typing import Literal, TypeAlias, cast

StreamExceptionPolicyV2: TypeAlias = Literal[
    "DROP",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamExceptionPolicyV2) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StreamExceptionPolicyV2:
    return cast(StreamExceptionPolicyV2, data)
