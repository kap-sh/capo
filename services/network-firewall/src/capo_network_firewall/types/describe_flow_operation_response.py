"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFlowOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.availability_zone
    import capo_network_firewall.types.availability_zone_id
    import capo_network_firewall.types.flow_operation
    import capo_network_firewall.types.flow_operation_id
    import capo_network_firewall.types.flow_operation_status
    import capo_network_firewall.types.flow_operation_type
    import capo_network_firewall.types.flow_request_timestamp
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.status_reason
    import capo_network_firewall.types.vpc_endpoint_id


class DescribeFlowOperationResponse(TypedDict, closed=True):
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    availability_zone: NotRequired[
        "capo_network_firewall.types.availability_zone.AvailabilityZone"
    ]
    """<p>The name of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>"""
    availability_zone_id: NotRequired[
        "capo_network_firewall.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone where the firewall is located. For example, <code>use2-az1</code>.</p>"""
    vpc_endpoint_association_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>A unique identifier for the primary endpoint associated with a firewall.</p>"""
    flow_operation_id: NotRequired[
        "capo_network_firewall.types.flow_operation_id.FlowOperationId"
    ]
    """<p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>"""
    flow_operation_type: NotRequired[
        "capo_network_firewall.types.flow_operation_type.FlowOperationType"
    ]
    """<p>Defines the type of <code>FlowOperation</code>.</p>"""
    flow_operation_status: NotRequired[
        "capo_network_firewall.types.flow_operation_status.FlowOperationStatus"
    ]
    """<p>Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.</p> <p>If the status is <code>COMPLETED_WITH_ERRORS</code>, results may be returned with any number of <code>Flows</code> missing from the response. If the status is <code>FAILED</code>, <code>Flows</code> returned will be empty.</p>"""
    status_message: NotRequired[
        "capo_network_firewall.types.status_reason.StatusReason"
    ]
    """<p>If the asynchronous operation fails, Network Firewall populates this with the reason for the error or failure. Options include <code>Flow operation error</code> and <code>Flow timeout</code>.</p>"""
    flow_request_timestamp: NotRequired[
        "capo_network_firewall.types.flow_request_timestamp.FlowRequestTimestamp"
    ]
    """<p>A timestamp indicating when the Suricata engine identified flows impacted by an operation. </p>"""
    flow_operation: NotRequired[
        "capo_network_firewall.types.flow_operation.FlowOperation"
    ]
    """<p>Returns key information about a flow operation, such as related statuses, unique identifiers, and all filters defined in the operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFlowOperationResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "flow_operation_id" in value:
        out["FlowOperationId"] = value["flow_operation_id"]
    if "flow_operation_type" in value:
        import capo_network_firewall.types.flow_operation_type

        out["FlowOperationType"] = (
            capo_network_firewall.types.flow_operation_type.serialize_aws_json_1_0(
                value["flow_operation_type"]
            )
        )
    if "flow_operation_status" in value:
        import capo_network_firewall.types.flow_operation_status

        out["FlowOperationStatus"] = (
            capo_network_firewall.types.flow_operation_status.serialize_aws_json_1_0(
                value["flow_operation_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "flow_request_timestamp" in value:
        import capo_network_firewall.types.flow_request_timestamp

        out["FlowRequestTimestamp"] = (
            capo_network_firewall.types.flow_request_timestamp.serialize_aws_json_1_0(
                value["flow_request_timestamp"]
            )
        )
    if "flow_operation" in value:
        import capo_network_firewall.types.flow_operation

        out["FlowOperation"] = (
            capo_network_firewall.types.flow_operation.serialize_aws_json_1_0(
                value["flow_operation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFlowOperationResponse:
    out: DescribeFlowOperationResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
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
    if data.get("FlowOperationType") is not None:
        import capo_network_firewall.types.flow_operation_type

        out["flow_operation_type"] = (
            capo_network_firewall.types.flow_operation_type.deserialize_aws_json_1_0(
                data["FlowOperationType"]
            )
        )
    if data.get("FlowOperationStatus") is not None:
        import capo_network_firewall.types.flow_operation_status

        out["flow_operation_status"] = (
            capo_network_firewall.types.flow_operation_status.deserialize_aws_json_1_0(
                data["FlowOperationStatus"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("FlowRequestTimestamp") is not None:
        import capo_network_firewall.types.flow_request_timestamp

        out["flow_request_timestamp"] = (
            capo_network_firewall.types.flow_request_timestamp.deserialize_aws_json_1_0(
                data["FlowRequestTimestamp"]
            )
        )
    if data.get("FlowOperation") is not None:
        import capo_network_firewall.types.flow_operation

        out["flow_operation"] = (
            capo_network_firewall.types.flow_operation.deserialize_aws_json_1_0(
                data["FlowOperation"]
            )
        )
    return out
