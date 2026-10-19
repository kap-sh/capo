"""Generated from Smithy shape ``com.amazonaws.datazone#FormEntryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.form_type_identifier
    import capo_datazone.types.revision


class FormEntryInput(TypedDict, closed=True):
    type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The type ID of the form entry.</p>"""
    type_revision: "capo_datazone.types.revision.Revision"
    """<p>The type revision of the form entry.</p>"""
    required: NotRequired["bool"]
    """<p>Specifies whether a form entry is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormEntryInput) -> dict:
    out: dict = {}
    out["typeIdentifier"] = value["type_identifier"]
    out["typeRevision"] = value["type_revision"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> FormEntryInput:
    out: FormEntryInput = {}  # type: ignore[typeddict-item]
    if data.get("typeIdentifier") is not None:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        out["type_identifier"] = ""
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    else:
        out["type_revision"] = ""
    if data.get("required") is not None:
        out["required"] = data["required"]
    return out
