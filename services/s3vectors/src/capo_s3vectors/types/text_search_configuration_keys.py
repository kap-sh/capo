"""Generated from Smithy shape ``com.amazonaws.s3vectors#TextSearchConfigurationKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3vectors.types.text_search_configuration_key

TextSearchConfigurationKeys: TypeAlias = list[
    "capo_s3vectors.types.text_search_configuration_key.TextSearchConfigurationKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: TextSearchConfigurationKeys) -> list:
    import capo_s3vectors.types.text_search_configuration_key

    out: list = []
    for item in value:
        out.append(
            capo_s3vectors.types.text_search_configuration_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TextSearchConfigurationKeys:
    import capo_s3vectors.types.text_search_configuration_key

    out: TextSearchConfigurationKeys = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_s3vectors.types.text_search_configuration_key.deserialize_json(item)
        )
    return out
