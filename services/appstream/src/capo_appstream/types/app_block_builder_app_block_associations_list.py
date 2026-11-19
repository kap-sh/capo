"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderAppBlockAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.app_block_builder_app_block_association

AppBlockBuilderAppBlockAssociationsList: TypeAlias = list[
    "capo_appstream.types.app_block_builder_app_block_association.AppBlockBuilderAppBlockAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilderAppBlockAssociationsList) -> list:
    import capo_appstream.types.app_block_builder_app_block_association

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.app_block_builder_app_block_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AppBlockBuilderAppBlockAssociationsList:
    import capo_appstream.types.app_block_builder_app_block_association

    out: AppBlockBuilderAppBlockAssociationsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.app_block_builder_app_block_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppBlockBuilderAppBlockAssociationsList) -> list:
    import capo_appstream.types.app_block_builder_app_block_association

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.app_block_builder_app_block_association.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AppBlockBuilderAppBlockAssociationsList:
    import capo_appstream.types.app_block_builder_app_block_association

    out: AppBlockBuilderAppBlockAssociationsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.app_block_builder_app_block_association.deserialize_cbor(
                item
            )
        )
    return out
