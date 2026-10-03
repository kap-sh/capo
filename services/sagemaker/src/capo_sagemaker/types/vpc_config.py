"""Generated from Smithy shape ``com.amazonaws.sagemaker#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.subnets
    import capo_sagemaker.types.vpc_security_group_ids


class VpcConfig(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "capo_sagemaker.types.vpc_security_group_ids.VpcSecurityGroupIds"
    ]
    """<p>The VPC security group IDs, in the form <code>sg-xxxxxxxx</code>. Specify the security groups for the VPC that is specified in the <code>Subnets</code> field.</p>"""
    subnets: NotRequired["capo_sagemaker.types.subnets.Subnets"]
    """<p>The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html">Supported Instance Types and Availability Zones</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfig) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import capo_sagemaker.types.vpc_security_group_ids

        out["SecurityGroupIds"] = (
            capo_sagemaker.types.vpc_security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "subnets" in value:
        import capo_sagemaker.types.subnets

        out["Subnets"] = capo_sagemaker.types.subnets.serialize_aws_json_1_1(
            value["subnets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("SecurityGroupIds") is not None:
        import capo_sagemaker.types.vpc_security_group_ids

        out["security_group_ids"] = (
            capo_sagemaker.types.vpc_security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if data.get("Subnets") is not None:
        import capo_sagemaker.types.subnets

        out["subnets"] = capo_sagemaker.types.subnets.deserialize_aws_json_1_1(
            data["Subnets"]
        )
    return out
