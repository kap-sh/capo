"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ActionScope``."""

from typing import Literal, TypeAlias, cast

ActionScope: TypeAlias = Literal[
    "FLOW",
    "TX",
    "HOOK",
    "PACKET",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionScope) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActionScope:
    return cast(ActionScope, data)
