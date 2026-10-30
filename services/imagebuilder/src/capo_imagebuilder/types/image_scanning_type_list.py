"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanningTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_scanning_type

ImageScanningTypeList: TypeAlias = list[
    "capo_imagebuilder.types.image_scanning_type.ImageScanningType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanningTypeList) -> list:
    import capo_imagebuilder.types.image_scanning_type

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.image_scanning_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageScanningTypeList:
    import capo_imagebuilder.types.image_scanning_type

    out: ImageScanningTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_imagebuilder.types.image_scanning_type.deserialize_json(item))
    return out
