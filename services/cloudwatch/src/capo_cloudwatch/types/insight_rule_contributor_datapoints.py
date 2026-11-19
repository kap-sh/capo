"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleContributorDatapoints``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

InsightRuleContributorDatapoints: TypeAlias = list[
    "capo_cloudwatch.types.insight_rule_contributor_datapoint.InsightRuleContributorDatapoint"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleContributorDatapoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.insight_rule_contributor_datapoint.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InsightRuleContributorDatapoints:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

    out: InsightRuleContributorDatapoints = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.insight_rule_contributor_datapoint.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: InsightRuleContributorDatapoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.insight_rule_contributor_datapoint.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> InsightRuleContributorDatapoints:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

    out: InsightRuleContributorDatapoints = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.insight_rule_contributor_datapoint.deserialize_query(
                child
            )
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleContributorDatapoints) -> list:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.insight_rule_contributor_datapoint.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InsightRuleContributorDatapoints:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

    out: InsightRuleContributorDatapoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.insight_rule_contributor_datapoint.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InsightRuleContributorDatapoints) -> list:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.insight_rule_contributor_datapoint.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> InsightRuleContributorDatapoints:
    import capo_cloudwatch.types.insight_rule_contributor_datapoint

    out: InsightRuleContributorDatapoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.insight_rule_contributor_datapoint.deserialize_cbor(
                item
            )
        )
    return out
