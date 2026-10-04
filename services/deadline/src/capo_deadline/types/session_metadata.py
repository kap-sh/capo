"""Generated from Smithy shape ``com.amazonaws.deadline#SessionMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.session_metadata_key
    import capo_deadline.types.session_metadata_value

SessionMetadata: TypeAlias = dict[
    "capo_deadline.types.session_metadata_key.SessionMetadataKey",
    "capo_deadline.types.session_metadata_value.SessionMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SessionMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SessionMetadata:
    out: SessionMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
