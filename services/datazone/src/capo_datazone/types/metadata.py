"""Generated from Smithy shape ``com.amazonaws.datazone#Metadata``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.metadata_key
    import capo_datazone.types.metadata_value

Metadata: TypeAlias = dict[
    "capo_datazone.types.metadata_key.MetadataKey",
    "capo_datazone.types.metadata_value.MetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Metadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Metadata:
    out: Metadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: Metadata) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
