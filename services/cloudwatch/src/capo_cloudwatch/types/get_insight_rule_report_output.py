"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetInsightRuleReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_aggregation_statistic
    import capo_cloudwatch.types.insight_rule_contributor_key_labels
    import capo_cloudwatch.types.insight_rule_contributors
    import capo_cloudwatch.types.insight_rule_metric_datapoints
    import capo_cloudwatch.types.insight_rule_unbound_double
    import capo_cloudwatch.types.insight_rule_unbound_long


class GetInsightRuleReportOutput(TypedDict, closed=True):
    key_labels: NotRequired[
        "capo_cloudwatch.types.insight_rule_contributor_key_labels.InsightRuleContributorKeyLabels"
    ]
    """<p>An array of the strings used as the keys for this rule. The keys are the dimensions used to classify contributors. If the rule contains more than one key, then each unique combination of values for the keys is counted as a unique contributor.</p>"""
    aggregation_statistic: NotRequired[
        "capo_cloudwatch.types.insight_rule_aggregation_statistic.InsightRuleAggregationStatistic"
    ]
    """<p>Specifies whether this rule aggregates contributor data by COUNT or SUM.</p>"""
    aggregate_value: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The sum of the values from all individual contributors that match the rule.</p>"""
    approximate_unique_count: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_long.InsightRuleUnboundLong"
    ]
    """<p>An approximate count of the unique contributors found by this rule in this time period.</p>"""
    contributors: NotRequired[
        "capo_cloudwatch.types.insight_rule_contributors.InsightRuleContributors"
    ]
    """<p>An array of the unique contributors found by this rule in this time period. If the rule contains multiple keys, each combination of values for the keys counts as a unique contributor.</p>"""
    metric_datapoints: NotRequired[
        "capo_cloudwatch.types.insight_rule_metric_datapoints.InsightRuleMetricDatapoints"
    ]
    """<p>A time series of metric data points that matches the time period in the rule request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetInsightRuleReportOutput) -> dict:
    out: dict = {}
    if "key_labels" in value:
        import capo_cloudwatch.types.insight_rule_contributor_key_labels

        out["KeyLabels"] = (
            capo_cloudwatch.types.insight_rule_contributor_key_labels.serialize_aws_json_1_0(
                value["key_labels"]
            )
        )
    if "aggregation_statistic" in value:
        out["AggregationStatistic"] = value["aggregation_statistic"]
    if "aggregate_value" in value:
        out["AggregateValue"] = (
            "NaN"
            if value["aggregate_value"] != value["aggregate_value"]
            else "Infinity"
            if value["aggregate_value"] == float("inf")
            else "-Infinity"
            if value["aggregate_value"] == float("-inf")
            else value["aggregate_value"]
        )
    if "approximate_unique_count" in value:
        out["ApproximateUniqueCount"] = value["approximate_unique_count"]
    if "contributors" in value:
        import capo_cloudwatch.types.insight_rule_contributors

        out["Contributors"] = (
            capo_cloudwatch.types.insight_rule_contributors.serialize_aws_json_1_0(
                value["contributors"]
            )
        )
    if "metric_datapoints" in value:
        import capo_cloudwatch.types.insight_rule_metric_datapoints

        out["MetricDatapoints"] = (
            capo_cloudwatch.types.insight_rule_metric_datapoints.serialize_aws_json_1_0(
                value["metric_datapoints"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetInsightRuleReportOutput:
    out: GetInsightRuleReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("KeyLabels") is not None:
        import capo_cloudwatch.types.insight_rule_contributor_key_labels

        out["key_labels"] = (
            capo_cloudwatch.types.insight_rule_contributor_key_labels.deserialize_aws_json_1_0(
                data["KeyLabels"]
            )
        )
    if data.get("AggregationStatistic") is not None:
        out["aggregation_statistic"] = data["AggregationStatistic"]
    if data.get("AggregateValue") is not None:
        out["aggregate_value"] = float(data["AggregateValue"])
    if data.get("ApproximateUniqueCount") is not None:
        out["approximate_unique_count"] = data["ApproximateUniqueCount"]
    if data.get("Contributors") is not None:
        import capo_cloudwatch.types.insight_rule_contributors

        out["contributors"] = (
            capo_cloudwatch.types.insight_rule_contributors.deserialize_aws_json_1_0(
                data["Contributors"]
            )
        )
    if data.get("MetricDatapoints") is not None:
        import capo_cloudwatch.types.insight_rule_metric_datapoints

        out["metric_datapoints"] = (
            capo_cloudwatch.types.insight_rule_metric_datapoints.deserialize_aws_json_1_0(
                data["MetricDatapoints"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetInsightRuleReportOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key_labels" in value:
        import capo_cloudwatch.types.insight_rule_contributor_key_labels

        capo_cloudwatch.types.insight_rule_contributor_key_labels.serialize_query(
            value["key_labels"], pairs, f"{key_prefix}KeyLabels"
        )
    if "aggregation_statistic" in value:
        pairs.append(
            (f"{key_prefix}AggregationStatistic", str(value["aggregation_statistic"]))
        )
    if "aggregate_value" in value:
        pairs.append(
            (
                f"{key_prefix}AggregateValue",
                (
                    "NaN"
                    if value["aggregate_value"] != value["aggregate_value"]
                    else "Infinity"
                    if value["aggregate_value"] == float("inf")
                    else "-Infinity"
                    if value["aggregate_value"] == float("-inf")
                    else str(value["aggregate_value"])
                ),
            )
        )
    if "approximate_unique_count" in value:
        pairs.append(
            (
                f"{key_prefix}ApproximateUniqueCount",
                str(value["approximate_unique_count"]),
            )
        )
    if "contributors" in value:
        import capo_cloudwatch.types.insight_rule_contributors

        capo_cloudwatch.types.insight_rule_contributors.serialize_query(
            value["contributors"], pairs, f"{key_prefix}Contributors"
        )
    if "metric_datapoints" in value:
        import capo_cloudwatch.types.insight_rule_metric_datapoints

        capo_cloudwatch.types.insight_rule_metric_datapoints.serialize_query(
            value["metric_datapoints"], pairs, f"{key_prefix}MetricDatapoints"
        )


def deserialize_query(el: Element) -> GetInsightRuleReportOutput:
    out: GetInsightRuleReportOutput = {}  # type: ignore[typeddict-item]
    child_key_labels = el.find("KeyLabels")
    if child_key_labels is not None:
        import capo_cloudwatch.types.insight_rule_contributor_key_labels

        out["key_labels"] = (
            capo_cloudwatch.types.insight_rule_contributor_key_labels.deserialize_query(
                child_key_labels
            )
        )
    child_aggregation_statistic = el.find("AggregationStatistic")
    if child_aggregation_statistic is not None:
        out["aggregation_statistic"] = str(child_aggregation_statistic.text or "")
    child_aggregate_value = el.find("AggregateValue")
    if child_aggregate_value is not None:
        out["aggregate_value"] = float(child_aggregate_value.text or "")
    child_approximate_unique_count = el.find("ApproximateUniqueCount")
    if child_approximate_unique_count is not None:
        out["approximate_unique_count"] = int(child_approximate_unique_count.text or "")
    child_contributors = el.find("Contributors")
    if child_contributors is not None:
        import capo_cloudwatch.types.insight_rule_contributors

        out["contributors"] = (
            capo_cloudwatch.types.insight_rule_contributors.deserialize_query(
                child_contributors
            )
        )
    child_metric_datapoints = el.find("MetricDatapoints")
    if child_metric_datapoints is not None:
        import capo_cloudwatch.types.insight_rule_metric_datapoints

        out["metric_datapoints"] = (
            capo_cloudwatch.types.insight_rule_metric_datapoints.deserialize_query(
                child_metric_datapoints
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetInsightRuleReportOutput) -> dict:
    out: dict = {}
    if "key_labels" in value:
        import capo_cloudwatch.types.insight_rule_contributor_key_labels

        out["KeyLabels"] = (
            capo_cloudwatch.types.insight_rule_contributor_key_labels.serialize_cbor(
                value["key_labels"]
            )
        )
    if "aggregation_statistic" in value:
        out["AggregationStatistic"] = value["aggregation_statistic"]
    if "aggregate_value" in value:
        out["AggregateValue"] = value["aggregate_value"]
    if "approximate_unique_count" in value:
        out["ApproximateUniqueCount"] = value["approximate_unique_count"]
    if "contributors" in value:
        import capo_cloudwatch.types.insight_rule_contributors

        out["Contributors"] = (
            capo_cloudwatch.types.insight_rule_contributors.serialize_cbor(
                value["contributors"]
            )
        )
    if "metric_datapoints" in value:
        import capo_cloudwatch.types.insight_rule_metric_datapoints

        out["MetricDatapoints"] = (
            capo_cloudwatch.types.insight_rule_metric_datapoints.serialize_cbor(
                value["metric_datapoints"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetInsightRuleReportOutput:
    out: GetInsightRuleReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("KeyLabels") is not None:
        import capo_cloudwatch.types.insight_rule_contributor_key_labels

        out["key_labels"] = (
            capo_cloudwatch.types.insight_rule_contributor_key_labels.deserialize_cbor(
                data["KeyLabels"]
            )
        )
    if data.get("AggregationStatistic") is not None:
        out["aggregation_statistic"] = data["AggregationStatistic"]
    if data.get("AggregateValue") is not None:
        out["aggregate_value"] = float(data["AggregateValue"])
    if data.get("ApproximateUniqueCount") is not None:
        out["approximate_unique_count"] = data["ApproximateUniqueCount"]
    if data.get("Contributors") is not None:
        import capo_cloudwatch.types.insight_rule_contributors

        out["contributors"] = (
            capo_cloudwatch.types.insight_rule_contributors.deserialize_cbor(
                data["Contributors"]
            )
        )
    if data.get("MetricDatapoints") is not None:
        import capo_cloudwatch.types.insight_rule_metric_datapoints

        out["metric_datapoints"] = (
            capo_cloudwatch.types.insight_rule_metric_datapoints.deserialize_cbor(
                data["MetricDatapoints"]
            )
        )
    return out
