"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PublicDomainNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.public_domain_name

PublicDomainNameList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.public_domain_name.PublicDomainName"
]


# --- restJson1 ser/de ---
def serialize_json(value: PublicDomainNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> PublicDomainNameList:
    return [item for item in data if item is not None]
