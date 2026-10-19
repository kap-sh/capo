"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.form_type_identifier
    import capo_datazone.types.revision


class MetadataFormReference(TypedDict, closed=True):
    type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The type ID of the metadata form reference.</p>"""
    type_revision: "capo_datazone.types.revision.Revision"
    """<p>The type revision of the metadata form reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormReference) -> dict:
    out: dict = {}
    out["typeIdentifier"] = value["type_identifier"]
    out["typeRevision"] = value["type_revision"]
    return out


def deserialize_json(data: dict) -> MetadataFormReference:
    out: MetadataFormReference = {}  # type: ignore[typeddict-item]
    if data.get("typeIdentifier") is not None:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        out["type_identifier"] = ""
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    else:
        out["type_revision"] = ""
    return out
