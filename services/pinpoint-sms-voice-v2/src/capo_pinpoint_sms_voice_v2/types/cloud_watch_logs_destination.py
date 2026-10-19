"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CloudWatchLogsDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.iam_role_arn
    import capo_pinpoint_sms_voice_v2.types.log_group_arn


class CloudWatchLogsDestination(TypedDict, closed=True):
    iam_role_arn: "capo_pinpoint_sms_voice_v2.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of an Identity and Access Management role that is able to write event data to an Amazon CloudWatch destination.</p>"""
    log_group_arn: "capo_pinpoint_sms_voice_v2.types.log_group_arn.LogGroupArn"
    """<p>The name of the Amazon CloudWatch log group that you want to record events in. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudWatchLogsDestination) -> dict:
    out: dict = {}
    out["IamRoleArn"] = value["iam_role_arn"]
    out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudWatchLogsDestination:
    out: CloudWatchLogsDestination = {}  # type: ignore[typeddict-item]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        out["iam_role_arn"] = ""
    if data.get("LogGroupArn") is not None:
        out["log_group_arn"] = data["LogGroupArn"]
    else:
        out["log_group_arn"] = ""
    return out
