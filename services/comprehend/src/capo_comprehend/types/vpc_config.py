"""Generated from Smithy shape ``com.amazonaws.comprehend#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.security_group_ids
    import capo_comprehend.types.subnets


class VpcConfig(TypedDict, closed=True):
    security_group_ids: "capo_comprehend.types.security_group_ids.SecurityGroupIds"
    """<p>The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html">Security Groups for your VPC</a>. </p>"""
    subnets: "capo_comprehend.types.subnets.Subnets"
    """<p>The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">VPCs and Subnets</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfig) -> dict:
    out: dict = {}
    import capo_comprehend.types.security_group_ids

    out["SecurityGroupIds"] = (
        capo_comprehend.types.security_group_ids.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    import capo_comprehend.types.subnets

    out["Subnets"] = capo_comprehend.types.subnets.serialize_aws_json_1_1(
        value["subnets"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("SecurityGroupIds") is not None:
        import capo_comprehend.types.security_group_ids

        out["security_group_ids"] = (
            capo_comprehend.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfig.security_group_ids required")
    if data.get("Subnets") is not None:
        import capo_comprehend.types.subnets

        out["subnets"] = capo_comprehend.types.subnets.deserialize_aws_json_1_1(
            data["Subnets"]
        )
    else:
        raise DeserializationError("VpcConfig.subnets required")
    return out
