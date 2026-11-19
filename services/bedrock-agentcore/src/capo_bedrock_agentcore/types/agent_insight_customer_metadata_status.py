"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentInsightCustomerMetadataStatus``."""

from typing import Literal, TypeAlias, cast

"""Whether customer-encrypted metadata is available for an Agent Insight."""
AgentInsightCustomerMetadataStatus: TypeAlias = Literal[
    "AVAILABLE",
    "CUSTOMER_KEY_UNAVAILABLE",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightCustomerMetadataStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentInsightCustomerMetadataStatus:
    return cast(AgentInsightCustomerMetadataStatus, data)
