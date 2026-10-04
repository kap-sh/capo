"""Generated from Smithy shape ``com.amazonaws.appstream#ImageType``."""

from typing import Literal, TypeAlias, cast

"""<p>The image type is the type of AppStream image resource.</p>"""
ImageType: TypeAlias = Literal[
    "CUSTOM",
    "NATIVE",
    "BYOL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageType:
    return cast(ImageType, data)
