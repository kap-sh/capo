"""Generated from Smithy shape ``com.amazonaws.glue#PublishDataQualityResultTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.name_string

PublishDataQualityResultTags: TypeAlias = dict[
    "capo_glue.types.name_string.NameString", "capo_glue.types.name_string.NameString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PublishDataQualityResultTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> PublishDataQualityResultTags:
    out: PublishDataQualityResultTags = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
