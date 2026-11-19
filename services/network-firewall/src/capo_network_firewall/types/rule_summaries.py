"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.rule_summary

RuleSummaries: TypeAlias = list["capo_network_firewall.types.rule_summary.RuleSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleSummaries) -> list:
    import capo_network_firewall.types.rule_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.rule_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RuleSummaries:
    import capo_network_firewall.types.rule_summary

    out: RuleSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.rule_summary.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleSummaries) -> list:
    import capo_network_firewall.types.rule_summary

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.rule_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RuleSummaries:
    import capo_network_firewall.types.rule_summary

    out: RuleSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.rule_summary.deserialize_cbor(item))
    return out
