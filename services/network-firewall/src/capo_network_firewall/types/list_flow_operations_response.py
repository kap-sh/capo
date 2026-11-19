"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListFlowOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.flow_operations
    import capo_network_firewall.types.pagination_token


class ListFlowOperationsResponse(TypedDict, closed=True):
    flow_operations: NotRequired[
        "capo_network_firewall.types.flow_operations.FlowOperations"
    ]
    """<p>Flow operations let you manage the flows tracked in the flow table, also known as the firewall table.</p> <p>A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort. </p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFlowOperationsResponse) -> dict:
    out: dict = {}
    if "flow_operations" in value:
        import capo_network_firewall.types.flow_operations

        out["FlowOperations"] = (
            capo_network_firewall.types.flow_operations.serialize_aws_json_1_0(
                value["flow_operations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFlowOperationsResponse:
    out: ListFlowOperationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlowOperations") is not None:
        import capo_network_firewall.types.flow_operations

        out["flow_operations"] = (
            capo_network_firewall.types.flow_operations.deserialize_aws_json_1_0(
                data["FlowOperations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListFlowOperationsResponse) -> dict:
    out: dict = {}
    if "flow_operations" in value:
        import capo_network_firewall.types.flow_operations

        out["FlowOperations"] = (
            capo_network_firewall.types.flow_operations.serialize_cbor(
                value["flow_operations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListFlowOperationsResponse:
    out: ListFlowOperationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlowOperations") is not None:
        import capo_network_firewall.types.flow_operations

        out["flow_operations"] = (
            capo_network_firewall.types.flow_operations.deserialize_cbor(
                data["FlowOperations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
