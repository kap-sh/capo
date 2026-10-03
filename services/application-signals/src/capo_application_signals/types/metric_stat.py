"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricStat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.metric
    import capo_application_signals.types.period
    import capo_application_signals.types.standard_unit
    import capo_application_signals.types.stat


class MetricStat(TypedDict, closed=True):
    metric: "capo_application_signals.types.metric.Metric"
    """<p>The metric to use as the service level indicator, including the metric name, namespace, and dimensions.</p>"""
    period: "capo_application_signals.types.period.Period"
    """<p>The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a <code>PutMetricData</code> call that includes a <code>StorageResolution</code> of 1 second.</p>"""
    stat: "capo_application_signals.types.stat.Stat"
    """<p>The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html">CloudWatch statistics definitions</a>.</p>"""
    unit: NotRequired["capo_application_signals.types.standard_unit.StandardUnit"]
    """<p>If you omit <code>Unit</code> then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricStat) -> dict:
    out: dict = {}
    import capo_application_signals.types.metric

    out["Metric"] = capo_application_signals.types.metric.serialize_json(
        value["metric"]
    )
    out["Period"] = value["period"]
    out["Stat"] = value["stat"]
    if "unit" in value:
        import capo_application_signals.types.standard_unit

        out["Unit"] = capo_application_signals.types.standard_unit.serialize_json(
            value["unit"]
        )
    return out


def deserialize_json(data: dict) -> MetricStat:
    out: MetricStat = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        import capo_application_signals.types.metric

        out["metric"] = capo_application_signals.types.metric.deserialize_json(
            data["Metric"]
        )
    else:
        raise DeserializationError("MetricStat.metric required")
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    else:
        raise DeserializationError("MetricStat.period required")
    if data.get("Stat") is not None:
        out["stat"] = data["Stat"]
    else:
        raise DeserializationError("MetricStat.stat required")
    if data.get("Unit") is not None:
        import capo_application_signals.types.standard_unit

        out["unit"] = capo_application_signals.types.standard_unit.deserialize_json(
            data["Unit"]
        )
    return out
