"""Generated from Smithy shape ``com.amazonaws.transfer#EndpointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.address_allocation_ids
    import capo_transfer.types.security_group_ids
    import capo_transfer.types.subnet_ids
    import capo_transfer.types.vpc_endpoint_id
    import capo_transfer.types.vpc_id


class EndpointDetails(TypedDict, closed=True):
    address_allocation_ids: NotRequired[
        "capo_transfer.types.address_allocation_ids.AddressAllocationIds"
    ]
    """<p>A list of address allocation IDs that are required to attach an Elastic IP address to your server's endpoint.</p> <p>An address allocation ID corresponds to the allocation ID of an Elastic IP address. This value can be retrieved from the <code>allocationId</code> field from the Amazon EC2 <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Address.html">Address</a> data type. One way to retrieve this value is by calling the EC2 <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html">DescribeAddresses</a> API.</p> <p>This parameter is optional. Set this parameter if you want to make your VPC endpoint public-facing. For details, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#create-internet-facing-endpoint">Create an internet-facing endpoint for your server</a>.</p> <note> <p>This property can only be set as follows:</p> <ul> <li> <p> <code>EndpointType</code> must be set to <code>VPC</code> </p> </li> <li> <p>The Transfer Family server must be offline.</p> </li> <li> <p>You cannot set this parameter for Transfer Family servers that use the FTP protocol.</p> </li> <li> <p>The server must already have <code>SubnetIds</code> populated (<code>SubnetIds</code> and <code>AddressAllocationIds</code> cannot be updated simultaneously).</p> </li> <li> <p> <code>AddressAllocationIds</code> can't contain duplicates, and must be equal in length to <code>SubnetIds</code>. For example, if you have three subnet IDs, you must also specify three address allocation IDs.</p> </li> <li> <p>Call the <code>UpdateServer</code> API to set or change this parameter.</p> </li> <li> <p>You can't set address allocation IDs for servers that have an <code>IpAddressType</code> set to <code>DUALSTACK</code> You can only set this property if <code>IpAddressType</code> is set to <code>IPV4</code>.</p> </li> </ul> </note>"""
    subnet_ids: NotRequired["capo_transfer.types.subnet_ids.SubnetIds"]
    """<p>A list of subnet IDs that are required to host your server endpoint in your VPC.</p> <note> <p>This property can only be set when <code>EndpointType</code> is set to <code>VPC</code>.</p> </note>"""
    vpc_endpoint_id: NotRequired["capo_transfer.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The identifier of the VPC endpoint.</p> <note> <p>This property can only be set when <code>EndpointType</code> is set to <code>VPC_ENDPOINT</code>.</p> <p>For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.</p> </note>"""
    vpc_id: NotRequired["capo_transfer.types.vpc_id.VpcId"]
    """<p>The VPC identifier of the VPC in which a server's endpoint will be hosted.</p> <note> <p>This property can only be set when <code>EndpointType</code> is set to <code>VPC</code>.</p> </note>"""
    security_group_ids: NotRequired[
        "capo_transfer.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of security groups IDs that are available to attach to your server's endpoint.</p> <note> <p>While <code>SecurityGroupIds</code> appears in the response syntax for consistency with <code>CreateServer</code> and <code>UpdateServer</code> operations, this field is not populated in <code>DescribeServer</code> responses. Security groups are managed at the VPC endpoint level and can be modified outside of the Transfer Family service. To retrieve current security group information, use the EC2 <code>DescribeVpcEndpoints</code> API with the <code>VpcEndpointId</code> returned in the response.</p> <p>This property can only be set when <code>EndpointType</code> is set to <code>VPC</code>.</p> <p>You can edit the <code>SecurityGroupIds</code> property in the <a href="https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateServer.html">UpdateServer</a> API only if you are changing the <code>EndpointType</code> from <code>PUBLIC</code> or <code>VPC_ENDPOINT</code> to <code>VPC</code>. To change security groups associated with your server's VPC endpoint after creation, use the Amazon EC2 <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html">ModifyVpcEndpoint</a> API.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointDetails) -> dict:
    out: dict = {}
    if "address_allocation_ids" in value:
        import capo_transfer.types.address_allocation_ids

        out["AddressAllocationIds"] = (
            capo_transfer.types.address_allocation_ids.serialize_aws_json_1_1(
                value["address_allocation_ids"]
            )
        )
    if "subnet_ids" in value:
        import capo_transfer.types.subnet_ids

        out["SubnetIds"] = capo_transfer.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "security_group_ids" in value:
        import capo_transfer.types.security_group_ids

        out["SecurityGroupIds"] = (
            capo_transfer.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointDetails:
    out: EndpointDetails = {}  # type: ignore[typeddict-item]
    if data.get("AddressAllocationIds") is not None:
        import capo_transfer.types.address_allocation_ids

        out["address_allocation_ids"] = (
            capo_transfer.types.address_allocation_ids.deserialize_aws_json_1_1(
                data["AddressAllocationIds"]
            )
        )
    if data.get("SubnetIds") is not None:
        import capo_transfer.types.subnet_ids

        out["subnet_ids"] = capo_transfer.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SecurityGroupIds") is not None:
        import capo_transfer.types.security_group_ids

        out["security_group_ids"] = (
            capo_transfer.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    return out
