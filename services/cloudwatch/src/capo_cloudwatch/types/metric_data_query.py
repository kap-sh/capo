"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricDataQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.account_id
    import capo_cloudwatch.types.metric_expression
    import capo_cloudwatch.types.metric_id
    import capo_cloudwatch.types.metric_label
    import capo_cloudwatch.types.metric_stat
    import capo_cloudwatch.types.period
    import capo_cloudwatch.types.return_data


class MetricDataQuery(TypedDict, closed=True):
    id: NotRequired["capo_cloudwatch.types.metric_id.MetricId"]
    """<p>A short name used to tie this object to the results in the response. This name must be unique within a single call to <code>GetMetricData</code>. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.</p>"""
    metric_stat: NotRequired["capo_cloudwatch.types.metric_stat.MetricStat"]
    """<p>The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.</p> <p>Within one MetricDataQuery object, you must specify either <code>Expression</code> or <code>MetricStat</code> but not both.</p>"""
    expression: NotRequired["capo_cloudwatch.types.metric_expression.MetricExpression"]
    """<p>This field can contain either a Metrics Insights query, or a metric math expression to be performed on the returned data. For more information about Metrics Insights queries, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-querylanguage">Metrics Insights query components and syntax</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>A math expression can use the <code>Id</code> of the other metrics or queries to refer to those metrics, and can also use the <code>Id</code> of other expressions to use the result of those expressions. For more information about metric math expressions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax">Metric Math Syntax and Functions</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>Within each MetricDataQuery object, you must specify either <code>Expression</code> or <code>MetricStat</code> but not both.</p>"""
    label: NotRequired["capo_cloudwatch.types.metric_label.MetricLabel"]
    """<p>A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.</p> <p>You can put dynamic expressions into a label, so that it is more descriptive. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html">Using Dynamic Labels</a>.</p>"""
    return_data: NotRequired["capo_cloudwatch.types.return_data.ReturnData"]
    """<p>When used in <code>GetMetricData</code>, this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify <code>false</code>. If you omit this, the default of <code>true</code> is used.</p> <p>When used in <code>PutMetricAlarm</code>, specify <code>true</code> for the one expression result to use as the alarm. For all other metrics and expressions in the same <code>PutMetricAlarm</code> operation, specify <code>ReturnData</code> as False.</p>"""
    period: NotRequired["capo_cloudwatch.types.period.Period"]
    """<p>The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a <code>PutMetricData</code> operation that includes a <code>StorageResolution of 1 second</code>.</p>"""
    account_id: NotRequired["capo_cloudwatch.types.account_id.AccountId"]
    """<p>The ID of the account where the metrics are located.</p> <p>If you are performing a <code>GetMetricData</code> operation in a monitoring account, use this to specify which account to retrieve this metric from.</p> <p>If you are performing a <code>PutMetricAlarm</code> operation, use this to specify which account contains the metric that the alarm is watching.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricDataQuery) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "metric_stat" in value:
        import capo_cloudwatch.types.metric_stat

        out["MetricStat"] = capo_cloudwatch.types.metric_stat.serialize_aws_json_1_0(
            value["metric_stat"]
        )
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "label" in value:
        out["Label"] = value["label"]
    if "return_data" in value:
        out["ReturnData"] = value["return_data"]
    if "period" in value:
        out["Period"] = value["period"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricDataQuery:
    out: MetricDataQuery = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("MetricStat") is not None:
        import capo_cloudwatch.types.metric_stat

        out["metric_stat"] = capo_cloudwatch.types.metric_stat.deserialize_aws_json_1_0(
            data["MetricStat"]
        )
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("ReturnData") is not None:
        out["return_data"] = data["ReturnData"]
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDataQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))
    if "metric_stat" in value:
        import capo_cloudwatch.types.metric_stat

        capo_cloudwatch.types.metric_stat.serialize_query(
            value["metric_stat"], pairs, f"{key_prefix}MetricStat"
        )
    if "expression" in value:
        pairs.append((f"{key_prefix}Expression", str(value["expression"])))
    if "label" in value:
        pairs.append((f"{key_prefix}Label", str(value["label"])))
    if "return_data" in value:
        pairs.append(
            (f"{key_prefix}ReturnData", "true" if value["return_data"] else "false")
        )
    if "period" in value:
        pairs.append((f"{key_prefix}Period", str(value["period"])))
    if "account_id" in value:
        pairs.append((f"{key_prefix}AccountId", str(value["account_id"])))


def deserialize_query(el: Element) -> MetricDataQuery:
    out: MetricDataQuery = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_metric_stat = el.find("MetricStat")
    if child_metric_stat is not None:
        import capo_cloudwatch.types.metric_stat

        out["metric_stat"] = capo_cloudwatch.types.metric_stat.deserialize_query(
            child_metric_stat
        )
    child_expression = el.find("Expression")
    if child_expression is not None:
        out["expression"] = str(child_expression.text or "")
    child_label = el.find("Label")
    if child_label is not None:
        out["label"] = str(child_label.text or "")
    child_return_data = el.find("ReturnData")
    if child_return_data is not None:
        out["return_data"] = (child_return_data.text or "").lower() == "true"
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    return out
