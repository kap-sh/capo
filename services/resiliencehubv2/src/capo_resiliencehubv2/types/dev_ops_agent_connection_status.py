"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DevOpsAgentConnectionStatus``."""

from typing import Literal, TypeAlias, cast

DevOpsAgentConnectionStatus: TypeAlias = Literal[
    "CONNECTING",
    "CONNECTED",
    "DISCONNECTED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DevOpsAgentConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> DevOpsAgentConnectionStatus:
    return cast(DevOpsAgentConnectionStatus, data)
