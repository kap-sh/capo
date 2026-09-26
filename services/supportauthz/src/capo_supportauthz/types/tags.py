"""Generated from Smithy shape ``com.amazonaws.supportauthz#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supportauthz.types.tag_key
    import capo_supportauthz.types.tag_value

Tags: TypeAlias = dict[
    "capo_supportauthz.types.tag_key.TagKey",
    "capo_supportauthz.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
