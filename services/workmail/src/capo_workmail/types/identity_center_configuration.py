"""Generated from Smithy shape ``com.amazonaws.workmail#IdentityCenterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.application_arn
    import capo_workmail.types.instance_arn


class IdentityCenterConfiguration(TypedDict, closed=True):
    instance_arn: "capo_workmail.types.instance_arn.InstanceArn"
    """<p> The Amazon Resource Name (ARN) of the of IAM Identity Center instance. Must be in the same AWS account and region as WorkMail organization.</p>"""
    application_arn: "capo_workmail.types.application_arn.ApplicationArn"
    """<p> The Amazon Resource Name (ARN) of IAMIdentity Center Application for WorkMail. Must be created by the WorkMail API, see CreateIdentityCenterApplication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityCenterConfiguration) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityCenterConfiguration:
    out: IdentityCenterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    return out
