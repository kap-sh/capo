"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentInsightStoreStatus``."""

from typing import Literal, TypeAlias, cast

AgentInsightStoreStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATING",
    "INACTIVE",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightStoreStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentInsightStoreStatus:
    return cast(AgentInsightStoreStatus, data)
