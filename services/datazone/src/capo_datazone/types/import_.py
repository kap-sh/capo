"""Generated from Smithy shape ``com.amazonaws.datazone#Import``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.form_type_name
    import capo_datazone.types.revision


class Import(TypedDict, closed=True):
    name: "capo_datazone.types.form_type_name.FormTypeName"
    """<p>The name of the import.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Import) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> Import:
    out: Import = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Import.name required")
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("Import.revision required")
    return out


def redact_sensitive(value: Import) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
