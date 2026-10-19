"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateRouterNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.router_network_interface_configuration


class CreateRouterNetworkInterfaceRequest(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router network interface.</p>"""
    configuration: "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
    """<p>The configuration settings for the router network interface.</p>"""
    region_name: NotRequired["str"]
    """<p>The Amazon Web Services Region for the router network interface. Defaults to the current region if not specified.</p>"""
    tags: NotRequired["capo_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p>Key-value pairs that can be used to tag and organize this router network interface.</p>"""
    client_token: NotRequired["capo_mediaconnect.types.client_token.ClientToken"]
    """<p>A unique identifier for the request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouterNetworkInterfaceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_network_interface_configuration

    out["configuration"] = (
        capo_mediaconnect.types.router_network_interface_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "region_name" in value:
        out["regionName"] = value["region_name"]
    if "tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRouterNetworkInterfaceRequest:
    out: CreateRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.router_network_interface_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_network_interface_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["configuration"] = capo_mediaconnect.types._unknown.UnknownUnionMember("")
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    if data.get("tags") is not None:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
