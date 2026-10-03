"""Generated from Smithy shape ``com.amazonaws.firehose#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.role_arn
    import capo_firehose.types.security_group_id_list
    import capo_firehose.types.subnet_id_list


class VpcConfiguration(TypedDict, closed=True):
    subnet_ids: "capo_firehose.types.subnet_id_list.SubnetIdList"
    """<p>The IDs of the subnets that you want Firehose to use to create ENIs in the VPC of the Amazon OpenSearch Service destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon OpenSearch Service endpoints. Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.</p> <p>The number of ENIs that Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Firehose can create up to three ENIs for this Firehose stream for each of the subnets specified here. For more information about ENI quota, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-enis">Network Interfaces </a> in the Amazon VPC Quotas topic.</p>"""
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p>The ARN of the IAM role that you want the Firehose stream to use to create endpoints in the destination VPC. You can use your existing Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Firehose service principal and that it grants the following permissions:</p> <ul> <li> <p> <code>ec2:DescribeVpcs</code> </p> </li> <li> <p> <code>ec2:DescribeVpcAttribute</code> </p> </li> <li> <p> <code>ec2:DescribeSubnets</code> </p> </li> <li> <p> <code>ec2:DescribeSecurityGroups</code> </p> </li> <li> <p> <code>ec2:DescribeNetworkInterfaces</code> </p> </li> <li> <p> <code>ec2:CreateNetworkInterface</code> </p> </li> <li> <p> <code>ec2:CreateNetworkInterfacePermission</code> </p> </li> <li> <p> <code>ec2:DeleteNetworkInterface</code> </p> </li> </ul> <important> <p>When you specify subnets for delivering data to the destination in a private VPC, make sure you have enough number of free IP addresses in chosen subnets. If there is no available free IP address in a specified subnet, Firehose cannot create or add ENIs for the data delivery in the private VPC, and the delivery will be degraded or fail.</p> </important>"""
    security_group_ids: "capo_firehose.types.security_group_id_list.SecurityGroupIdList"
    """<p>The IDs of the security groups that you want Firehose to use when it creates ENIs in the VPC of the Amazon OpenSearch Service destination. You can use the same security group that the Amazon OpenSearch Service domain uses or different ones. If you specify different security groups here, ensure that they allow outbound HTTPS traffic to the Amazon OpenSearch Service domain's security group. Also ensure that the Amazon OpenSearch Service domain's security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your delivery stream and the Amazon OpenSearch Service domain, make sure the security group inbound rule allows HTTPS traffic. For more information about security group rules, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules">Security group rules</a> in the Amazon VPC documentation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfiguration) -> dict:
    out: dict = {}
    import capo_firehose.types.subnet_id_list

    out["SubnetIds"] = capo_firehose.types.subnet_id_list.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    out["RoleARN"] = value["role_arn"]
    import capo_firehose.types.security_group_id_list

    out["SecurityGroupIds"] = (
        capo_firehose.types.security_group_id_list.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_firehose.types.subnet_id_list

        out["subnet_ids"] = capo_firehose.types.subnet_id_list.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    else:
        raise DeserializationError("VpcConfiguration.subnet_ids required")
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("VpcConfiguration.role_arn required")
    if data.get("SecurityGroupIds") is not None:
        import capo_firehose.types.security_group_id_list

        out["security_group_ids"] = (
            capo_firehose.types.security_group_id_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfiguration.security_group_ids required")
    return out
