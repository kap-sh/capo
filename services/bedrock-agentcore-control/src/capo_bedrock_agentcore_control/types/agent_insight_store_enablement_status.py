"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentInsightStoreEnablementStatus``."""

from typing import Literal, TypeAlias, cast

AgentInsightStoreEnablementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightStoreEnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentInsightStoreEnablementStatus:
    return cast(AgentInsightStoreEnablementStatus, data)
