"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateCustomRoutingEndpointGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_destination_configurations
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.idempotency_token


class CreateCustomRoutingEndpointGroupRequest(TypedDict, closed=True):
    listener_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener for a custom routing endpoint.</p>"""
    endpoint_group_region: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Web Services Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.</p>"""
    destination_configurations: "capo_global_accelerator.types.custom_routing_destination_configurations.CustomRoutingDestinationConfigurations"
    """<p>Sets the port range and protocol for all endpoints (virtual private cloud subnets) in a custom routing endpoint group to accept client traffic on.</p>"""
    idempotency_token: (
        "capo_global_accelerator.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomRoutingEndpointGroupRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    out["EndpointGroupRegion"] = value["endpoint_group_region"]
    import capo_global_accelerator.types.custom_routing_destination_configurations

    out["DestinationConfigurations"] = (
        capo_global_accelerator.types.custom_routing_destination_configurations.serialize_aws_json_1_1(
            value["destination_configurations"]
        )
    )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomRoutingEndpointGroupRequest:
    out: CreateCustomRoutingEndpointGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ListenerArn") is not None:
        out["listener_arn"] = data["ListenerArn"]
    else:
        out["listener_arn"] = ""
    if data.get("EndpointGroupRegion") is not None:
        out["endpoint_group_region"] = data["EndpointGroupRegion"]
    else:
        out["endpoint_group_region"] = ""
    if data.get("DestinationConfigurations") is not None:
        import capo_global_accelerator.types.custom_routing_destination_configurations

        out["destination_configurations"] = (
            capo_global_accelerator.types.custom_routing_destination_configurations.deserialize_aws_json_1_1(
                data["DestinationConfigurations"]
            )
        )
    else:
        out["destination_configurations"] = []
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    return out
