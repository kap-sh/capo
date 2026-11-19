"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.ip_set
    import capo_network_firewall.types.rule_variable_name

IPSets: TypeAlias = dict[
    "capo_network_firewall.types.rule_variable_name.RuleVariableName",
    "capo_network_firewall.types.ip_set.IPSet",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: IPSets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.ip_set

        out[key] = capo_network_firewall.types.ip_set.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSets:
    out: IPSets = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.ip_set

        out[key] = capo_network_firewall.types.ip_set.deserialize_aws_json_1_0(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: IPSets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.ip_set

        out[key] = capo_network_firewall.types.ip_set.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> IPSets:
    out: IPSets = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.ip_set

        out[key] = capo_network_firewall.types.ip_set.deserialize_cbor(value)
    return out
