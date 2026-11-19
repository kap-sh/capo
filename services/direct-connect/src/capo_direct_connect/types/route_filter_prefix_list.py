"""Generated from Smithy shape ``com.amazonaws.directconnect#RouteFilterPrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.route_filter_prefix

RouteFilterPrefixList: TypeAlias = list[
    "capo_direct_connect.types.route_filter_prefix.RouteFilterPrefix"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteFilterPrefixList) -> list:
    import capo_direct_connect.types.route_filter_prefix

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.route_filter_prefix.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RouteFilterPrefixList:
    import capo_direct_connect.types.route_filter_prefix

    out: RouteFilterPrefixList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.route_filter_prefix.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RouteFilterPrefixList) -> list:
    import capo_direct_connect.types.route_filter_prefix

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.route_filter_prefix.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RouteFilterPrefixList:
    import capo_direct_connect.types.route_filter_prefix

    out: RouteFilterPrefixList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.route_filter_prefix.deserialize_cbor(item))
    return out
