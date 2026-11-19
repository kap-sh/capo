"""Generated from Smithy shape ``com.amazonaws.directconnect#RouteFilterCidrStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.route_filter_cidr_string

RouteFilterCidrStringList: TypeAlias = list[
    "capo_direct_connect.types.route_filter_cidr_string.RouteFilterCidrString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteFilterCidrStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RouteFilterCidrStringList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RouteFilterCidrStringList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> RouteFilterCidrStringList:
    return [item for item in data if item is not None]
