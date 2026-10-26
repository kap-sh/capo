"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn_list
    import capo_mediaconnect.types.router_network_interface_arn_list
    import capo_mediaconnect.types.router_output_type_list
    import capo_mediaconnect.types.routing_scope_list
    import capo_mediaconnect.types.string_list


class _RouterOutputFilter_RegionNames(TypedDict, closed=True):
    RegionNames: "capo_mediaconnect.types.string_list.StringList"


class _RouterOutputFilter_NetworkInterfaceArns(TypedDict, closed=True):
    NetworkInterfaceArns: "capo_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList"


class _RouterOutputFilter_RoutingScopes(TypedDict, closed=True):
    RoutingScopes: "capo_mediaconnect.types.routing_scope_list.RoutingScopeList"


class _RouterOutputFilter_OutputTypes(TypedDict, closed=True):
    OutputTypes: "capo_mediaconnect.types.router_output_type_list.RouterOutputTypeList"


class _RouterOutputFilter_RoutedInputArns(TypedDict, closed=True):
    RoutedInputArns: "capo_mediaconnect.types.router_input_arn_list.RouterInputArnList"


class _RouterOutputFilter_NameContains(TypedDict, closed=True):
    NameContains: "capo_mediaconnect.types.string_list.StringList"


RouterOutputFilter: TypeAlias = (
    _RouterOutputFilter_RegionNames
    | _RouterOutputFilter_NetworkInterfaceArns
    | _RouterOutputFilter_RoutingScopes
    | _RouterOutputFilter_OutputTypes
    | _RouterOutputFilter_RoutedInputArns
    | _RouterOutputFilter_NameContains
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouterOutputFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
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
    elif "OutputTypes" in value:
        import capo_mediaconnect.types.router_output_type_list

        return {
            "outputTypes": capo_mediaconnect.types.router_output_type_list.serialize_json(
                value["OutputTypes"]
            )
        }
    elif "RoutedInputArns" in value:
        import capo_mediaconnect.types.router_input_arn_list

        return {
            "routedInputArns": capo_mediaconnect.types.router_input_arn_list.serialize_json(
                value["RoutedInputArns"]
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
        raise SerializationError("RouterOutputFilter: no variant present")


def deserialize_json(data: dict) -> RouterOutputFilter:
    if data.get("regionNames") is not None:
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
    elif data.get("outputTypes") is not None:
        import capo_mediaconnect.types.router_output_type_list

        return {
            "OutputTypes": capo_mediaconnect.types.router_output_type_list.deserialize_json(
                data["outputTypes"]
            )
        }
    elif data.get("routedInputArns") is not None:
        import capo_mediaconnect.types.router_input_arn_list

        return {
            "RoutedInputArns": capo_mediaconnect.types.router_input_arn_list.deserialize_json(
                data["routedInputArns"]
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
        raise DeserializationError("RouterOutputFilter: no recognized variant key")
