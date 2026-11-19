"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.rule_group_metadata

RuleGroups: TypeAlias = list[
    "capo_network_firewall.types.rule_group_metadata.RuleGroupMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleGroups) -> list:
    import capo_network_firewall.types.rule_group_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.rule_group_metadata.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RuleGroups:
    import capo_network_firewall.types.rule_group_metadata

    out: RuleGroups = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.rule_group_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleGroups) -> list:
    import capo_network_firewall.types.rule_group_metadata

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.rule_group_metadata.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RuleGroups:
    import capo_network_firewall.types.rule_group_metadata

    out: RuleGroups = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.rule_group_metadata.deserialize_cbor(item)
        )
    return out
