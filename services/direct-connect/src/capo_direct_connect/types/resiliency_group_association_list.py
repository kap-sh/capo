"""Generated from Smithy shape ``com.amazonaws.directconnect#ResiliencyGroupAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.resiliency_group_association

ResiliencyGroupAssociationList: TypeAlias = list[
    "capo_direct_connect.types.resiliency_group_association.ResiliencyGroupAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResiliencyGroupAssociationList) -> list:
    import capo_direct_connect.types.resiliency_group_association

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.resiliency_group_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResiliencyGroupAssociationList:
    import capo_direct_connect.types.resiliency_group_association

    out: ResiliencyGroupAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.resiliency_group_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResiliencyGroupAssociationList) -> list:
    import capo_direct_connect.types.resiliency_group_association

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.resiliency_group_association.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ResiliencyGroupAssociationList:
    import capo_direct_connect.types.resiliency_group_association

    out: ResiliencyGroupAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.resiliency_group_association.deserialize_cbor(
                item
            )
        )
    return out
