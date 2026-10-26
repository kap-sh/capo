"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.router_network_interface_arn
    import capo_mediaconnect.types.router_network_interface_configuration
    import capo_mediaconnect.types.router_network_interface_state
    import capo_mediaconnect.types.router_network_interface_type


class RouterNetworkInterface(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router network interface.</p>"""
    arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the router network interface.</p>"""
    id: "str"
    """<p>The unique identifier of the router network interface.</p>"""
    state: "capo_mediaconnect.types.router_network_interface_state.RouterNetworkInterfaceState"
    """<p>The current state of the router network interface.</p>"""
    network_interface_type: "capo_mediaconnect.types.router_network_interface_type.RouterNetworkInterfaceType"
    """<p>The type of the router network interface.</p>"""
    configuration: "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
    associated_output_count: "int"
    """<p>The number of router outputs associated with the network interface.</p>"""
    associated_input_count: "int"
    """<p>The number of router inputs associated with the network interface.</p>"""
    region_name: "str"
    """<p>The Amazon Web Services Region where the router network interface is located.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the router network interface was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router network interface was last updated.</p>"""
    tags: "capo_mediaconnect.types.__map_of_string.__mapOfString"
    """<p>Key-value pairs that can be used to tag and organize this router network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterface) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_mediaconnect.types.router_network_interface_state

    out["state"] = (
        capo_mediaconnect.types.router_network_interface_state.serialize_json(
            value["state"]
        )
    )
    import capo_mediaconnect.types.router_network_interface_type

    out["networkInterfaceType"] = (
        capo_mediaconnect.types.router_network_interface_type.serialize_json(
            value["network_interface_type"]
        )
    )
    import capo_mediaconnect.types.router_network_interface_configuration

    out["configuration"] = (
        capo_mediaconnect.types.router_network_interface_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["associatedOutputCount"] = value["associated_output_count"]
    out["associatedInputCount"] = value["associated_input_count"]
    out["regionName"] = value["region_name"]
    import capo_mediaconnect._protocol.serialize

    out["createdAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_mediaconnect._protocol.serialize

    out["updatedAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    import capo_mediaconnect.types.__map_of_string

    out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RouterNetworkInterface:
    out: RouterNetworkInterface = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("state") is not None:
        import capo_mediaconnect.types.router_network_interface_state

        out["state"] = (
            capo_mediaconnect.types.router_network_interface_state.deserialize_json(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_mediaconnect.types.router_network_interface_state.RouterNetworkInterfaceState",
            "",
        )
    if data.get("networkInterfaceType") is not None:
        import capo_mediaconnect.types.router_network_interface_type

        out["network_interface_type"] = (
            capo_mediaconnect.types.router_network_interface_type.deserialize_json(
                data["networkInterfaceType"]
            )
        )
    else:
        import typing

        out["network_interface_type"] = typing.cast(
            "capo_mediaconnect.types.router_network_interface_type.RouterNetworkInterfaceType",
            "",
        )
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.router_network_interface_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_network_interface_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        out["configuration"] = {"$unknown": {"name": ""}}
    if data.get("associatedOutputCount") is not None:
        out["associated_output_count"] = data["associatedOutputCount"]
    else:
        out["associated_output_count"] = 0
    if data.get("associatedInputCount") is not None:
        out["associated_input_count"] = data["associatedInputCount"]
    else:
        out["associated_input_count"] = 0
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    else:
        out["region_name"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("tags") is not None:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
