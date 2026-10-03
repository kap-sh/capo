"""Generated from Smithy shape ``com.amazonaws.datasync#PrivateLinkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.endpoint
    import capo_datasync.types.pl_security_group_arn_list
    import capo_datasync.types.pl_subnet_arn_list
    import capo_datasync.types.vpc_endpoint_id


class PrivateLinkConfig(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired["capo_datasync.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>Specifies the ID of the VPC endpoint that your agent connects to.</p>"""
    private_link_endpoint: NotRequired["capo_datasync.types.endpoint.Endpoint"]
    """<p>Specifies the VPC endpoint provided by <a href="https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html">Amazon Web Services PrivateLink</a> that your agent connects to.</p>"""
    subnet_arns: NotRequired["capo_datasync.types.pl_subnet_arn_list.PLSubnetArnList"]
    """<p>Specifies the ARN of the subnet where your VPC endpoint is located. You can only specify one ARN.</p>"""
    security_group_arns: NotRequired[
        "capo_datasync.types.pl_security_group_arn_list.PLSecurityGroupArnList"
    ]
    """<p>Specifies the Amazon Resource Names (ARN) of the security group that provides DataSync access to your VPC endpoint. You can only specify one ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateLinkConfig) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "private_link_endpoint" in value:
        out["PrivateLinkEndpoint"] = value["private_link_endpoint"]
    if "subnet_arns" in value:
        import capo_datasync.types.pl_subnet_arn_list

        out["SubnetArns"] = (
            capo_datasync.types.pl_subnet_arn_list.serialize_aws_json_1_1(
                value["subnet_arns"]
            )
        )
    if "security_group_arns" in value:
        import capo_datasync.types.pl_security_group_arn_list

        out["SecurityGroupArns"] = (
            capo_datasync.types.pl_security_group_arn_list.serialize_aws_json_1_1(
                value["security_group_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateLinkConfig:
    out: PrivateLinkConfig = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if data.get("PrivateLinkEndpoint") is not None:
        out["private_link_endpoint"] = data["PrivateLinkEndpoint"]
    if data.get("SubnetArns") is not None:
        import capo_datasync.types.pl_subnet_arn_list

        out["subnet_arns"] = (
            capo_datasync.types.pl_subnet_arn_list.deserialize_aws_json_1_1(
                data["SubnetArns"]
            )
        )
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.pl_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.pl_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    return out
