"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpRoutes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.ip_route

IpRoutes: TypeAlias = list["capo_directory_service.types.ip_route.IpRoute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRoutes) -> list:
    import capo_directory_service.types.ip_route

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.ip_route.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IpRoutes:
    import capo_directory_service.types.ip_route

    out: IpRoutes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.ip_route.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpRoutes) -> list:
    import capo_directory_service.types.ip_route

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.ip_route.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IpRoutes:
    import capo_directory_service.types.ip_route

    out: IpRoutes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.ip_route.deserialize_cbor(item))
    return out
