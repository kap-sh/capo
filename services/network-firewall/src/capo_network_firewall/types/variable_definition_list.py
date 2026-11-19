"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VariableDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.variable_definition

VariableDefinitionList: TypeAlias = list[
    "capo_network_firewall.types.variable_definition.VariableDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VariableDefinitionList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VariableDefinitionList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VariableDefinitionList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> VariableDefinitionList:
    return [item for item in data if item is not None]
