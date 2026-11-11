"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.domain_name

DomainList: TypeAlias = list["capo_bedrock_agentcore.types.domain_name.DomainName"]


# --- restJson1 ser/de ---
def serialize_json(value: DomainList) -> list:
    return list(value)


def deserialize_json(data: list) -> DomainList:
    return [item for item in data if item is not None]
