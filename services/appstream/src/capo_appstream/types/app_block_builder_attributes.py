"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.app_block_builder_attribute

AppBlockBuilderAttributes: TypeAlias = list[
    "capo_appstream.types.app_block_builder_attribute.AppBlockBuilderAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilderAttributes) -> list:
    import capo_appstream.types.app_block_builder_attribute

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.app_block_builder_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AppBlockBuilderAttributes:
    import capo_appstream.types.app_block_builder_attribute

    out: AppBlockBuilderAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.app_block_builder_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppBlockBuilderAttributes) -> list:
    import capo_appstream.types.app_block_builder_attribute

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.app_block_builder_attribute.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AppBlockBuilderAttributes:
    import capo_appstream.types.app_block_builder_attribute

    out: AppBlockBuilderAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.app_block_builder_attribute.deserialize_cbor(item)
        )
    return out
