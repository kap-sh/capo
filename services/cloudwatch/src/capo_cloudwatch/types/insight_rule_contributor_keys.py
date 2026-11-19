"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleContributorKeys``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_contributor_key

InsightRuleContributorKeys: TypeAlias = list[
    "capo_cloudwatch.types.insight_rule_contributor_key.InsightRuleContributorKey"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleContributorKeys, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> InsightRuleContributorKeys:
    out: InsightRuleContributorKeys = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: InsightRuleContributorKeys, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> InsightRuleContributorKeys:
    out: InsightRuleContributorKeys = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleContributorKeys) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> InsightRuleContributorKeys:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InsightRuleContributorKeys) -> list:
    return list(value)


def deserialize_cbor(data: list) -> InsightRuleContributorKeys:
    return [item for item in data if item is not None]
