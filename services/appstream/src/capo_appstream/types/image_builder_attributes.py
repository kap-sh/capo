"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.image_builder_attribute

ImageBuilderAttributes: TypeAlias = list[
    "capo_appstream.types.image_builder_attribute.ImageBuilderAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderAttributes) -> list:
    import capo_appstream.types.image_builder_attribute

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.image_builder_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImageBuilderAttributes:
    import capo_appstream.types.image_builder_attribute

    out: ImageBuilderAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.image_builder_attribute.deserialize_aws_json_1_1(item)
        )
    return out
