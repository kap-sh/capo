"""Generated from Smithy shape ``com.amazonaws.appstream#ImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.image

ImageList: TypeAlias = list["capo_appstream.types.image.Image"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageList) -> list:
    import capo_appstream.types.image

    out: list = []
    for item in value:
        out.append(capo_appstream.types.image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageList:
    import capo_appstream.types.image

    out: ImageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.image.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageList) -> list:
    import capo_appstream.types.image

    out: list = []
    for item in value:
        out.append(capo_appstream.types.image.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ImageList:
    import capo_appstream.types.image

    out: ImageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.image.deserialize_cbor(item))
    return out
