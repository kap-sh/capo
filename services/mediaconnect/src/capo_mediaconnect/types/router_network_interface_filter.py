"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_network_interface_type_list
    import capo_mediaconnect.types.string_list


class RouterNetworkInterfaceFilterRegionNamesMember(TypedDict, closed=True):
    RegionNames: "capo_mediaconnect.types.string_list.StringList"


class RouterNetworkInterfaceFilterNetworkInterfaceTypesMember(TypedDict, closed=True):
    NetworkInterfaceTypes: "capo_mediaconnect.types.router_network_interface_type_list.RouterNetworkInterfaceTypeList"


class RouterNetworkInterfaceFilterNameContainsMember(TypedDict, closed=True):
    NameContains: "capo_mediaconnect.types.string_list.StringList"


RouterNetworkInterfaceFilter: TypeAlias = (
    RouterNetworkInterfaceFilterRegionNamesMember
    | RouterNetworkInterfaceFilterNetworkInterfaceTypesMember
    | RouterNetworkInterfaceFilterNameContainsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouterNetworkInterfaceFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "RegionNames" in value:
        import capo_mediaconnect.types.string_list

        return {
            "regionNames": capo_mediaconnect.types.string_list.serialize_json(
                value["RegionNames"]
            )
        }
    elif "NetworkInterfaceTypes" in value:
        import capo_mediaconnect.types.router_network_interface_type_list

        return {
            "networkInterfaceTypes": capo_mediaconnect.types.router_network_interface_type_list.serialize_json(
                value["NetworkInterfaceTypes"]
            )
        }
    elif "NameContains" in value:
        import capo_mediaconnect.types.string_list

        return {
            "nameContains": capo_mediaconnect.types.string_list.serialize_json(
                value["NameContains"]
            )
        }
    else:
        raise SerializationError("RouterNetworkInterfaceFilter: no variant present")


def deserialize_json(data: dict) -> RouterNetworkInterfaceFilter:
    if data.get("regionNames") is not None:
        import capo_mediaconnect.types.string_list

        return {
            "RegionNames": capo_mediaconnect.types.string_list.deserialize_json(
                data["regionNames"]
            )
        }
    elif data.get("networkInterfaceTypes") is not None:
        import capo_mediaconnect.types.router_network_interface_type_list

        return {
            "NetworkInterfaceTypes": capo_mediaconnect.types.router_network_interface_type_list.deserialize_json(
                data["networkInterfaceTypes"]
            )
        }
    elif data.get("nameContains") is not None:
        import capo_mediaconnect.types.string_list

        return {
            "NameContains": capo_mediaconnect.types.string_list.deserialize_json(
                data["nameContains"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RouterNetworkInterfaceFilter: no recognized variant key"
        )
