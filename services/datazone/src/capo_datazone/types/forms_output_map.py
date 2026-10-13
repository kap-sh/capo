"""Generated from Smithy shape ``com.amazonaws.datazone#FormsOutputMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.form_entry_output
    import capo_datazone.types.form_name

FormsOutputMap: TypeAlias = dict[
    "capo_datazone.types.form_name.FormName",
    "capo_datazone.types.form_entry_output.FormEntryOutput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FormsOutputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_datazone.types.form_entry_output

        out[key] = capo_datazone.types.form_entry_output.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FormsOutputMap:
    out: FormsOutputMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_datazone.types.form_entry_output

        out[key] = capo_datazone.types.form_entry_output.deserialize_json(value)
    return out


def redact_sensitive(value: FormsOutputMap) -> dict[str, Any]:
    import capo_datazone.types.form_entry_output

    return {
        key: capo_datazone.types.form_entry_output.redact_sensitive(item)
        for key, item in value.items()
    }
