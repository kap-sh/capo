"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StartFlowFlushResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.flow_operation_id
    import capo_network_firewall.types.flow_operation_status
    import capo_network_firewall.types.resource_arn


class StartFlowFlushResponse(TypedDict, closed=True):
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    flow_operation_id: NotRequired[
        "capo_network_firewall.types.flow_operation_id.FlowOperationId"
    ]
    """<p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>"""
    flow_operation_status: NotRequired[
        "capo_network_firewall.types.flow_operation_status.FlowOperationStatus"
    ]
    """<p>Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.</p> <p>If the status is <code>COMPLETED_WITH_ERRORS</code>, results may be returned with any number of <code>Flows</code> missing from the response. If the status is <code>FAILED</code>, <code>Flows</code> returned will be empty.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFlowFlushResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "flow_operation_id" in value:
        out["FlowOperationId"] = value["flow_operation_id"]
    if "flow_operation_status" in value:
        import capo_network_firewall.types.flow_operation_status

        out["FlowOperationStatus"] = (
            capo_network_firewall.types.flow_operation_status.serialize_aws_json_1_0(
                value["flow_operation_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFlowFlushResponse:
    out: StartFlowFlushResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FlowOperationId") is not None:
        out["flow_operation_id"] = data["FlowOperationId"]
    if data.get("FlowOperationStatus") is not None:
        import capo_network_firewall.types.flow_operation_status

        out["flow_operation_status"] = (
            capo_network_firewall.types.flow_operation_status.deserialize_aws_json_1_0(
                data["FlowOperationStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartFlowFlushResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "flow_operation_id" in value:
        out["FlowOperationId"] = value["flow_operation_id"]
    if "flow_operation_status" in value:
        import capo_network_firewall.types.flow_operation_status

        out["FlowOperationStatus"] = (
            capo_network_firewall.types.flow_operation_status.serialize_cbor(
                value["flow_operation_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StartFlowFlushResponse:
    out: StartFlowFlushResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FlowOperationId") is not None:
        out["flow_operation_id"] = data["FlowOperationId"]
    if data.get("FlowOperationStatus") is not None:
        import capo_network_firewall.types.flow_operation_status

        out["flow_operation_status"] = (
            capo_network_firewall.types.flow_operation_status.deserialize_cbor(
                data["FlowOperationStatus"]
            )
        )
    return out
