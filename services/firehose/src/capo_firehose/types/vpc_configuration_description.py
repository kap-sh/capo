"""Generated from Smithy shape ``com.amazonaws.firehose#VpcConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.non_empty_string_without_whitespace
    import capo_firehose.types.role_arn
    import capo_firehose.types.security_group_id_list
    import capo_firehose.types.subnet_id_list


class VpcConfigurationDescription(TypedDict, closed=True):
    subnet_ids: "capo_firehose.types.subnet_id_list.SubnetIdList"
    """<p>The IDs of the subnets that Firehose uses to create ENIs in the VPC of the Amazon OpenSearch Service destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon OpenSearch Service endpoints. Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.</p> <p>The number of ENIs that Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Firehose can create up to three ENIs for this Firehose stream for each of the subnets specified here. For more information about ENI quota, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-enis">Network Interfaces </a> in the Amazon VPC Quotas topic.</p>"""
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p>The ARN of the IAM role that the Firehose stream uses to create endpoints in the destination VPC. You can use your existing Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Firehose service principal and that it grants the following permissions:</p> <ul> <li> <p> <code>ec2:DescribeVpcs</code> </p> </li> <li> <p> <code>ec2:DescribeVpcAttribute</code> </p> </li> <li> <p> <code>ec2:DescribeSubnets</code> </p> </li> <li> <p> <code>ec2:DescribeSecurityGroups</code> </p> </li> <li> <p> <code>ec2:DescribeNetworkInterfaces</code> </p> </li> <li> <p> <code>ec2:CreateNetworkInterface</code> </p> </li> <li> <p> <code>ec2:CreateNetworkInterfacePermission</code> </p> </li> <li> <p> <code>ec2:DeleteNetworkInterface</code> </p> </li> </ul> <p>If you revoke these permissions after you create the Firehose stream, Firehose can't scale out by creating more ENIs when necessary. You might therefore see a degradation in performance.</p>"""
    security_group_ids: "capo_firehose.types.security_group_id_list.SecurityGroupIdList"
    """<p>The IDs of the security groups that Firehose uses when it creates ENIs in the VPC of the Amazon OpenSearch Service destination. You can use the same security group that the Amazon ES domain uses or different ones. If you specify different security groups, ensure that they allow outbound HTTPS traffic to the Amazon OpenSearch Service domain's security group. Also ensure that the Amazon OpenSearch Service domain's security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your Firehose stream and the Amazon OpenSearch Service domain, make sure the security group inbound rule allows HTTPS traffic. For more information about security group rules, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules">Security group rules</a> in the Amazon VPC documentation.</p>"""
    vpc_id: "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    """<p>The ID of the Amazon OpenSearch Service destination's VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfigurationDescription) -> dict:
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
    out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfigurationDescription:
    out: VpcConfigurationDescription = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_firehose.types.subnet_id_list

        out["subnet_ids"] = capo_firehose.types.subnet_id_list.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    else:
        raise DeserializationError("VpcConfigurationDescription.subnet_ids required")
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("VpcConfigurationDescription.role_arn required")
    if data.get("SecurityGroupIds") is not None:
        import capo_firehose.types.security_group_id_list

        out["security_group_ids"] = (
            capo_firehose.types.security_group_id_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "VpcConfigurationDescription.security_group_ids required"
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError("VpcConfigurationDescription.vpc_id required")
    return out
