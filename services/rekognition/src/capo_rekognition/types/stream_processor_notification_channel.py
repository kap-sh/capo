"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorNotificationChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.sns_topic_arn


class StreamProcessorNotificationChannel(TypedDict, closed=True):
    sns_topic_arn: "capo_rekognition.types.sns_topic_arn.SNSTopicArn"
    """<p> The Amazon Resource Number (ARN) of the Amazon Amazon Simple Notification Service topic to which Amazon Rekognition posts the completion status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorNotificationChannel) -> dict:
    out: dict = {}
    out["SNSTopicArn"] = value["sns_topic_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessorNotificationChannel:
    out: StreamProcessorNotificationChannel = {}  # type: ignore[typeddict-item]
    if data.get("SNSTopicArn") is not None:
        out["sns_topic_arn"] = data["SNSTopicArn"]
    else:
        out["sns_topic_arn"] = ""
    return out
