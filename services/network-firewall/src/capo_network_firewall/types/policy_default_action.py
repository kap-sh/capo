"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PolicyDefaultAction``."""

from typing import Literal, TypeAlias, cast

PolicyDefaultAction: TypeAlias = Literal[
    "DROP",
    "ACCEPT",
    "REJECT",
    "ALERT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyDefaultAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PolicyDefaultAction:
    return cast(PolicyDefaultAction, data)
