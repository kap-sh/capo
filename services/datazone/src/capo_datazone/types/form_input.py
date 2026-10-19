"""Generated from Smithy shape ``com.amazonaws.datazone#FormInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.form_name
    import capo_datazone.types.form_type_identifier
    import capo_datazone.types.revision_input


class FormInput(TypedDict, closed=True):
    form_name: "capo_datazone.types.form_name.FormName"
    """<p>The name of the metadata form.</p>"""
    type_identifier: NotRequired[
        "capo_datazone.types.form_type_identifier.FormTypeIdentifier"
    ]
    """<p>The ID of the metadata form type.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision_input.RevisionInput"]
    """<p>The revision of the metadata form type.</p>"""
    content: NotRequired["str"]
    """<p>The content of the metadata form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    if "type_identifier" in value:
        out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> FormInput:
    out: FormInput = {}  # type: ignore[typeddict-item]
    if data.get("formName") is not None:
        out["form_name"] = data["formName"]
    else:
        out["form_name"] = ""
    if data.get("typeIdentifier") is not None:
        out["type_identifier"] = data["typeIdentifier"]
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    if data.get("content") is not None:
        out["content"] = data["content"]
    return out
