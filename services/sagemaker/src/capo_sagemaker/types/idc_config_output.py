"""Generated from Smithy shape ``com.amazonaws.sagemaker#IdcConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.application_arn
    import capo_sagemaker.types.instance_arn


class IdcConfigOutput(TypedDict, closed=True):
    instance_arn: "capo_sagemaker.types.instance_arn.InstanceArn"
    """<p>The ARN of the Amazon Web Services IAM Identity Center instance that the SageMaker Partner AI App uses to authenticate users.</p>"""
    application_arn: NotRequired["capo_sagemaker.types.application_arn.ApplicationArn"]
    """<p>The ARN of the Amazon Web Services IAM Identity Center application that SageMaker creates for the SageMaker Partner AI App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdcConfigOutput) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdcConfigOutput:
    out: IdcConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    return out
