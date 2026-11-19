"""Generated from Smithy shape ``com.amazonaws.directconnect#RouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.route

RouteList: TypeAlias = list["capo_direct_connect.types.route.Route"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteList) -> list:
    import capo_direct_connect.types.route

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.route.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RouteList:
    import capo_direct_connect.types.route

    out: RouteList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.route.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RouteList) -> list:
    import capo_direct_connect.types.route

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.route.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RouteList:
    import capo_direct_connect.types.route

    out: RouteList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.route.deserialize_cbor(item))
    return out
