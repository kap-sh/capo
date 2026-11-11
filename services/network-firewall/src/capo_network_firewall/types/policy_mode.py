"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PolicyMode``."""

from typing import Literal, TypeAlias, cast

PolicyMode: TypeAlias = Literal[
    "ENFORCE",
    "MONITOR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PolicyMode:
    return cast(PolicyMode, data)
