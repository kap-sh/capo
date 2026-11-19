"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SummaryRuleOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.summary_rule_option

SummaryRuleOptions: TypeAlias = list[
    "capo_network_firewall.types.summary_rule_option.SummaryRuleOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryRuleOptions) -> list:
    import capo_network_firewall.types.summary_rule_option

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.summary_rule_option.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SummaryRuleOptions:
    import capo_network_firewall.types.summary_rule_option

    out: SummaryRuleOptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.summary_rule_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SummaryRuleOptions) -> list:
    import capo_network_firewall.types.summary_rule_option

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.summary_rule_option.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SummaryRuleOptions:
    import capo_network_firewall.types.summary_rule_option

    out: SummaryRuleOptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.summary_rule_option.deserialize_cbor(item)
        )
    return out
