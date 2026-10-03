"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateAnomalyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.anomaly_detector_arn
    import capo_cloudwatch_logs.types.anomaly_id
    import capo_cloudwatch_logs.types.baseline
    import capo_cloudwatch_logs.types.pattern_id
    import capo_cloudwatch_logs.types.suppression_period
    import capo_cloudwatch_logs.types.suppression_type


class UpdateAnomalyRequest(TypedDict, closed=True):
    anomaly_id: NotRequired["capo_cloudwatch_logs.types.anomaly_id.AnomalyId"]
    """<p>If you are suppressing or unsuppressing an anomaly, specify its unique ID here. You can find anomaly IDs by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.html">ListAnomalies</a> operation.</p>"""
    pattern_id: NotRequired["capo_cloudwatch_logs.types.pattern_id.PatternId"]
    """<p>If you are suppressing or unsuppressing an pattern, specify its unique ID here. You can find pattern IDs by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.html">ListAnomalies</a> operation.</p>"""
    anomaly_detector_arn: (
        "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn"
    )
    """<p>The ARN of the anomaly detector that this operation is to act on.</p>"""
    suppression_type: NotRequired[
        "capo_cloudwatch_logs.types.suppression_type.SuppressionType"
    ]
    """<p>Use this to specify whether the suppression to be temporary or infinite. If you specify <code>LIMITED</code>, you must also specify a <code>suppressionPeriod</code>. If you specify <code>INFINITE</code>, any value for <code>suppressionPeriod</code> is ignored. </p>"""
    suppression_period: NotRequired[
        "capo_cloudwatch_logs.types.suppression_period.SuppressionPeriod"
    ]
    """<p>If you are temporarily suppressing an anomaly or pattern, use this structure to specify how long the suppression is to last.</p>"""
    baseline: NotRequired["capo_cloudwatch_logs.types.baseline.Baseline"]
    """<p>Set this to <code>true</code> to prevent CloudWatch Logs from displaying this behavior as an anomaly in the future. The behavior is then treated as baseline behavior. However, if similar but more severe occurrences of this behavior occur in the future, those will still be reported as anomalies. </p> <p>The default is <code>false</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAnomalyRequest) -> dict:
    out: dict = {}
    if "anomaly_id" in value:
        out["anomalyId"] = value["anomaly_id"]
    if "pattern_id" in value:
        out["patternId"] = value["pattern_id"]
    out["anomalyDetectorArn"] = value["anomaly_detector_arn"]
    if "suppression_type" in value:
        import capo_cloudwatch_logs.types.suppression_type

        out["suppressionType"] = (
            capo_cloudwatch_logs.types.suppression_type.serialize_aws_json_1_1(
                value["suppression_type"]
            )
        )
    if "suppression_period" in value:
        import capo_cloudwatch_logs.types.suppression_period

        out["suppressionPeriod"] = (
            capo_cloudwatch_logs.types.suppression_period.serialize_aws_json_1_1(
                value["suppression_period"]
            )
        )
    if "baseline" in value:
        out["baseline"] = value["baseline"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAnomalyRequest:
    out: UpdateAnomalyRequest = {}  # type: ignore[typeddict-item]
    if data.get("anomalyId") is not None:
        out["anomaly_id"] = data["anomalyId"]
    if data.get("patternId") is not None:
        out["pattern_id"] = data["patternId"]
    if data.get("anomalyDetectorArn") is not None:
        out["anomaly_detector_arn"] = data["anomalyDetectorArn"]
    else:
        raise DeserializationError("UpdateAnomalyRequest.anomaly_detector_arn required")
    if data.get("suppressionType") is not None:
        import capo_cloudwatch_logs.types.suppression_type

        out["suppression_type"] = (
            capo_cloudwatch_logs.types.suppression_type.deserialize_aws_json_1_1(
                data["suppressionType"]
            )
        )
    if data.get("suppressionPeriod") is not None:
        import capo_cloudwatch_logs.types.suppression_period

        out["suppression_period"] = (
            capo_cloudwatch_logs.types.suppression_period.deserialize_aws_json_1_1(
                data["suppressionPeriod"]
            )
        )
    if data.get("baseline") is not None:
        out["baseline"] = data["baseline"]
    return out
