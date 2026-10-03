"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AnomalyDetector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.anomaly_detector_arn
    import capo_cloudwatch_logs.types.anomaly_detector_status
    import capo_cloudwatch_logs.types.anomaly_visibility_time
    import capo_cloudwatch_logs.types.detector_name
    import capo_cloudwatch_logs.types.epoch_millis
    import capo_cloudwatch_logs.types.evaluation_frequency
    import capo_cloudwatch_logs.types.filter_pattern
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.log_group_arn_list


class AnomalyDetector(TypedDict, closed=True):
    anomaly_detector_arn: NotRequired[
        "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn"
    ]
    """<p>The ARN of the anomaly detector.</p>"""
    detector_name: NotRequired["capo_cloudwatch_logs.types.detector_name.DetectorName"]
    """<p>The name of the anomaly detector.</p>"""
    log_group_arn_list: NotRequired[
        "capo_cloudwatch_logs.types.log_group_arn_list.LogGroupArnList"
    ]
    """<p>A list of the ARNs of the log groups that this anomaly detector watches.</p>"""
    evaluation_frequency: NotRequired[
        "capo_cloudwatch_logs.types.evaluation_frequency.EvaluationFrequency"
    ]
    """<p>Specifies how often the anomaly detector runs and look for anomalies.</p>"""
    filter_pattern: NotRequired[
        "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    anomaly_detector_status: NotRequired[
        "capo_cloudwatch_logs.types.anomaly_detector_status.AnomalyDetectorStatus"
    ]
    """<p>Specifies the current status of the anomaly detector. To pause an anomaly detector, use the <code>enabled</code> parameter in the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateLogAnomalyDetector.html">UpdateLogAnomalyDetector</a> operation.</p>"""
    kms_key_id: NotRequired["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key assigned to this anomaly detector, if any.</p>"""
    creation_time_stamp: "capo_cloudwatch_logs.types.epoch_millis.EpochMillis"
    """<p>The date and time when this anomaly detector was created.</p>"""
    last_modified_time_stamp: "capo_cloudwatch_logs.types.epoch_millis.EpochMillis"
    """<p>The date and time when this anomaly detector was most recently modified.</p>"""
    anomaly_visibility_time: NotRequired[
        "capo_cloudwatch_logs.types.anomaly_visibility_time.AnomalyVisibilityTime"
    ]
    """<p>The number of days used as the life cycle of anomalies. After this time, anomalies are automatically baselined and the anomaly detector model will treat new occurrences of similar event as normal. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyDetector) -> dict:
    out: dict = {}
    if "anomaly_detector_arn" in value:
        out["anomalyDetectorArn"] = value["anomaly_detector_arn"]
    if "detector_name" in value:
        out["detectorName"] = value["detector_name"]
    if "log_group_arn_list" in value:
        import capo_cloudwatch_logs.types.log_group_arn_list

        out["logGroupArnList"] = (
            capo_cloudwatch_logs.types.log_group_arn_list.serialize_aws_json_1_1(
                value["log_group_arn_list"]
            )
        )
    if "evaluation_frequency" in value:
        import capo_cloudwatch_logs.types.evaluation_frequency

        out["evaluationFrequency"] = (
            capo_cloudwatch_logs.types.evaluation_frequency.serialize_aws_json_1_1(
                value["evaluation_frequency"]
            )
        )
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    if "anomaly_detector_status" in value:
        import capo_cloudwatch_logs.types.anomaly_detector_status

        out["anomalyDetectorStatus"] = (
            capo_cloudwatch_logs.types.anomaly_detector_status.serialize_aws_json_1_1(
                value["anomaly_detector_status"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    out["creationTimeStamp"] = value.get("creation_time_stamp", 0)
    out["lastModifiedTimeStamp"] = value.get("last_modified_time_stamp", 0)
    if "anomaly_visibility_time" in value:
        out["anomalyVisibilityTime"] = value["anomaly_visibility_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnomalyDetector:
    out: AnomalyDetector = {}  # type: ignore[typeddict-item]
    if data.get("anomalyDetectorArn") is not None:
        out["anomaly_detector_arn"] = data["anomalyDetectorArn"]
    if data.get("detectorName") is not None:
        out["detector_name"] = data["detectorName"]
    if data.get("logGroupArnList") is not None:
        import capo_cloudwatch_logs.types.log_group_arn_list

        out["log_group_arn_list"] = (
            capo_cloudwatch_logs.types.log_group_arn_list.deserialize_aws_json_1_1(
                data["logGroupArnList"]
            )
        )
    if data.get("evaluationFrequency") is not None:
        import capo_cloudwatch_logs.types.evaluation_frequency

        out["evaluation_frequency"] = (
            capo_cloudwatch_logs.types.evaluation_frequency.deserialize_aws_json_1_1(
                data["evaluationFrequency"]
            )
        )
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    if data.get("anomalyDetectorStatus") is not None:
        import capo_cloudwatch_logs.types.anomaly_detector_status

        out["anomaly_detector_status"] = (
            capo_cloudwatch_logs.types.anomaly_detector_status.deserialize_aws_json_1_1(
                data["anomalyDetectorStatus"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("creationTimeStamp") is not None:
        out["creation_time_stamp"] = data["creationTimeStamp"]
    else:
        out["creation_time_stamp"] = 0
    if data.get("lastModifiedTimeStamp") is not None:
        out["last_modified_time_stamp"] = data["lastModifiedTimeStamp"]
    else:
        out["last_modified_time_stamp"] = 0
    if data.get("anomalyVisibilityTime") is not None:
        out["anomaly_visibility_time"] = data["anomalyVisibilityTime"]
    return out
