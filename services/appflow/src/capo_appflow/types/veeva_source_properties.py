"""Generated from Smithy shape ``com.amazonaws.appflow#VeevaSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.document_type
    import capo_appflow.types.object


class VeevaSourceProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the Veeva flow source. </p>"""
    document_type: NotRequired["capo_appflow.types.document_type.DocumentType"]
    """<p>The document type specified in the Veeva document extract flow.</p>"""
    include_source_files: "capo_appflow.types.boolean.Boolean"
    """<p>Boolean value to include source files in Veeva document extract flow.</p>"""
    include_renditions: "capo_appflow.types.boolean.Boolean"
    """<p>Boolean value to include file renditions in Veeva document extract flow.</p>"""
    include_all_versions: "capo_appflow.types.boolean.Boolean"
    """<p>Boolean value to include All Versions of files in Veeva document extract flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VeevaSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    if "document_type" in value:
        out["documentType"] = value["document_type"]
    out["includeSourceFiles"] = value.get("include_source_files", False)
    out["includeRenditions"] = value.get("include_renditions", False)
    out["includeAllVersions"] = value.get("include_all_versions", False)
    return out


def deserialize_json(data: dict) -> VeevaSourceProperties:
    out: VeevaSourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("object") is not None:
        out["object"] = data["object"]
    else:
        out["object"] = ""
    if data.get("documentType") is not None:
        out["document_type"] = data["documentType"]
    if data.get("includeSourceFiles") is not None:
        out["include_source_files"] = data["includeSourceFiles"]
    else:
        out["include_source_files"] = False
    if data.get("includeRenditions") is not None:
        out["include_renditions"] = data["includeRenditions"]
    else:
        out["include_renditions"] = False
    if data.get("includeAllVersions") is not None:
        out["include_all_versions"] = data["includeAllVersions"]
    else:
        out["include_all_versions"] = False
    return out
