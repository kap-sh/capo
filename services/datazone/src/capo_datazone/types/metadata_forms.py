"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataForms``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.form_output

MetadataForms: TypeAlias = list["capo_datazone.types.form_output.FormOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataForms) -> list:
    import capo_datazone.types.form_output

    out: list = []
    for item in value:
        out.append(capo_datazone.types.form_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataForms:
    import capo_datazone.types.form_output

    out: MetadataForms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.form_output.deserialize_json(item))
    return out


def redact_sensitive(value: MetadataForms) -> list[Any]:
    import capo_datazone.types.form_output

    return [capo_datazone.types.form_output.redact_sensitive(item) for item in value]
