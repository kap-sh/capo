"""Generated from Smithy shape ``com.amazonaws.sagemaker#IamPolicyConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.enabled_or_disabled


class IamPolicyConstraints(TypedDict, closed=True):
    source_ip: NotRequired["capo_sagemaker.types.enabled_or_disabled.EnabledOrDisabled"]
    """<p>When <code>SourceIp</code> is <code>Enabled</code> the worker's IP address when a task is rendered in the worker portal is added to the IAM policy as a <code>Condition</code> used to generate the Amazon S3 presigned URL. This IP address is checked by Amazon S3 and must match in order for the Amazon S3 resource to be rendered in the worker portal.</p>"""
    vpc_source_ip: NotRequired[
        "capo_sagemaker.types.enabled_or_disabled.EnabledOrDisabled"
    ]
    """<p>When <code>VpcSourceIp</code> is <code>Enabled</code> the worker's IP address when a task is rendered in private worker portal inside the VPC is added to the IAM policy as a <code>Condition</code> used to generate the Amazon S3 presigned URL. To render the task successfully Amazon S3 checks that the presigned URL is being accessed over an Amazon S3 VPC Endpoint, and that the worker's IP address matches the IP address in the IAM policy. To learn more about configuring private worker portal, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/samurai-vpc-worker-portal.html">Use Amazon VPC mode from a private worker portal</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IamPolicyConstraints) -> dict:
    out: dict = {}
    if "source_ip" in value:
        import capo_sagemaker.types.enabled_or_disabled

        out["SourceIp"] = (
            capo_sagemaker.types.enabled_or_disabled.serialize_aws_json_1_1(
                value["source_ip"]
            )
        )
    if "vpc_source_ip" in value:
        import capo_sagemaker.types.enabled_or_disabled

        out["VpcSourceIp"] = (
            capo_sagemaker.types.enabled_or_disabled.serialize_aws_json_1_1(
                value["vpc_source_ip"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IamPolicyConstraints:
    out: IamPolicyConstraints = {}  # type: ignore[typeddict-item]
    if data.get("SourceIp") is not None:
        import capo_sagemaker.types.enabled_or_disabled

        out["source_ip"] = (
            capo_sagemaker.types.enabled_or_disabled.deserialize_aws_json_1_1(
                data["SourceIp"]
            )
        )
    if data.get("VpcSourceIp") is not None:
        import capo_sagemaker.types.enabled_or_disabled

        out["vpc_source_ip"] = (
            capo_sagemaker.types.enabled_or_disabled.deserialize_aws_json_1_1(
                data["VpcSourceIp"]
            )
        )
    return out
