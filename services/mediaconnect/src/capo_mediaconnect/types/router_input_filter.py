"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_type_list
    import capo_mediaconnect.types.router_network_interface_arn_list
    import capo_mediaconnect.types.routing_scope_list
    import capo_mediaconnect.types.string_list


class _RouterInputFilter_NameContains(TypedDict, closed=True):
    NameContains: "capo_mediaconnect.types.string_list.StringList"


class _RouterInputFilter_RegionNames(TypedDict, closed=True):
    RegionNames: "capo_mediaconnect.types.string_list.StringList"


class _RouterInputFilter_NetworkInterfaceArns(TypedDict, closed=True):
    NetworkInterfaceArns: "capo_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList"


class _RouterInputFilter_RoutingScopes(TypedDict, closed=True):
    RoutingScopes: "capo_mediaconnect.types.routing_scope_list.RoutingScopeList"


class _RouterInputFilter_InputTypes(TypedDict, closed=True):
    InputTypes: "capo_mediaconnect.types.router_input_type_list.RouterInputTypeList"


RouterInputFilter: TypeAlias = (
    _RouterInputFilter_NameContains
    | _RouterInputFilter_RegionNames
    | _RouterInputFilter_NetworkInterfaceArns
    | _RouterInputFilter_RoutingScopes
    | _RouterInputFilter_InputTypes
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouterInputFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "NameContains" in value:
        import capo_mediaconnect.types.string_list

        return {
            "nameContains": capo_mediaconnect.types.string_list.serialize_json(
                value["NameContains"]
            )
        }
    elif "RegionNames" in value:
        import capo_mediaconnect.types.string_list

        return {
            "regionNames": capo_mediaconnect.types.string_list.serialize_json(
                value["RegionNames"]
            )
        }
    elif "NetworkInterfaceArns" in value:
        import capo_mediaconnect.types.router_network_interface_arn_list

        return {
            "networkInterfaceArns": capo_mediaconnect.types.router_network_interface_arn_list.serialize_json(
                value["NetworkInterfaceArns"]
            )
        }
    elif "RoutingScopes" in value:
        import capo_mediaconnect.types.routing_scope_list

        return {
            "routingScopes": capo_mediaconnect.types.routing_scope_list.serialize_json(
                value["RoutingScopes"]
            )
        }
    elif "InputTypes" in value:
        import capo_mediaconnect.types.router_input_type_list

        return {
            "inputTypes": capo_mediaconnect.types.router_input_type_list.serialize_json(
                value["InputTypes"]
            )
        }
    else:
        raise SerializationError("RouterInputFilter: no variant present")


def deserialize_json(data: dict) -> RouterInputFilter:
    if data.get("nameContains") is not None:
        import capo_mediaconnect.types.string_list

        return {
            "NameContains": capo_mediaconnect.types.string_list.deserialize_json(
                data["nameContains"]
            )
        }
    elif data.get("regionNames") is not None:
        import capo_mediaconnect.types.string_list

        return {
            "RegionNames": capo_mediaconnect.types.string_list.deserialize_json(
                data["regionNames"]
            )
        }
    elif data.get("networkInterfaceArns") is not None:
        import capo_mediaconnect.types.router_network_interface_arn_list

        return {
            "NetworkInterfaceArns": capo_mediaconnect.types.router_network_interface_arn_list.deserialize_json(
                data["networkInterfaceArns"]
            )
        }
    elif data.get("routingScopes") is not None:
        import capo_mediaconnect.types.routing_scope_list

        return {
            "RoutingScopes": capo_mediaconnect.types.routing_scope_list.deserialize_json(
                data["routingScopes"]
            )
        }
    elif data.get("inputTypes") is not None:
        import capo_mediaconnect.types.router_input_type_list

        return {
            "InputTypes": capo_mediaconnect.types.router_input_type_list.deserialize_json(
                data["inputTypes"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RouterInputFilter: no recognized variant key")
