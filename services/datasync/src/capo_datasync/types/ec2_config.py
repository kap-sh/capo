"""Generated from Smithy shape ``com.amazonaws.datasync#Ec2Config``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.ec2_security_group_arn_list
    import capo_datasync.types.ec2_subnet_arn


class Ec2Config(TypedDict, closed=True):
    subnet_arn: "capo_datasync.types.ec2_subnet_arn.Ec2SubnetArn"
    """<p>Specifies the ARN of a subnet where DataSync creates the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces">network interfaces</a> for managing traffic during your transfer.</p> <p>The subnet must be located:</p> <ul> <li> <p>In the same virtual private cloud (VPC) as the Amazon EFS file system.</p> </li> <li> <p>In the same Availability Zone as at least one mount target for the Amazon EFS file system.</p> </li> </ul> <note> <p>You don't need to specify a subnet that includes a file system mount target.</p> </note>"""
    security_group_arns: (
        "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    )
    """<p>Specifies the Amazon Resource Names (ARNs) of the security groups associated with an Amazon EFS file system's mount target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2Config) -> dict:
    out: dict = {}
    out["SubnetArn"] = value["subnet_arn"]
    import capo_datasync.types.ec2_security_group_arn_list

    out["SecurityGroupArns"] = (
        capo_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
            value["security_group_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Ec2Config:
    out: Ec2Config = {}  # type: ignore[typeddict-item]
    if data.get("SubnetArn") is not None:
        out["subnet_arn"] = data["SubnetArn"]
    else:
        raise DeserializationError("Ec2Config.subnet_arn required")
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    else:
        raise DeserializationError("Ec2Config.security_group_arns required")
    return out
