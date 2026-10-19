"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.form_name
    import capo_datazone.types.form_type_name
    import capo_datazone.types.revision


class MetadataFormSummary(TypedDict, closed=True):
    form_name: NotRequired["capo_datazone.types.form_name.FormName"]
    """<p>The form name of the metadata form.</p>"""
    type_name: "capo_datazone.types.form_type_name.FormTypeName"
    """<p>The type name of the metadata form.</p>"""
    type_revision: "capo_datazone.types.revision.Revision"
    """<p>The type revision of the metadata form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormSummary) -> dict:
    out: dict = {}
    if "form_name" in value:
        out["formName"] = value["form_name"]
    out["typeName"] = value["type_name"]
    out["typeRevision"] = value["type_revision"]
    return out


def deserialize_json(data: dict) -> MetadataFormSummary:
    out: MetadataFormSummary = {}  # type: ignore[typeddict-item]
    if data.get("formName") is not None:
        out["form_name"] = data["formName"]
    if data.get("typeName") is not None:
        out["type_name"] = data["typeName"]
    else:
        out["type_name"] = ""
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    else:
        out["type_revision"] = ""
    return out


def redact_sensitive(value: MetadataFormSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type_name" in value:
        out["type_name"] = "*** Sensitive Data Redacted ***"
    return out
