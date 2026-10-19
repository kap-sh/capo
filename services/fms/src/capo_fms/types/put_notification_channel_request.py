"""Generated from Smithy shape ``com.amazonaws.fms#PutNotificationChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fms.types.resource_arn


class PutNotificationChannelRequest(TypedDict, closed=True):
    sns_topic_arn: "capo_fms.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the SNS topic that collects notifications from Firewall Manager.</p>"""
    sns_role_name: "capo_fms.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record Firewall Manager activity. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutNotificationChannelRequest) -> dict:
    out: dict = {}
    out["SnsTopicArn"] = value["sns_topic_arn"]
    out["SnsRoleName"] = value["sns_role_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutNotificationChannelRequest:
    out: PutNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    else:
        out["sns_topic_arn"] = ""
    if data.get("SnsRoleName") is not None:
        out["sns_role_name"] = data["SnsRoleName"]
    else:
        out["sns_role_name"] = ""
    return out
