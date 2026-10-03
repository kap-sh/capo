"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.anomaly_detector_excluded_time_ranges
    import capo_cloudwatch.types.anomaly_detector_metric_timezone


class AnomalyDetectorConfiguration(TypedDict, closed=True):
    excluded_time_ranges: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_excluded_time_ranges.AnomalyDetectorExcludedTimeRanges"
    ]
    """<p>An array of time ranges to exclude from use when the anomaly detection model is trained. Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren't used when CloudWatch creates the model.</p>"""
    metric_timezone: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_metric_timezone.AnomalyDetectorMetricTimezone"
    ]
    """<p>The time zone to use for the metric. This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes.</p> <p>To specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see <a href="https://en.wikipedia.org/wiki/Tz_database">tz database</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetectorConfiguration) -> dict:
    out: dict = {}
    if "excluded_time_ranges" in value:
        import capo_cloudwatch.types.anomaly_detector_excluded_time_ranges

        out["ExcludedTimeRanges"] = (
            capo_cloudwatch.types.anomaly_detector_excluded_time_ranges.serialize_aws_json_1_0(
                value["excluded_time_ranges"]
            )
        )
    if "metric_timezone" in value:
        out["MetricTimezone"] = value["metric_timezone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AnomalyDetectorConfiguration:
    out: AnomalyDetectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ExcludedTimeRanges") is not None:
        import capo_cloudwatch.types.anomaly_detector_excluded_time_ranges

        out["excluded_time_ranges"] = (
            capo_cloudwatch.types.anomaly_detector_excluded_time_ranges.deserialize_aws_json_1_0(
                data["ExcludedTimeRanges"]
            )
        )
    if data.get("MetricTimezone") is not None:
        out["metric_timezone"] = data["MetricTimezone"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: AnomalyDetectorConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "excluded_time_ranges" in value:
        import capo_cloudwatch.types.anomaly_detector_excluded_time_ranges

        capo_cloudwatch.types.anomaly_detector_excluded_time_ranges.serialize_query(
            value["excluded_time_ranges"], pairs, f"{key_prefix}ExcludedTimeRanges"
        )
    if "metric_timezone" in value:
        pairs.append((f"{key_prefix}MetricTimezone", str(value["metric_timezone"])))


def deserialize_query(el: Element) -> AnomalyDetectorConfiguration:
    out: AnomalyDetectorConfiguration = {}  # type: ignore[typeddict-item]
    child_excluded_time_ranges = el.find("ExcludedTimeRanges")
    if child_excluded_time_ranges is not None:
        import capo_cloudwatch.types.anomaly_detector_excluded_time_ranges

        out["excluded_time_ranges"] = (
            capo_cloudwatch.types.anomaly_detector_excluded_time_ranges.deserialize_query(
                child_excluded_time_ranges
            )
        )
    child_metric_timezone = el.find("MetricTimezone")
    if child_metric_timezone is not None:
        out["metric_timezone"] = str(child_metric_timezone.text or "")
    return out
