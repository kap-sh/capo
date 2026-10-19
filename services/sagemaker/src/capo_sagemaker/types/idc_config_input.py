"""Generated from Smithy shape ``com.amazonaws.sagemaker#IdcConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.instance_arn


class IdcConfigInput(TypedDict, closed=True):
    instance_arn: "capo_sagemaker.types.instance_arn.InstanceArn"
    """<p>The ARN of the Amazon Web Services IAM Identity Center instance that the SageMaker Partner AI App uses to authenticate users.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdcConfigInput) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdcConfigInput:
    out: IdcConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    return out
