"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateCoreNetworkEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.update_ip_address_list


class UpdateCoreNetworkEndpointInput(TypedDict, closed=True):
    core_network_endpoint_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the core network endpoint to update.</p>"""
    name: NotRequired["capo_route53globalresolver.types.resource_name.ResourceName"]
    """<p>The name of the core network endpoint.</p>"""
    update_ip_addresses: NotRequired[
        "capo_route53globalresolver.types.update_ip_address_list.UpdateIpAddressList"
    ]
    """<p>The IP address changes to apply to the core network endpoint. Use this parameter to add or remove the IP addresses that the endpoint uses to resolve DNS queries within the Amazon Web Services Cloud WAN core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCoreNetworkEndpointInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "update_ip_addresses" in value:
        import capo_route53globalresolver.types.update_ip_address_list

        out["updateIpAddresses"] = (
            capo_route53globalresolver.types.update_ip_address_list.serialize_json(
                value["update_ip_addresses"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCoreNetworkEndpointInput:
    out: UpdateCoreNetworkEndpointInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("updateIpAddresses") is not None:
        import capo_route53globalresolver.types.update_ip_address_list

        out["update_ip_addresses"] = (
            capo_route53globalresolver.types.update_ip_address_list.deserialize_json(
                data["updateIpAddresses"]
            )
        )
    return out
