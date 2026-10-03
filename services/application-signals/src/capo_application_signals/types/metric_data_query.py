"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricDataQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.account_id
    import capo_application_signals.types.metric_expression
    import capo_application_signals.types.metric_id
    import capo_application_signals.types.metric_label
    import capo_application_signals.types.metric_stat
    import capo_application_signals.types.period
    import capo_application_signals.types.return_data


class MetricDataQuery(TypedDict, closed=True):
    id: "capo_application_signals.types.metric_id.MetricId"
    """<p>A short name used to tie this object to the results in the response. This <code>Id</code> must be unique within a <code>MetricDataQueries</code> array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.</p>"""
    metric_stat: NotRequired["capo_application_signals.types.metric_stat.MetricStat"]
    """<p>A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.</p> <p>Within one <code>MetricDataQuery</code> object, you must specify either <code>Expression</code> or <code>MetricStat</code> but not both.</p>"""
    expression: NotRequired[
        "capo_application_signals.types.metric_expression.MetricExpression"
    ]
    """<p>This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this <code>MetricDataQueries</code> structure. </p> <p>A math expression can use the <code>Id</code> of the other metrics or queries to refer to those metrics, and can also use the <code>Id</code> of other expressions to use the result of those expressions. For more information about metric math expressions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax">Metric Math Syntax and Functions</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>Within each <code>MetricDataQuery</code> object, you must specify either <code>Expression</code> or <code>MetricStat</code> but not both.</p>"""
    label: NotRequired["capo_application_signals.types.metric_label.MetricLabel"]
    """<p>A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If <code>Label</code> is omitted, CloudWatch generates a default.</p> <p>You can put dynamic expressions into a label, so that it is more descriptive. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html">Using Dynamic Labels</a>.</p>"""
    return_data: NotRequired["capo_application_signals.types.return_data.ReturnData"]
    """<p>Use this only if you are using a metric math expression for the SLO. Specify <code>true</code> for <code>ReturnData</code> for only the one expression result to use as the alarm. For all other metrics and expressions in the same <code>CreateServiceLevelObjective</code> operation, specify <code>ReturnData</code> as <code>false</code>.</p>"""
    period: NotRequired["capo_application_signals.types.period.Period"]
    """<p>The granularity, in seconds, of the returned data points for this metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a <code>PutMetricData</code> call that includes a <code>StorageResolution</code> of 1 second.</p> <p>If the <code>StartTime</code> parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:</p> <ul> <li> <p>Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).</p> </li> <li> <p>Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).</p> </li> <li> <p>Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).</p> </li> </ul>"""
    account_id: NotRequired["capo_application_signals.types.account_id.AccountId"]
    """<p>The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDataQuery) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "metric_stat" in value:
        import capo_application_signals.types.metric_stat

        out["MetricStat"] = capo_application_signals.types.metric_stat.serialize_json(
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


def deserialize_json(data: dict) -> MetricDataQuery:
    out: MetricDataQuery = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("MetricDataQuery.id required")
    if data.get("MetricStat") is not None:
        import capo_application_signals.types.metric_stat

        out["metric_stat"] = (
            capo_application_signals.types.metric_stat.deserialize_json(
                data["MetricStat"]
            )
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
