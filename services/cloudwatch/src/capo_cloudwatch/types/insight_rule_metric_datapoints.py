"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleMetricDatapoints``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

InsightRuleMetricDatapoints: TypeAlias = list[
    "capo_cloudwatch.types.insight_rule_metric_datapoint.InsightRuleMetricDatapoint"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleMetricDatapoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.insight_rule_metric_datapoint.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InsightRuleMetricDatapoints:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

    out: InsightRuleMetricDatapoints = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.insight_rule_metric_datapoint.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: InsightRuleMetricDatapoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.insight_rule_metric_datapoint.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InsightRuleMetricDatapoints:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

    out: InsightRuleMetricDatapoints = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.insight_rule_metric_datapoint.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleMetricDatapoints) -> list:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.insight_rule_metric_datapoint.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InsightRuleMetricDatapoints:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

    out: InsightRuleMetricDatapoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.insight_rule_metric_datapoint.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InsightRuleMetricDatapoints) -> list:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.insight_rule_metric_datapoint.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> InsightRuleMetricDatapoints:
    import capo_cloudwatch.types.insight_rule_metric_datapoint

    out: InsightRuleMetricDatapoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.insight_rule_metric_datapoint.deserialize_cbor(item)
        )
    return out
