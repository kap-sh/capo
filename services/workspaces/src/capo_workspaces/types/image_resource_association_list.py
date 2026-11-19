"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.image_resource_association

ImageResourceAssociationList: TypeAlias = list[
    "capo_workspaces.types.image_resource_association.ImageResourceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageResourceAssociationList) -> list:
    import capo_workspaces.types.image_resource_association

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.image_resource_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImageResourceAssociationList:
    import capo_workspaces.types.image_resource_association

    out: ImageResourceAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.image_resource_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageResourceAssociationList) -> list:
    import capo_workspaces.types.image_resource_association

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.image_resource_association.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ImageResourceAssociationList:
    import capo_workspaces.types.image_resource_association

    out: ImageResourceAssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.image_resource_association.deserialize_cbor(item)
        )
    return out
