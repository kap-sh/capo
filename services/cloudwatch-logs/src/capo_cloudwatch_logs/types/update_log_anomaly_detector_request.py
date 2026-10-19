"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateLogAnomalyDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.anomaly_detector_arn
    import capo_cloudwatch_logs.types.anomaly_visibility_time
    import capo_cloudwatch_logs.types.boolean
    import capo_cloudwatch_logs.types.evaluation_frequency
    import capo_cloudwatch_logs.types.filter_pattern


class UpdateLogAnomalyDetectorRequest(TypedDict, closed=True):
    anomaly_detector_arn: (
        "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn"
    )
    """<p>The ARN of the anomaly detector that you want to update.</p>"""
    evaluation_frequency: NotRequired[
        "capo_cloudwatch_logs.types.evaluation_frequency.EvaluationFrequency"
    ]
    """<p>Specifies how often the anomaly detector runs and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then setting <code>evaluationFrequency</code> to <code>FIFTEEN_MIN</code> might be appropriate.</p>"""
    filter_pattern: NotRequired[
        "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    anomaly_visibility_time: NotRequired[
        "capo_cloudwatch_logs.types.anomaly_visibility_time.AnomalyVisibilityTime"
    ]
    """<p>The number of days to use as the life cycle of anomalies. After this time, anomalies are automatically baselined and the anomaly detector model will treat new occurrences of similar event as normal. Therefore, if you do not correct the cause of an anomaly during this time, it will be considered normal going forward and will not be detected.</p>"""
    enabled: "capo_cloudwatch_logs.types.boolean.Boolean"
    """<p>Use this parameter to pause or restart the anomaly detector. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLogAnomalyDetectorRequest) -> dict:
    out: dict = {}
    out["anomalyDetectorArn"] = value["anomaly_detector_arn"]
    if "evaluation_frequency" in value:
        import capo_cloudwatch_logs.types.evaluation_frequency

        out["evaluationFrequency"] = (
            capo_cloudwatch_logs.types.evaluation_frequency.serialize_aws_json_1_1(
                value["evaluation_frequency"]
            )
        )
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    if "anomaly_visibility_time" in value:
        out["anomalyVisibilityTime"] = value["anomaly_visibility_time"]
    out["enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLogAnomalyDetectorRequest:
    out: UpdateLogAnomalyDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("anomalyDetectorArn") is not None:
        out["anomaly_detector_arn"] = data["anomalyDetectorArn"]
    else:
        out["anomaly_detector_arn"] = ""
    if data.get("evaluationFrequency") is not None:
        import capo_cloudwatch_logs.types.evaluation_frequency

        out["evaluation_frequency"] = (
            capo_cloudwatch_logs.types.evaluation_frequency.deserialize_aws_json_1_1(
                data["evaluationFrequency"]
            )
        )
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    if data.get("anomalyVisibilityTime") is not None:
        out["anomaly_visibility_time"] = data["anomalyVisibilityTime"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
