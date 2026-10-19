"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_protocols
    import capo_global_accelerator.types.port_number


class CustomRoutingDestinationConfiguration(TypedDict, closed=True):
    from_port: "capo_global_accelerator.types.port_number.PortNumber"
    """<p>The first port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.</p>"""
    to_port: "capo_global_accelerator.types.port_number.PortNumber"
    """<p>The last port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.</p>"""
    protocols: (
        "capo_global_accelerator.types.custom_routing_protocols.CustomRoutingProtocols"
    )
    """<p>The protocol for the endpoint group that is associated with a custom routing accelerator. The protocol can be either TCP or UDP.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingDestinationConfiguration) -> dict:
    out: dict = {}
    out["FromPort"] = value["from_port"]
    out["ToPort"] = value["to_port"]
    import capo_global_accelerator.types.custom_routing_protocols

    out["Protocols"] = (
        capo_global_accelerator.types.custom_routing_protocols.serialize_aws_json_1_1(
            value["protocols"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomRoutingDestinationConfiguration:
    out: CustomRoutingDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FromPort") is not None:
        out["from_port"] = data["FromPort"]
    else:
        out["from_port"] = 0
    if data.get("ToPort") is not None:
        out["to_port"] = data["ToPort"]
    else:
        out["to_port"] = 0
    if data.get("Protocols") is not None:
        import capo_global_accelerator.types.custom_routing_protocols

        out["protocols"] = (
            capo_global_accelerator.types.custom_routing_protocols.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    else:
        out["protocols"] = []
    return out
