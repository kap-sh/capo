"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.context_set
    import capo_network_firewall.types.rule_variable_name

ContextSets: TypeAlias = dict[
    "capo_network_firewall.types.rule_variable_name.RuleVariableName",
    "capo_network_firewall.types.context_set.ContextSet",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ContextSets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.context_set

        out[key] = capo_network_firewall.types.context_set.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> ContextSets:
    out: ContextSets = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.context_set

        out[key] = capo_network_firewall.types.context_set.deserialize_aws_json_1_0(
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ContextSets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.context_set

        out[key] = capo_network_firewall.types.context_set.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> ContextSets:
    out: ContextSets = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.context_set

        out[key] = capo_network_firewall.types.context_set.deserialize_cbor(value)
    return out
