"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.context_definition

ContextDefinitionList: TypeAlias = list[
    "capo_network_firewall.types.context_definition.ContextDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextDefinitionList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ContextDefinitionList:
    return [item for item in data if item is not None]
