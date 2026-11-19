"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmsForMetricOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_alarms


class DescribeAlarmsForMetricOutput(TypedDict, closed=True):
    metric_alarms: NotRequired["capo_cloudwatch.types.metric_alarms.MetricAlarms"]
    """<p>The information for each alarm with the specified metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmsForMetricOutput) -> dict:
    out: dict = {}
    if "metric_alarms" in value:
        import capo_cloudwatch.types.metric_alarms

        out["MetricAlarms"] = (
            capo_cloudwatch.types.metric_alarms.serialize_aws_json_1_0(
                value["metric_alarms"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmsForMetricOutput:
    out: DescribeAlarmsForMetricOutput = {}  # type: ignore[typeddict-item]
    if data.get("MetricAlarms") is not None:
        import capo_cloudwatch.types.metric_alarms

        out["metric_alarms"] = (
            capo_cloudwatch.types.metric_alarms.deserialize_aws_json_1_0(
                data["MetricAlarms"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmsForMetricOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_alarms" in value:
        import capo_cloudwatch.types.metric_alarms

        capo_cloudwatch.types.metric_alarms.serialize_query(
            value["metric_alarms"], pairs, f"{key_prefix}MetricAlarms"
        )


def deserialize_query(el: Element) -> DescribeAlarmsForMetricOutput:
    out: DescribeAlarmsForMetricOutput = {}  # type: ignore[typeddict-item]
    child_metric_alarms = el.find("MetricAlarms")
    if child_metric_alarms is not None:
        import capo_cloudwatch.types.metric_alarms

        out["metric_alarms"] = capo_cloudwatch.types.metric_alarms.deserialize_query(
            child_metric_alarms
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAlarmsForMetricOutput) -> dict:
    out: dict = {}
    if "metric_alarms" in value:
        import capo_cloudwatch.types.metric_alarms

        out["MetricAlarms"] = capo_cloudwatch.types.metric_alarms.serialize_cbor(
            value["metric_alarms"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeAlarmsForMetricOutput:
    out: DescribeAlarmsForMetricOutput = {}  # type: ignore[typeddict-item]
    if data.get("MetricAlarms") is not None:
        import capo_cloudwatch.types.metric_alarms

        out["metric_alarms"] = capo_cloudwatch.types.metric_alarms.deserialize_cbor(
            data["MetricAlarms"]
        )
    return out
