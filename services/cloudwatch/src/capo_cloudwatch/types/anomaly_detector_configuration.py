"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.anomaly_detector_adaptation_speed
    import capo_cloudwatch.types.anomaly_detector_excluded_time_ranges
    import capo_cloudwatch.types.anomaly_detector_metric_timezone
    import capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength


class AnomalyDetectorConfiguration(TypedDict, closed=True):
    excluded_time_ranges: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_excluded_time_ranges.AnomalyDetectorExcludedTimeRanges"
    ]
    """<p>An array of time ranges to exclude from use when the anomaly detection model is trained. Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren't used when CloudWatch creates the model.</p>"""
    metric_timezone: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_metric_timezone.AnomalyDetectorMetricTimezone"
    ]
    """<p>The time zone to use for the metric. This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes.</p> <p>To specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see <a href="https://en.wikipedia.org/wiki/Tz_database">tz database</a>.</p>"""
    adaptation_speed: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_adaptation_speed.AnomalyDetectorAdaptationSpeed"
    ]
    """<p>The speed at which the anomaly detection model adapts to sustained changes in the metric's baseline. Faster adaptation lets the model track shifting workloads sooner, but increases the chance that the model treats a real, lasting change as normal.</p> <p>Valid values:</p> <ul> <li> <p> <code>FAST</code> - The model adapts quickly to sustained changes in the baseline.</p> </li> <li> <p> <code>NORMAL</code> - The model adapts at a moderate pace. This is the default value.</p> </li> <li> <p> <code>SLOW</code> - The model adapts slowly, reducing the risk of treating a real change as normal.</p> </li> </ul>"""
    outlier_filtering_strength: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength.AnomalyDetectorOutlierFilteringStrength"
    ]
    """<p>The aggressiveness with which CloudWatch filters outliers from the metric data that the anomaly detection model uses. Stronger filtering excludes more extreme values, which can produce a tighter band of expected values but may also suppress legitimate spikes.</p> <p>Valid values:</p> <ul> <li> <p> <code>MINIMAL</code> - Excludes only the most extreme outliers.</p> </li> <li> <p> <code>MODERATE</code> - Excludes a moderate range of outliers. This is the default value.</p> </li> <li> <p> <code>STRICT</code> - Excludes a wider range of outliers, which can suppress legitimate spikes.</p> </li> </ul>"""


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
    if "adaptation_speed" in value:
        import capo_cloudwatch.types.anomaly_detector_adaptation_speed

        out["AdaptationSpeed"] = (
            capo_cloudwatch.types.anomaly_detector_adaptation_speed.serialize_aws_json_1_0(
                value["adaptation_speed"]
            )
        )
    if "outlier_filtering_strength" in value:
        import capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength

        out["OutlierFilteringStrength"] = (
            capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength.serialize_aws_json_1_0(
                value["outlier_filtering_strength"]
            )
        )
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
    if data.get("AdaptationSpeed") is not None:
        import capo_cloudwatch.types.anomaly_detector_adaptation_speed

        out["adaptation_speed"] = (
            capo_cloudwatch.types.anomaly_detector_adaptation_speed.deserialize_aws_json_1_0(
                data["AdaptationSpeed"]
            )
        )
    if data.get("OutlierFilteringStrength") is not None:
        import capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength

        out["outlier_filtering_strength"] = (
            capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength.deserialize_aws_json_1_0(
                data["OutlierFilteringStrength"]
            )
        )
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
    if "adaptation_speed" in value:
        import capo_cloudwatch.types.anomaly_detector_adaptation_speed

        capo_cloudwatch.types.anomaly_detector_adaptation_speed.serialize_query(
            value["adaptation_speed"], pairs, f"{key_prefix}AdaptationSpeed"
        )
    if "outlier_filtering_strength" in value:
        import capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength

        capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength.serialize_query(
            value["outlier_filtering_strength"],
            pairs,
            f"{key_prefix}OutlierFilteringStrength",
        )


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
    child_adaptation_speed = el.find("AdaptationSpeed")
    if child_adaptation_speed is not None:
        import capo_cloudwatch.types.anomaly_detector_adaptation_speed

        out["adaptation_speed"] = (
            capo_cloudwatch.types.anomaly_detector_adaptation_speed.deserialize_query(
                child_adaptation_speed
            )
        )
    child_outlier_filtering_strength = el.find("OutlierFilteringStrength")
    if child_outlier_filtering_strength is not None:
        import capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength

        out["outlier_filtering_strength"] = (
            capo_cloudwatch.types.anomaly_detector_outlier_filtering_strength.deserialize_query(
                child_outlier_filtering_strength
            )
        )
    return out
