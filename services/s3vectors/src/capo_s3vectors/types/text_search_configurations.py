"""Generated from Smithy shape ``com.amazonaws.s3vectors#TextSearchConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3vectors.types.text_search_configuration

TextSearchConfigurations: TypeAlias = list[
    "capo_s3vectors.types.text_search_configuration.TextSearchConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TextSearchConfigurations) -> list:
    import capo_s3vectors.types.text_search_configuration

    out: list = []
    for item in value:
        out.append(capo_s3vectors.types.text_search_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> TextSearchConfigurations:
    import capo_s3vectors.types.text_search_configuration

    out: TextSearchConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_s3vectors.types.text_search_configuration.deserialize_json(item)
        )
    return out
