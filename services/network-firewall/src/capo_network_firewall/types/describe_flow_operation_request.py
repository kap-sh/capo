"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFlowOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.availability_zone
    import capo_network_firewall.types.availability_zone_id
    import capo_network_firewall.types.flow_operation_id
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.vpc_endpoint_id


class DescribeFlowOperationRequest(TypedDict, closed=True):
    firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    availability_zone: NotRequired[
        "capo_network_firewall.types.availability_zone.AvailabilityZone"
    ]
    """<p>The name of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>"""
    availability_zone_id: NotRequired[
        "capo_network_firewall.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone where the firewall is located. For example, <code>use2-az1</code>. Availability Zone IDs are the same in every Amazon Web Services account, so use this parameter when you coordinate resources across accounts. Specify either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code>, not both. If you specify both, the request fails.</p>"""
    vpc_endpoint_association_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>A unique identifier for the primary endpoint associated with a firewall.</p>"""
    flow_operation_id: "capo_network_firewall.types.flow_operation_id.FlowOperationId"
    """<p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFlowOperationRequest) -> dict:
    out: dict = {}
    out["FirewallArn"] = value["firewall_arn"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    out["FlowOperationId"] = value["flow_operation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFlowOperationRequest:
    out: DescribeFlowOperationRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        out["firewall_arn"] = ""
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("AvailabilityZoneId") is not None:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if data.get("VpcEndpointAssociationArn") is not None:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if data.get("FlowOperationId") is not None:
        out["flow_operation_id"] = data["FlowOperationId"]
    else:
        out["flow_operation_id"] = ""
    return out
