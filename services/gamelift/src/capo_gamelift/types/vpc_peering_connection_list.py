"""Generated from Smithy shape ``com.amazonaws.gamelift#VpcPeeringConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.vpc_peering_connection

VpcPeeringConnectionList: TypeAlias = list[
    "capo_gamelift.types.vpc_peering_connection.VpcPeeringConnection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcPeeringConnectionList) -> list:
    import capo_gamelift.types.vpc_peering_connection

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.vpc_peering_connection.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VpcPeeringConnectionList:
    import capo_gamelift.types.vpc_peering_connection

    out: VpcPeeringConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.vpc_peering_connection.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VpcPeeringConnectionList) -> list:
    import capo_gamelift.types.vpc_peering_connection

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.vpc_peering_connection.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> VpcPeeringConnectionList:
    import capo_gamelift.types.vpc_peering_connection

    out: VpcPeeringConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.vpc_peering_connection.deserialize_cbor(item))
    return out
