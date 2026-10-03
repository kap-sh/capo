"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.client_affinity
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.idempotency_token
    import capo_global_accelerator.types.port_ranges
    import capo_global_accelerator.types.protocol


class CreateListenerRequest(TypedDict, closed=True):
    accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of your accelerator.</p>"""
    port_ranges: "capo_global_accelerator.types.port_ranges.PortRanges"
    """<p>The list of port ranges to support for connections from clients to your accelerator.</p>"""
    protocol: "capo_global_accelerator.types.protocol.Protocol"
    """<p>The protocol for connections from clients to your accelerator.</p>"""
    client_affinity: NotRequired[
        "capo_global_accelerator.types.client_affinity.ClientAffinity"
    ]
    """<p>Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Client affinity gives you control over whether to always route each client to the same specific endpoint.</p> <p>Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is <code>NONE</code>, Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes. </p> <p>If you want a given client to always be routed to the same endpoint, set client affinity to <code>SOURCE_IP</code> instead. When you use the <code>SOURCE_IP</code> setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.</p> <p>The default value is <code>NONE</code>.</p>"""
    idempotency_token: (
        "capo_global_accelerator.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateListenerRequest) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    import capo_global_accelerator.types.port_ranges

    out["PortRanges"] = (
        capo_global_accelerator.types.port_ranges.serialize_aws_json_1_1(
            value["port_ranges"]
        )
    )
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
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateListenerRequest:
    out: CreateListenerRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorArn") is not None:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        raise DeserializationError("CreateListenerRequest.accelerator_arn required")
    if data.get("PortRanges") is not None:
        import capo_global_accelerator.types.port_ranges

        out["port_ranges"] = (
            capo_global_accelerator.types.port_ranges.deserialize_aws_json_1_1(
                data["PortRanges"]
            )
        )
    else:
        raise DeserializationError("CreateListenerRequest.port_ranges required")
    if data.get("Protocol") is not None:
        import capo_global_accelerator.types.protocol

        out["protocol"] = (
            capo_global_accelerator.types.protocol.deserialize_aws_json_1_1(
                data["Protocol"]
            )
        )
    else:
        raise DeserializationError("CreateListenerRequest.protocol required")
    if data.get("ClientAffinity") is not None:
        import capo_global_accelerator.types.client_affinity

        out["client_affinity"] = (
            capo_global_accelerator.types.client_affinity.deserialize_aws_json_1_1(
                data["ClientAffinity"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError("CreateListenerRequest.idempotency_token required")
    return out
