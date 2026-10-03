"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Alarms``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.iam_arn


class Alarms(TypedDict, closed=True):
    alarm_role_arn: "capo_iotsitewise.types.iam_arn.IamArn"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IAM role that allows the alarm to perform actions and access Amazon Web Services resources and services, such as IoT Events.</p>"""
    notification_lambda_arn: NotRequired["capo_iotsitewise.types.arn.ARN"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the Lambda function that manages alarm notifications. For more information, see <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html">Managing alarm notifications</a> in the <i>IoT Events Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Alarms) -> dict:
    out: dict = {}
    out["alarmRoleArn"] = value["alarm_role_arn"]
    if "notification_lambda_arn" in value:
        out["notificationLambdaArn"] = value["notification_lambda_arn"]
    return out


def deserialize_json(data: dict) -> Alarms:
    out: Alarms = {}  # type: ignore[typeddict-item]
    if data.get("alarmRoleArn") is not None:
        out["alarm_role_arn"] = data["alarmRoleArn"]
    else:
        raise DeserializationError("Alarms.alarm_role_arn required")
    if data.get("notificationLambdaArn") is not None:
        out["notification_lambda_arn"] = data["notificationLambdaArn"]
    return out
