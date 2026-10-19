"""Generated from Smithy shape ``com.amazonaws.datazone#FormEntryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.form_type_name
    import capo_datazone.types.revision


class FormEntryOutput(TypedDict, closed=True):
    type_name: "capo_datazone.types.form_type_name.FormTypeName"
    """<p>The name of the type of the form entry.</p>"""
    type_revision: "capo_datazone.types.revision.Revision"
    """<p>The type revision of the form entry.</p>"""
    required: NotRequired["bool"]
    """<p>Specifies whether a form entry is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormEntryOutput) -> dict:
    out: dict = {}
    out["typeName"] = value["type_name"]
    out["typeRevision"] = value["type_revision"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> FormEntryOutput:
    out: FormEntryOutput = {}  # type: ignore[typeddict-item]
    if data.get("typeName") is not None:
        out["type_name"] = data["typeName"]
    else:
        out["type_name"] = ""
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    else:
        out["type_revision"] = ""
    if data.get("required") is not None:
        out["required"] = data["required"]
    return out


def redact_sensitive(value: FormEntryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type_name" in value:
        out["type_name"] = "*** Sensitive Data Redacted ***"
    return out
