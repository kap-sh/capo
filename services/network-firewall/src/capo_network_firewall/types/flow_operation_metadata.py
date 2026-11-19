"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowOperationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.flow_operation_id
    import capo_network_firewall.types.flow_operation_status
    import capo_network_firewall.types.flow_operation_type
    import capo_network_firewall.types.flow_request_timestamp


class FlowOperationMetadata(TypedDict, closed=True):
    flow_operation_id: NotRequired[
        "capo_network_firewall.types.flow_operation_id.FlowOperationId"
    ]
    """<p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>"""
    flow_operation_type: NotRequired[
        "capo_network_firewall.types.flow_operation_type.FlowOperationType"
    ]
    """<p>Defines the type of <code>FlowOperation</code>.</p>"""
    flow_request_timestamp: NotRequired[
        "capo_network_firewall.types.flow_request_timestamp.FlowRequestTimestamp"
    ]
    """<p>A timestamp indicating when the Suricata engine identified flows impacted by an operation. </p>"""
    flow_operation_status: NotRequired[
        "capo_network_firewall.types.flow_operation_status.FlowOperationStatus"
    ]
    """<p>Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.</p> <p>If the status is <code>COMPLETED_WITH_ERRORS</code>, results may be returned with any number of <code>Flows</code> missing from the response. If the status is <code>FAILED</code>, <code>Flows</code> returned will be empty.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowOperationMetadata) -> dict:
    out: dict = {}
    if "flow_operation_id" in value:
        out["FlowOperationId"] = value["flow_operation_id"]
    if "flow_operation_type" in value:
        import capo_network_firewall.types.flow_operation_type

        out["FlowOperationType"] = (
            capo_network_firewall.types.flow_operation_type.serialize_aws_json_1_0(
                value["flow_operation_type"]
            )
        )
    if "flow_request_timestamp" in value:
        import capo_network_firewall.types.flow_request_timestamp

        out["FlowRequestTimestamp"] = (
            capo_network_firewall.types.flow_request_timestamp.serialize_aws_json_1_0(
                value["flow_request_timestamp"]
            )
        )
    if "flow_operation_status" in value:
        import capo_network_firewall.types.flow_operation_status

        out["FlowOperationStatus"] = (
            capo_network_firewall.types.flow_operation_status.serialize_aws_json_1_0(
                value["flow_operation_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FlowOperationMetadata:
    out: FlowOperationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("FlowOperationId") is not None:
        out["flow_operation_id"] = data["FlowOperationId"]
    if data.get("FlowOperationType") is not None:
        import capo_network_firewall.types.flow_operation_type

        out["flow_operation_type"] = (
            capo_network_firewall.types.flow_operation_type.deserialize_aws_json_1_0(
                data["FlowOperationType"]
            )
        )
    if data.get("FlowRequestTimestamp") is not None:
        import capo_network_firewall.types.flow_request_timestamp

        out["flow_request_timestamp"] = (
            capo_network_firewall.types.flow_request_timestamp.deserialize_aws_json_1_0(
                data["FlowRequestTimestamp"]
            )
        )
    if data.get("FlowOperationStatus") is not None:
        import capo_network_firewall.types.flow_operation_status

        out["flow_operation_status"] = (
            capo_network_firewall.types.flow_operation_status.deserialize_aws_json_1_0(
                data["FlowOperationStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlowOperationMetadata) -> dict:
    out: dict = {}
    if "flow_operation_id" in value:
        out["FlowOperationId"] = value["flow_operation_id"]
    if "flow_operation_type" in value:
        import capo_network_firewall.types.flow_operation_type

        out["FlowOperationType"] = (
            capo_network_firewall.types.flow_operation_type.serialize_cbor(
                value["flow_operation_type"]
            )
        )
    if "flow_request_timestamp" in value:
        import capo_network_firewall.types.flow_request_timestamp

        out["FlowRequestTimestamp"] = (
            capo_network_firewall.types.flow_request_timestamp.serialize_cbor(
                value["flow_request_timestamp"]
            )
        )
    if "flow_operation_status" in value:
        import capo_network_firewall.types.flow_operation_status

        out["FlowOperationStatus"] = (
            capo_network_firewall.types.flow_operation_status.serialize_cbor(
                value["flow_operation_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> FlowOperationMetadata:
    out: FlowOperationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("FlowOperationId") is not None:
        out["flow_operation_id"] = data["FlowOperationId"]
    if data.get("FlowOperationType") is not None:
        import capo_network_firewall.types.flow_operation_type

        out["flow_operation_type"] = (
            capo_network_firewall.types.flow_operation_type.deserialize_cbor(
                data["FlowOperationType"]
            )
        )
    if data.get("FlowRequestTimestamp") is not None:
        import capo_network_firewall.types.flow_request_timestamp

        out["flow_request_timestamp"] = (
            capo_network_firewall.types.flow_request_timestamp.deserialize_cbor(
                data["FlowRequestTimestamp"]
            )
        )
    if data.get("FlowOperationStatus") is not None:
        import capo_network_firewall.types.flow_operation_status

        out["flow_operation_status"] = (
            capo_network_firewall.types.flow_operation_status.deserialize_cbor(
                data["FlowOperationStatus"]
            )
        )
    return out
