"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateLogAnomalyDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.anomaly_visibility_time
    import capo_cloudwatch_logs.types.detector_kms_key_arn
    import capo_cloudwatch_logs.types.detector_name
    import capo_cloudwatch_logs.types.evaluation_frequency
    import capo_cloudwatch_logs.types.filter_pattern
    import capo_cloudwatch_logs.types.log_group_arn_list
    import capo_cloudwatch_logs.types.tags


class CreateLogAnomalyDetectorRequest(TypedDict, closed=True):
    log_group_arn_list: "capo_cloudwatch_logs.types.log_group_arn_list.LogGroupArnList"
    """<p>An array containing the ARN of the log group that this anomaly detector will watch. You can specify only one log group ARN.</p>"""
    detector_name: NotRequired["capo_cloudwatch_logs.types.detector_name.DetectorName"]
    """<p>A name for this anomaly detector.</p>"""
    evaluation_frequency: NotRequired[
        "capo_cloudwatch_logs.types.evaluation_frequency.EvaluationFrequency"
    ]
    """<p>Specifies how often the anomaly detector is to run and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then 15 minutes might be a good setting for <code>evaluationFrequency</code> .</p>"""
    filter_pattern: NotRequired[
        "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    """<p>You can use this parameter to limit the anomaly detection model to examine only log events that match the pattern you specify here. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html">Filter and Pattern Syntax</a>.</p>"""
    kms_key_id: NotRequired[
        "capo_cloudwatch_logs.types.detector_kms_key_arn.DetectorKmsKeyArn"
    ]
    """<p>Optionally assigns a KMS key to secure this anomaly detector and its findings. If a key is assigned, the anomalies found and the model used by this detector are encrypted at rest with the key. If a key is assigned to an anomaly detector, a user must have permissions for both this key and for the anomaly detector to retrieve information about the anomalies that it finds.</p> <p> Make sure the value provided is a valid KMS key ARN. For more information about using a KMS key and to see the required IAM policy, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-KMS.html">Use a KMS key with an anomaly detector</a>.</p>"""
    anomaly_visibility_time: NotRequired[
        "capo_cloudwatch_logs.types.anomaly_visibility_time.AnomalyVisibilityTime"
    ]
    """<p>The number of days to have visibility on an anomaly. After this time period has elapsed for an anomaly, it will be automatically baselined and the anomaly detector will treat new occurrences of a similar anomaly as normal. Therefore, if you do not correct the cause of an anomaly during the time period specified in <code>anomalyVisibilityTime</code>, it will be considered normal going forward and will not be detected as an anomaly.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLogAnomalyDetectorRequest) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.log_group_arn_list

    out["logGroupArnList"] = (
        capo_cloudwatch_logs.types.log_group_arn_list.serialize_aws_json_1_1(
            value["log_group_arn_list"]
        )
    )
    if "detector_name" in value:
        out["detectorName"] = value["detector_name"]
    if "evaluation_frequency" in value:
        import capo_cloudwatch_logs.types.evaluation_frequency

        out["evaluationFrequency"] = (
            capo_cloudwatch_logs.types.evaluation_frequency.serialize_aws_json_1_1(
                value["evaluation_frequency"]
            )
        )
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "anomaly_visibility_time" in value:
        out["anomalyVisibilityTime"] = value["anomaly_visibility_time"]
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLogAnomalyDetectorRequest:
    out: CreateLogAnomalyDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupArnList") is not None:
        import capo_cloudwatch_logs.types.log_group_arn_list

        out["log_group_arn_list"] = (
            capo_cloudwatch_logs.types.log_group_arn_list.deserialize_aws_json_1_1(
                data["logGroupArnList"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLogAnomalyDetectorRequest.log_group_arn_list required"
        )
    if data.get("detectorName") is not None:
        out["detector_name"] = data["detectorName"]
    if data.get("evaluationFrequency") is not None:
        import capo_cloudwatch_logs.types.evaluation_frequency

        out["evaluation_frequency"] = (
            capo_cloudwatch_logs.types.evaluation_frequency.deserialize_aws_json_1_1(
                data["evaluationFrequency"]
            )
        )
    if data.get("filterPattern") is not None:
        out["filter_pattern"] = data["filterPattern"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("anomalyVisibilityTime") is not None:
        out["anomaly_visibility_time"] = data["anomalyVisibilityTime"]
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
