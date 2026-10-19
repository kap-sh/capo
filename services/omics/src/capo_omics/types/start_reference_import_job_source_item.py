"""Generated from Smithy shape ``com.amazonaws.omics#StartReferenceImportJobSourceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.reference_description
    import capo_omics.types.reference_name
    import capo_omics.types.s3_uri
    import capo_omics.types.tag_map


class StartReferenceImportJobSourceItem(TypedDict, closed=True):
    source_file: "capo_omics.types.s3_uri.S3Uri"
    """<p>The source file's location in Amazon S3.</p>"""
    name: "capo_omics.types.reference_name.ReferenceName"
    """<p>The source's name.</p>"""
    description: NotRequired[
        "capo_omics.types.reference_description.ReferenceDescription"
    ]
    """<p>The source's description.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>The source's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReferenceImportJobSourceItem) -> dict:
    out: dict = {}
    out["sourceFile"] = value["source_file"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartReferenceImportJobSourceItem:
    out: StartReferenceImportJobSourceItem = {}  # type: ignore[typeddict-item]
    if data.get("sourceFile") is not None:
        out["source_file"] = data["sourceFile"]
    else:
        out["source_file"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    return out
