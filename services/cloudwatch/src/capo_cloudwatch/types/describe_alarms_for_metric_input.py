"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmsForMetricInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.extended_statistic
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.period
    import capo_cloudwatch.types.standard_unit
    import capo_cloudwatch.types.statistic


class DescribeAlarmsForMetricInput(TypedDict, closed=True):
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace of the metric.</p>"""
    statistic: NotRequired["capo_cloudwatch.types.statistic.Statistic"]
    """<p>The statistic for the metric, other than percentiles. For percentile statistics, use <code>ExtendedStatistics</code>.</p>"""
    extended_statistic: NotRequired[
        "capo_cloudwatch.types.extended_statistic.ExtendedStatistic"
    ]
    """<p>The percentile statistic for the metric. Specify a value between p0.0 and p100.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.</p>"""
    period: NotRequired["capo_cloudwatch.types.period.Period"]
    """<p>The period, in seconds, over which the statistic is applied.</p>"""
    unit: NotRequired["capo_cloudwatch.types.standard_unit.StandardUnit"]
    """<p>The unit for the metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmsForMetricInput) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "statistic" in value:
        import capo_cloudwatch.types.statistic

        out["Statistic"] = capo_cloudwatch.types.statistic.serialize_aws_json_1_0(
            value["statistic"]
        )
    if "extended_statistic" in value:
        out["ExtendedStatistic"] = value["extended_statistic"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmsForMetricInput:
    out: DescribeAlarmsForMetricInput = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("Statistic") is not None:
        import capo_cloudwatch.types.statistic

        out["statistic"] = capo_cloudwatch.types.statistic.deserialize_aws_json_1_0(
            data["Statistic"]
        )
    if data.get("ExtendedStatistic") is not None:
        out["extended_statistic"] = data["ExtendedStatistic"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
            data["Dimensions"]
        )
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_aws_json_1_0(
            data["Unit"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmsForMetricInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "statistic" in value:
        import capo_cloudwatch.types.statistic

        capo_cloudwatch.types.statistic.serialize_query(
            value["statistic"], pairs, f"{key_prefix}Statistic"
        )
    if "extended_statistic" in value:
        pairs.append(
            (f"{key_prefix}ExtendedStatistic", str(value["extended_statistic"]))
        )
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        capo_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )
    if "period" in value:
        pairs.append((f"{key_prefix}Period", str(value["period"])))
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        capo_cloudwatch.types.standard_unit.serialize_query(
            value["unit"], pairs, f"{key_prefix}Unit"
        )


def deserialize_query(el: Element) -> DescribeAlarmsForMetricInput:
    out: DescribeAlarmsForMetricInput = {}  # type: ignore[typeddict-item]
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_statistic = el.find("Statistic")
    if child_statistic is not None:
        import capo_cloudwatch.types.statistic

        out["statistic"] = capo_cloudwatch.types.statistic.deserialize_query(
            child_statistic
        )
    child_extended_statistic = el.find("ExtendedStatistic")
    if child_extended_statistic is not None:
        out["extended_statistic"] = str(child_extended_statistic.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_query(
            child_dimensions
        )
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_unit = el.find("Unit")
    if child_unit is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_query(child_unit)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAlarmsForMetricInput) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "statistic" in value:
        import capo_cloudwatch.types.statistic

        out["Statistic"] = capo_cloudwatch.types.statistic.serialize_cbor(
            value["statistic"]
        )
    if "extended_statistic" in value:
        out["ExtendedStatistic"] = value["extended_statistic"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_cbor(
            value["dimensions"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_cbor(value["unit"])
    return out


def deserialize_cbor(data: dict) -> DescribeAlarmsForMetricInput:
    out: DescribeAlarmsForMetricInput = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("Statistic") is not None:
        import capo_cloudwatch.types.statistic

        out["statistic"] = capo_cloudwatch.types.statistic.deserialize_cbor(
            data["Statistic"]
        )
    if data.get("ExtendedStatistic") is not None:
        out["extended_statistic"] = data["ExtendedStatistic"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_cbor(
            data["Dimensions"]
        )
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_cbor(data["Unit"])
    return out
