"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.composite_alarms
    import capo_cloudwatch.types.log_alarms
    import capo_cloudwatch.types.metric_alarms
    import capo_cloudwatch.types.next_token


class DescribeAlarmsOutput(TypedDict, closed=True):
    composite_alarms: NotRequired[
        "capo_cloudwatch.types.composite_alarms.CompositeAlarms"
    ]
    """<p>The information about any composite alarms returned by the operation.</p>"""
    metric_alarms: NotRequired["capo_cloudwatch.types.metric_alarms.MetricAlarms"]
    """<p>The information about any metric alarms returned by the operation.</p>"""
    log_alarms: NotRequired["capo_cloudwatch.types.log_alarms.LogAlarms"]
    """<p>The information about any log alarms returned by the operation.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmsOutput) -> dict:
    out: dict = {}
    if "composite_alarms" in value:
        import capo_cloudwatch.types.composite_alarms

        out["CompositeAlarms"] = (
            capo_cloudwatch.types.composite_alarms.serialize_aws_json_1_0(
                value["composite_alarms"]
            )
        )
    if "metric_alarms" in value:
        import capo_cloudwatch.types.metric_alarms

        out["MetricAlarms"] = (
            capo_cloudwatch.types.metric_alarms.serialize_aws_json_1_0(
                value["metric_alarms"]
            )
        )
    if "log_alarms" in value:
        import capo_cloudwatch.types.log_alarms

        out["LogAlarms"] = capo_cloudwatch.types.log_alarms.serialize_aws_json_1_0(
            value["log_alarms"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmsOutput:
    out: DescribeAlarmsOutput = {}  # type: ignore[typeddict-item]
    if data.get("CompositeAlarms") is not None:
        import capo_cloudwatch.types.composite_alarms

        out["composite_alarms"] = (
            capo_cloudwatch.types.composite_alarms.deserialize_aws_json_1_0(
                data["CompositeAlarms"]
            )
        )
    if data.get("MetricAlarms") is not None:
        import capo_cloudwatch.types.metric_alarms

        out["metric_alarms"] = (
            capo_cloudwatch.types.metric_alarms.deserialize_aws_json_1_0(
                data["MetricAlarms"]
            )
        )
    if data.get("LogAlarms") is not None:
        import capo_cloudwatch.types.log_alarms

        out["log_alarms"] = capo_cloudwatch.types.log_alarms.deserialize_aws_json_1_0(
            data["LogAlarms"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "composite_alarms" in value:
        import capo_cloudwatch.types.composite_alarms

        capo_cloudwatch.types.composite_alarms.serialize_query(
            value["composite_alarms"], pairs, f"{key_prefix}CompositeAlarms"
        )
    if "metric_alarms" in value:
        import capo_cloudwatch.types.metric_alarms

        capo_cloudwatch.types.metric_alarms.serialize_query(
            value["metric_alarms"], pairs, f"{key_prefix}MetricAlarms"
        )
    if "log_alarms" in value:
        import capo_cloudwatch.types.log_alarms

        capo_cloudwatch.types.log_alarms.serialize_query(
            value["log_alarms"], pairs, f"{key_prefix}LogAlarms"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAlarmsOutput:
    out: DescribeAlarmsOutput = {}  # type: ignore[typeddict-item]
    child_composite_alarms = el.find("CompositeAlarms")
    if child_composite_alarms is not None:
        import capo_cloudwatch.types.composite_alarms

        out["composite_alarms"] = (
            capo_cloudwatch.types.composite_alarms.deserialize_query(
                child_composite_alarms
            )
        )
    child_metric_alarms = el.find("MetricAlarms")
    if child_metric_alarms is not None:
        import capo_cloudwatch.types.metric_alarms

        out["metric_alarms"] = capo_cloudwatch.types.metric_alarms.deserialize_query(
            child_metric_alarms
        )
    child_log_alarms = el.find("LogAlarms")
    if child_log_alarms is not None:
        import capo_cloudwatch.types.log_alarms

        out["log_alarms"] = capo_cloudwatch.types.log_alarms.deserialize_query(
            child_log_alarms
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAlarmsOutput) -> dict:
    out: dict = {}
    if "composite_alarms" in value:
        import capo_cloudwatch.types.composite_alarms

        out["CompositeAlarms"] = capo_cloudwatch.types.composite_alarms.serialize_cbor(
            value["composite_alarms"]
        )
    if "metric_alarms" in value:
        import capo_cloudwatch.types.metric_alarms

        out["MetricAlarms"] = capo_cloudwatch.types.metric_alarms.serialize_cbor(
            value["metric_alarms"]
        )
    if "log_alarms" in value:
        import capo_cloudwatch.types.log_alarms

        out["LogAlarms"] = capo_cloudwatch.types.log_alarms.serialize_cbor(
            value["log_alarms"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAlarmsOutput:
    out: DescribeAlarmsOutput = {}  # type: ignore[typeddict-item]
    if data.get("CompositeAlarms") is not None:
        import capo_cloudwatch.types.composite_alarms

        out["composite_alarms"] = (
            capo_cloudwatch.types.composite_alarms.deserialize_cbor(
                data["CompositeAlarms"]
            )
        )
    if data.get("MetricAlarms") is not None:
        import capo_cloudwatch.types.metric_alarms

        out["metric_alarms"] = capo_cloudwatch.types.metric_alarms.deserialize_cbor(
            data["MetricAlarms"]
        )
    if data.get("LogAlarms") is not None:
        import capo_cloudwatch.types.log_alarms

        out["log_alarms"] = capo_cloudwatch.types.log_alarms.deserialize_cbor(
            data["LogAlarms"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
