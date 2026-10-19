"""Generated from Smithy shape ``com.amazonaws.omics#ImportReferenceSourceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.job_status_message
    import capo_omics.types.reference_description
    import capo_omics.types.reference_id
    import capo_omics.types.reference_import_job_item_status
    import capo_omics.types.reference_name
    import capo_omics.types.s3_uri
    import capo_omics.types.tag_map


class ImportReferenceSourceItem(TypedDict, closed=True):
    source_file: NotRequired["capo_omics.types.s3_uri.S3Uri"]
    """<p>The source file's location in Amazon S3.</p>"""
    status: (
        "capo_omics.types.reference_import_job_item_status.ReferenceImportJobItemStatus"
    )
    """<p>The source's status.</p>"""
    status_message: NotRequired["capo_omics.types.job_status_message.JobStatusMessage"]
    """<p>The source's status message.</p>"""
    name: NotRequired["capo_omics.types.reference_name.ReferenceName"]
    """<p>The source's name.</p>"""
    description: NotRequired[
        "capo_omics.types.reference_description.ReferenceDescription"
    ]
    """<p>The source's description.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>The source's tags.</p>"""
    reference_id: NotRequired["capo_omics.types.reference_id.ReferenceId"]
    """<p>The source's reference ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportReferenceSourceItem) -> dict:
    out: dict = {}
    if "source_file" in value:
        out["sourceFile"] = value["source_file"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "reference_id" in value:
        out["referenceId"] = value["reference_id"]
    return out


def deserialize_json(data: dict) -> ImportReferenceSourceItem:
    out: ImportReferenceSourceItem = {}  # type: ignore[typeddict-item]
    if data.get("sourceFile") is not None:
        out["source_file"] = data["sourceFile"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    return out
