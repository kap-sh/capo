"""Generated from Smithy shape ``com.amazonaws.fms#DnsRuleGroupPriorities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.dns_rule_group_priority

DnsRuleGroupPriorities: TypeAlias = list[
    "capo_fms.types.dns_rule_group_priority.DnsRuleGroupPriority"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRuleGroupPriorities) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsRuleGroupPriorities:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DnsRuleGroupPriorities) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DnsRuleGroupPriorities:
    return [item for item in data if item is not None]
