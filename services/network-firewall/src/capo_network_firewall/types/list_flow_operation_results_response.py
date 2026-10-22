"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListFlowOperationResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.availability_zone
    import capo_network_firewall.types.availability_zone_id
    import capo_network_firewall.types.flow_operation_id
    import capo_network_firewall.types.flow_operation_status
    import capo_network_firewall.types.flow_request_timestamp
    import capo_network_firewall.types.flows
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.status_reason
    import capo_network_firewall.types.vpc_endpoint_id


class ListFlowOperationResultsResponse(TypedDict, closed=True):
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
    """<p></p>"""
    vpc_endpoint_id: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p></p>"""
    flow_operation_id: NotRequired[
        "capo_network_firewall.types.flow_operation_id.FlowOperationId"
    ]
    """<p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>"""
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
    flows: NotRequired["capo_network_firewall.types.flows.Flows"]
    """<p>Any number of arrays, where each array is a single flow identified in the scope of the operation. If multiple flows were in the scope of the operation, multiple <code>Flows</code> arrays are returned.</p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFlowOperationResultsResponse) -> dict:
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
    if "flows" in value:
        import capo_network_firewall.types.flows

        out["Flows"] = capo_network_firewall.types.flows.serialize_aws_json_1_0(
            value["flows"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFlowOperationResultsResponse:
    out: ListFlowOperationResultsResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("Flows") is not None:
        import capo_network_firewall.types.flows

        out["flows"] = capo_network_firewall.types.flows.deserialize_aws_json_1_0(
            data["Flows"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
