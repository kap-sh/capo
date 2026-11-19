"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpRoutesInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.ip_route_info

IpRoutesInfo: TypeAlias = list["capo_directory_service.types.ip_route_info.IpRouteInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRoutesInfo) -> list:
    import capo_directory_service.types.ip_route_info

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.ip_route_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IpRoutesInfo:
    import capo_directory_service.types.ip_route_info

    out: IpRoutesInfo = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.ip_route_info.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpRoutesInfo) -> list:
    import capo_directory_service.types.ip_route_info

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.ip_route_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IpRoutesInfo:
    import capo_directory_service.types.ip_route_info

    out: IpRoutesInfo = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.ip_route_info.deserialize_cbor(item))
    return out
