"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricDatum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.counts
    import capo_cloudwatch.types.datapoint_value
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.standard_unit
    import capo_cloudwatch.types.statistic_set
    import capo_cloudwatch.types.storage_resolution
    import capo_cloudwatch.types.timestamp
    import capo_cloudwatch.types.values


class MetricDatum(TypedDict, closed=True):
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>The dimensions associated with the metric. </p>"""
    timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.</p>"""
    value: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The value for the metric.</p> <p>Although the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.</p>"""
    statistic_values: NotRequired["capo_cloudwatch.types.statistic_set.StatisticSet"]
    """<p>The statistical values for the metric.</p>"""
    values: NotRequired["capo_cloudwatch.types.values.Values"]
    """<p>Array of numbers representing the values for the metric during the period. Each unique value is listed just once in this array, and the corresponding number in the <code>Counts</code> array specifies the number of times that value occurred during the period. You can include up to 150 unique values in each <code>PutMetricData</code> action that specifies a <code>Values</code> array.</p> <p>Although the <code>Values</code> array accepts numbers of type <code>Double</code>, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.</p>"""
    counts: NotRequired["capo_cloudwatch.types.counts.Counts"]
    """<p>Array of numbers that is used along with the <code>Values</code> array. Each number in the <code>Count</code> array is the number of times the corresponding value in the <code>Values</code> array occurred during the period. </p> <p>If you omit the <code>Counts</code> array, the default of 1 is used as the value for each count. If you include a <code>Counts</code> array, it must include the same amount of values as the <code>Values</code> array.</p>"""
    unit: NotRequired["capo_cloudwatch.types.standard_unit.StandardUnit"]
    """<p>When you are using a <code>Put</code> operation, this defines what unit you want to use when storing the metric.</p> <p>In a <code>Get</code> operation, this displays the unit that is used for the metric.</p>"""
    storage_resolution: NotRequired[
        "capo_cloudwatch.types.storage_resolution.StorageResolution"
    ]
    """<p>Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#high-resolution-metrics">High-Resolution Metrics</a> in the <i>Amazon CloudWatch User Guide</i>. </p> <p>This field is optional, if you do not specify it the default of 60 is used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricDatum) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
        )
    if "value" in value:
        out["Value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    if "statistic_values" in value:
        import capo_cloudwatch.types.statistic_set

        out["StatisticValues"] = (
            capo_cloudwatch.types.statistic_set.serialize_aws_json_1_0(
                value["statistic_values"]
            )
        )
    if "values" in value:
        import capo_cloudwatch.types.values

        out["Values"] = capo_cloudwatch.types.values.serialize_aws_json_1_0(
            value["values"]
        )
    if "counts" in value:
        import capo_cloudwatch.types.counts

        out["Counts"] = capo_cloudwatch.types.counts.serialize_aws_json_1_0(
            value["counts"]
        )
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    if "storage_resolution" in value:
        out["StorageResolution"] = value["storage_resolution"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricDatum:
    out: MetricDatum = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
            data["Dimensions"]
        )
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["Timestamp"]
        )
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    if data.get("StatisticValues") is not None:
        import capo_cloudwatch.types.statistic_set

        out["statistic_values"] = (
            capo_cloudwatch.types.statistic_set.deserialize_aws_json_1_0(
                data["StatisticValues"]
            )
        )
    if data.get("Values") is not None:
        import capo_cloudwatch.types.values

        out["values"] = capo_cloudwatch.types.values.deserialize_aws_json_1_0(
            data["Values"]
        )
    if data.get("Counts") is not None:
        import capo_cloudwatch.types.counts

        out["counts"] = capo_cloudwatch.types.counts.deserialize_aws_json_1_0(
            data["Counts"]
        )
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_aws_json_1_0(
            data["Unit"]
        )
    if data.get("StorageResolution") is not None:
        out["storage_resolution"] = data["StorageResolution"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDatum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        capo_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )
    if "value" in value:
        pairs.append(
            (
                f"{key_prefix}Value",
                (
                    "NaN"
                    if value["value"] != value["value"]
                    else "Infinity"
                    if value["value"] == float("inf")
                    else "-Infinity"
                    if value["value"] == float("-inf")
                    else str(value["value"])
                ),
            )
        )
    if "statistic_values" in value:
        import capo_cloudwatch.types.statistic_set

        capo_cloudwatch.types.statistic_set.serialize_query(
            value["statistic_values"], pairs, f"{key_prefix}StatisticValues"
        )
    if "values" in value:
        import capo_cloudwatch.types.values

        capo_cloudwatch.types.values.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )
    if "counts" in value:
        import capo_cloudwatch.types.counts

        capo_cloudwatch.types.counts.serialize_query(
            value["counts"], pairs, f"{key_prefix}Counts"
        )
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        capo_cloudwatch.types.standard_unit.serialize_query(
            value["unit"], pairs, f"{key_prefix}Unit"
        )
    if "storage_resolution" in value:
        pairs.append(
            (f"{key_prefix}StorageResolution", str(value["storage_resolution"]))
        )


def deserialize_query(el: Element) -> MetricDatum:
    out: MetricDatum = {}  # type: ignore[typeddict-item]
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_query(
            child_dimensions
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = float(child_value.text or "")
    child_statistic_values = el.find("StatisticValues")
    if child_statistic_values is not None:
        import capo_cloudwatch.types.statistic_set

        out["statistic_values"] = capo_cloudwatch.types.statistic_set.deserialize_query(
            child_statistic_values
        )
    child_values = el.find("Values")
    if child_values is not None:
        import capo_cloudwatch.types.values

        out["values"] = capo_cloudwatch.types.values.deserialize_query(child_values)
    child_counts = el.find("Counts")
    if child_counts is not None:
        import capo_cloudwatch.types.counts

        out["counts"] = capo_cloudwatch.types.counts.deserialize_query(child_counts)
    child_unit = el.find("Unit")
    if child_unit is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_query(child_unit)
    child_storage_resolution = el.find("StorageResolution")
    if child_storage_resolution is not None:
        out["storage_resolution"] = int(child_storage_resolution.text or "")
    return out
