"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormInputs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.form_input

MetadataFormInputs: TypeAlias = list["capo_datazone.types.form_input.FormInput"]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormInputs) -> list:
    import capo_datazone.types.form_input

    out: list = []
    for item in value:
        out.append(capo_datazone.types.form_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataFormInputs:
    import capo_datazone.types.form_input

    out: MetadataFormInputs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.form_input.deserialize_json(item))
    return out


def redact_sensitive(value: MetadataFormInputs) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
