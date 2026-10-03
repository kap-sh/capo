"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.client_affinity
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.port_ranges
    import capo_global_accelerator.types.protocol


class UpdateListenerRequest(TypedDict, closed=True):
    listener_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener to update.</p>"""
    port_ranges: NotRequired["capo_global_accelerator.types.port_ranges.PortRanges"]
    """<p>The updated list of port ranges for the connections from clients to the accelerator.</p>"""
    protocol: NotRequired["capo_global_accelerator.types.protocol.Protocol"]
    """<p>The updated protocol for the connections from clients to the accelerator.</p>"""
    client_affinity: NotRequired[
        "capo_global_accelerator.types.client_affinity.ClientAffinity"
    ]
    """<p>Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Client affinity gives you control over whether to always route each client to the same specific endpoint.</p> <p>Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is <code>NONE</code>, Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes. </p> <p>If you want a given client to always be routed to the same endpoint, set client affinity to <code>SOURCE_IP</code> instead. When you use the <code>SOURCE_IP</code> setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.</p> <p>The default value is <code>NONE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateListenerRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    if "port_ranges" in value:
        import capo_global_accelerator.types.port_ranges

        out["PortRanges"] = (
            capo_global_accelerator.types.port_ranges.serialize_aws_json_1_1(
                value["port_ranges"]
            )
        )
    if "protocol" in value:
        import capo_global_accelerator.types.protocol

        out["Protocol"] = capo_global_accelerator.types.protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "client_affinity" in value:
        import capo_global_accelerator.types.client_affinity

        out["ClientAffinity"] = (
            capo_global_accelerator.types.client_affinity.serialize_aws_json_1_1(
                value["client_affinity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateListenerRequest:
    out: UpdateListenerRequest = {}  # type: ignore[typeddict-item]
    if data.get("ListenerArn") is not None:
        out["listener_arn"] = data["ListenerArn"]
    else:
        raise DeserializationError("UpdateListenerRequest.listener_arn required")
    if data.get("PortRanges") is not None:
        import capo_global_accelerator.types.port_ranges

        out["port_ranges"] = (
            capo_global_accelerator.types.port_ranges.deserialize_aws_json_1_1(
                data["PortRanges"]
            )
        )
    if data.get("Protocol") is not None:
        import capo_global_accelerator.types.protocol

        out["protocol"] = (
            capo_global_accelerator.types.protocol.deserialize_aws_json_1_1(
                data["Protocol"]
            )
        )
    if data.get("ClientAffinity") is not None:
        import capo_global_accelerator.types.client_affinity

        out["client_affinity"] = (
            capo_global_accelerator.types.client_affinity.deserialize_aws_json_1_1(
                data["ClientAffinity"]
            )
        )
    return out
