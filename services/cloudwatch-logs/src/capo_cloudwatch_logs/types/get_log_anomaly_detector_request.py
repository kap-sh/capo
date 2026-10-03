"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogAnomalyDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.anomaly_detector_arn


class GetLogAnomalyDetectorRequest(TypedDict, closed=True):
    anomaly_detector_arn: (
        "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn"
    )
    """<p>The ARN of the anomaly detector to retrieve information about. You can find the ARNs of log anomaly detectors in your account by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListLogAnomalyDetectors.html">ListLogAnomalyDetectors</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogAnomalyDetectorRequest) -> dict:
    out: dict = {}
    out["anomalyDetectorArn"] = value["anomaly_detector_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogAnomalyDetectorRequest:
    out: GetLogAnomalyDetectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("anomalyDetectorArn") is not None:
        out["anomaly_detector_arn"] = data["anomalyDetectorArn"]
    else:
        raise DeserializationError(
            "GetLogAnomalyDetectorRequest.anomaly_detector_arn required"
        )
    return out
