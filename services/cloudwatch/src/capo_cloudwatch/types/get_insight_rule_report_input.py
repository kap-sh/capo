"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetInsightRuleReportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_metric_list
    import capo_cloudwatch.types.insight_rule_name
    import capo_cloudwatch.types.insight_rule_order_by
    import capo_cloudwatch.types.insight_rule_unbound_integer
    import capo_cloudwatch.types.period
    import capo_cloudwatch.types.timestamp


class GetInsightRuleReportInput(TypedDict, closed=True):
    rule_name: NotRequired["capo_cloudwatch.types.insight_rule_name.InsightRuleName"]
    """<p>The name of the rule that you want to see data from.</p>"""
    start_time: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The start time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>"""
    end_time: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The end time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>"""
    period: NotRequired["capo_cloudwatch.types.period.Period"]
    """<p>The period, in seconds, to use for the statistics in the <code>InsightRuleMetricDatapoint</code> results.</p>"""
    max_contributor_count: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_integer.InsightRuleUnboundInteger"
    ]
    """<p>The maximum number of contributors to include in the report. The range is 1 to 100. If you omit this, the default of 10 is used.</p>"""
    metrics: NotRequired[
        "capo_cloudwatch.types.insight_rule_metric_list.InsightRuleMetricList"
    ]
    """<p>Specifies which metrics to use for aggregation of contributor values for the report. You can specify one or more of the following metrics:</p> <ul> <li> <p> <code>UniqueContributors</code> -- the number of unique contributors for each data point.</p> </li> <li> <p> <code>MaxContributorValue</code> -- the value of the top contributor for each data point. The identity of the contributor might change for each data point in the graph.</p> <p>If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the rule's <code>Value</code>, during that period.</p> </li> <li> <p> <code>SampleCount</code> -- the number of data points matched by the rule.</p> </li> <li> <p> <code>Sum</code> -- the sum of the values from all contributors during the time period represented by that data point.</p> </li> <li> <p> <code>Minimum</code> -- the minimum value from a single observation during the time period represented by that data point.</p> </li> <li> <p> <code>Maximum</code> -- the maximum value from a single observation during the time period represented by that data point.</p> </li> <li> <p> <code>Average</code> -- the average value from all contributors during the time period represented by that data point.</p> </li> </ul>"""
    order_by: NotRequired[
        "capo_cloudwatch.types.insight_rule_order_by.InsightRuleOrderBy"
    ]
    """<p>Determines what statistic to use to rank the contributors. Valid values are <code>Sum</code> and <code>Maximum</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetInsightRuleReportInput) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "start_time" in value:
        import capo_cloudwatch.types.timestamp

        out["StartTime"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudwatch.types.timestamp

        out["EndTime"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["end_time"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "max_contributor_count" in value:
        out["MaxContributorCount"] = value["max_contributor_count"]
    if "metrics" in value:
        import capo_cloudwatch.types.insight_rule_metric_list

        out["Metrics"] = (
            capo_cloudwatch.types.insight_rule_metric_list.serialize_aws_json_1_0(
                value["metrics"]
            )
        )
    if "order_by" in value:
        out["OrderBy"] = value["order_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetInsightRuleReportInput:
    out: GetInsightRuleReportInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("StartTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_time"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["end_time"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("MaxContributorCount") is not None:
        out["max_contributor_count"] = data["MaxContributorCount"]
    if data.get("Metrics") is not None:
        import capo_cloudwatch.types.insight_rule_metric_list

        out["metrics"] = (
            capo_cloudwatch.types.insight_rule_metric_list.deserialize_aws_json_1_0(
                data["Metrics"]
            )
        )
    if data.get("OrderBy") is not None:
        out["order_by"] = data["OrderBy"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetInsightRuleReportInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_name" in value:
        pairs.append((f"{key_prefix}RuleName", str(value["rule_name"])))
    if "start_time" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "period" in value:
        pairs.append((f"{key_prefix}Period", str(value["period"])))
    if "max_contributor_count" in value:
        pairs.append(
            (f"{key_prefix}MaxContributorCount", str(value["max_contributor_count"]))
        )
    if "metrics" in value:
        import capo_cloudwatch.types.insight_rule_metric_list

        capo_cloudwatch.types.insight_rule_metric_list.serialize_query(
            value["metrics"], pairs, f"{key_prefix}Metrics"
        )
    if "order_by" in value:
        pairs.append((f"{key_prefix}OrderBy", str(value["order_by"])))


def deserialize_query(el: Element) -> GetInsightRuleReportInput:
    out: GetInsightRuleReportInput = {}  # type: ignore[typeddict-item]
    child_rule_name = el.find("RuleName")
    if child_rule_name is not None:
        out["rule_name"] = str(child_rule_name.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_cloudwatch.types.timestamp

        out["start_time"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_cloudwatch.types.timestamp

        out["end_time"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_end_time
        )
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_max_contributor_count = el.find("MaxContributorCount")
    if child_max_contributor_count is not None:
        out["max_contributor_count"] = int(child_max_contributor_count.text or "")
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import capo_cloudwatch.types.insight_rule_metric_list

        out["metrics"] = (
            capo_cloudwatch.types.insight_rule_metric_list.deserialize_query(
                child_metrics
            )
        )
    child_order_by = el.find("OrderBy")
    if child_order_by is not None:
        out["order_by"] = str(child_order_by.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetInsightRuleReportInput) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "start_time" in value:
        import capo_cloudwatch.types.timestamp

        out["StartTime"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudwatch.types.timestamp

        out["EndTime"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "max_contributor_count" in value:
        out["MaxContributorCount"] = value["max_contributor_count"]
    if "metrics" in value:
        import capo_cloudwatch.types.insight_rule_metric_list

        out["Metrics"] = capo_cloudwatch.types.insight_rule_metric_list.serialize_cbor(
            value["metrics"]
        )
    if "order_by" in value:
        out["OrderBy"] = value["order_by"]
    return out


def deserialize_cbor(data: dict) -> GetInsightRuleReportInput:
    out: GetInsightRuleReportInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("StartTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_time"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["end_time"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("MaxContributorCount") is not None:
        out["max_contributor_count"] = data["MaxContributorCount"]
    if data.get("Metrics") is not None:
        import capo_cloudwatch.types.insight_rule_metric_list

        out["metrics"] = (
            capo_cloudwatch.types.insight_rule_metric_list.deserialize_cbor(
                data["Metrics"]
            )
        )
    if data.get("OrderBy") is not None:
        out["order_by"] = data["OrderBy"]
    return out
