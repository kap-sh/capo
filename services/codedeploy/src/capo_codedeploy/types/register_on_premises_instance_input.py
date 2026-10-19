"""Generated from Smithy shape ``com.amazonaws.codedeploy#RegisterOnPremisesInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.iam_session_arn
    import capo_codedeploy.types.iam_user_arn
    import capo_codedeploy.types.instance_name


class RegisterOnPremisesInstanceInput(TypedDict, closed=True):
    instance_name: "capo_codedeploy.types.instance_name.InstanceName"
    """<p>The name of the on-premises instance to register.</p>"""
    iam_session_arn: NotRequired["capo_codedeploy.types.iam_session_arn.IamSessionArn"]
    """<p>The ARN of the IAM session to associate with the on-premises instance.</p>"""
    iam_user_arn: NotRequired["capo_codedeploy.types.iam_user_arn.IamUserArn"]
    """<p>The ARN of the user to associate with the on-premises instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterOnPremisesInstanceInput) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    if "iam_session_arn" in value:
        out["iamSessionArn"] = value["iam_session_arn"]
    if "iam_user_arn" in value:
        out["iamUserArn"] = value["iam_user_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterOnPremisesInstanceInput:
    out: RegisterOnPremisesInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        out["instance_name"] = ""
    if data.get("iamSessionArn") is not None:
        out["iam_session_arn"] = data["iamSessionArn"]
    if data.get("iamUserArn") is not None:
        out["iam_user_arn"] = data["iamUserArn"]
    return out
