"""Generated from Smithy shape ``com.amazonaws.datazone#FormOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.form_name
    import capo_datazone.types.form_type_name
    import capo_datazone.types.revision


class FormOutput(TypedDict, closed=True):
    form_name: "capo_datazone.types.form_name.FormName"
    """<p>The name of the metadata form.</p>"""
    type_name: NotRequired["capo_datazone.types.form_type_name.FormTypeName"]
    """<p>The name of the metadata form type.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the metadata form type.</p>"""
    content: NotRequired["str"]
    """<p>The content of the metadata form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormOutput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    if "type_name" in value:
        out["typeName"] = value["type_name"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> FormOutput:
    out: FormOutput = {}  # type: ignore[typeddict-item]
    if data.get("formName") is not None:
        out["form_name"] = data["formName"]
    else:
        raise DeserializationError("FormOutput.form_name required")
    if data.get("typeName") is not None:
        out["type_name"] = data["typeName"]
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    if data.get("content") is not None:
        out["content"] = data["content"]
    return out


def redact_sensitive(value: FormOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type_name" in value:
        out["type_name"] = "*** Sensitive Data Redacted ***"
    return out
