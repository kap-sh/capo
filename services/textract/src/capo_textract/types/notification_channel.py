"""Generated from Smithy shape ``com.amazonaws.textract#NotificationChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.role_arn
    import capo_textract.types.sns_topic_arn


class NotificationChannel(TypedDict, closed=True):
    sns_topic_arn: "capo_textract.types.sns_topic_arn.SNSTopicArn"
    """<p>The Amazon SNS topic that Amazon Textract posts the completion status to.</p>"""
    role_arn: "capo_textract.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that gives Amazon Textract publishing permissions to the Amazon SNS topic. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationChannel) -> dict:
    out: dict = {}
    out["SNSTopicArn"] = value["sns_topic_arn"]
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationChannel:
    out: NotificationChannel = {}  # type: ignore[typeddict-item]
    if data.get("SNSTopicArn") is not None:
        out["sns_topic_arn"] = data["SNSTopicArn"]
    else:
        out["sns_topic_arn"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
