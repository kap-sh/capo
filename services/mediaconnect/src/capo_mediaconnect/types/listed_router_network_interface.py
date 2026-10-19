"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterNetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.router_network_interface_arn
    import capo_mediaconnect.types.router_network_interface_state
    import capo_mediaconnect.types.router_network_interface_type


class ListedRouterNetworkInterface(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router network interface.</p>"""
    arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the router network interface.</p>"""
    id: "str"
    """<p>The unique identifier of the router network interface.</p>"""
    network_interface_type: "capo_mediaconnect.types.router_network_interface_type.RouterNetworkInterfaceType"
    """<p>The type of the router network interface.</p>"""
    associated_output_count: "int"
    """<p>The number of router outputs associated with the network interface.</p>"""
    associated_input_count: "int"
    """<p>The number of router inputs associated with the network interface.</p>"""
    state: "capo_mediaconnect.types.router_network_interface_state.RouterNetworkInterfaceState"
    """<p>The current state of the router network interface.</p>"""
    region_name: "str"
    """<p>The Amazon Web Services Region where the router network interface is located.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the network interface was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router network interface was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterNetworkInterface) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_mediaconnect.types.router_network_interface_type

    out["networkInterfaceType"] = (
        capo_mediaconnect.types.router_network_interface_type.serialize_json(
            value["network_interface_type"]
        )
    )
    out["associatedOutputCount"] = value["associated_output_count"]
    out["associatedInputCount"] = value["associated_input_count"]
    import capo_mediaconnect.types.router_network_interface_state

    out["state"] = (
        capo_mediaconnect.types.router_network_interface_state.serialize_json(
            value["state"]
        )
    )
    out["regionName"] = value["region_name"]
    import capo_mediaconnect._protocol.serialize

    out["createdAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_mediaconnect._protocol.serialize

    out["updatedAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ListedRouterNetworkInterface:
    out: ListedRouterNetworkInterface = {}  # type: ignore[typeddict-item]
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
    if data.get("associatedOutputCount") is not None:
        out["associated_output_count"] = data["associatedOutputCount"]
    else:
        out["associated_output_count"] = 0
    if data.get("associatedInputCount") is not None:
        out["associated_input_count"] = data["associatedInputCount"]
    else:
        out["associated_input_count"] = 0
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
    return out
