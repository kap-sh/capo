"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ImageFormatList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.image_format

ImageFormatList: TypeAlias = list[
    "capo_partnercentral_marketing.types.image_format.ImageFormat"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageFormatList) -> list:
    import capo_partnercentral_marketing.types.image_format

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.image_format.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ImageFormatList:
    import capo_partnercentral_marketing.types.image_format

    out: ImageFormatList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.image_format.deserialize_cbor(item)
        )
    return out
