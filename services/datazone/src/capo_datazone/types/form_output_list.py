"""Generated from Smithy shape ``com.amazonaws.datazone#FormOutputList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.form_output

FormOutputList: TypeAlias = list["capo_datazone.types.form_output.FormOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: FormOutputList) -> list:
    import capo_datazone.types.form_output

    out: list = []
    for item in value:
        out.append(capo_datazone.types.form_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> FormOutputList:
    import capo_datazone.types.form_output

    out: FormOutputList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.form_output.deserialize_json(item))
    return out


def redact_sensitive(value: FormOutputList) -> list[Any]:
    import capo_datazone.types.form_output

    return [capo_datazone.types.form_output.redact_sensitive(item) for item in value]
