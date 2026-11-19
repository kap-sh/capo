"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.image_builder

ImageBuilderList: TypeAlias = list["capo_appstream.types.image_builder.ImageBuilder"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderList) -> list:
    import capo_appstream.types.image_builder

    out: list = []
    for item in value:
        out.append(capo_appstream.types.image_builder.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageBuilderList:
    import capo_appstream.types.image_builder

    out: ImageBuilderList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.image_builder.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageBuilderList) -> list:
    import capo_appstream.types.image_builder

    out: list = []
    for item in value:
        out.append(capo_appstream.types.image_builder.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ImageBuilderList:
    import capo_appstream.types.image_builder

    out: ImageBuilderList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.image_builder.deserialize_cbor(item))
    return out
