"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.creation_job_id
    import capo_omics.types.md5
    import capo_omics.types.reference_arn
    import capo_omics.types.reference_creation_type
    import capo_omics.types.reference_description
    import capo_omics.types.reference_files
    import capo_omics.types.reference_id
    import capo_omics.types.reference_name
    import capo_omics.types.reference_status
    import capo_omics.types.reference_store_id


class GetReferenceMetadataResponse(TypedDict, closed=True):
    id: "capo_omics.types.reference_id.ReferenceId"
    """<p>The reference's ID.</p>"""
    arn: "capo_omics.types.reference_arn.ReferenceArn"
    """<p>The reference's ARN.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The reference's reference store ID.</p>"""
    md5: "capo_omics.types.md5.Md5"
    """<p>The reference's MD5 checksum.</p>"""
    status: NotRequired["capo_omics.types.reference_status.ReferenceStatus"]
    """<p>The reference's status.</p>"""
    name: NotRequired["capo_omics.types.reference_name.ReferenceName"]
    """<p>The reference's name.</p>"""
    description: NotRequired[
        "capo_omics.types.reference_description.ReferenceDescription"
    ]
    """<p>The reference's description.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the reference was created.</p>"""
    update_time: "datetime.datetime"
    """<p>When the reference was updated.</p>"""
    files: NotRequired["capo_omics.types.reference_files.ReferenceFiles"]
    """<p>The reference's files.</p>"""
    creation_type: NotRequired[
        "capo_omics.types.reference_creation_type.ReferenceCreationType"
    ]
    """<p>The reference's creation type.</p>"""
    creation_job_id: NotRequired["capo_omics.types.creation_job_id.CreationJobId"]
    """<p>The reference's creation job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReferenceMetadataResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["md5"] = value["md5"]
    if "status" in value:
        out["status"] = value["status"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    import capo_omics._protocol.serialize

    out["updateTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    if "files" in value:
        import capo_omics.types.reference_files

        out["files"] = capo_omics.types.reference_files.serialize_json(value["files"])
    if "creation_type" in value:
        out["creationType"] = value["creation_type"]
    if "creation_job_id" in value:
        out["creationJobId"] = value["creation_job_id"]
    return out


def deserialize_json(data: dict) -> GetReferenceMetadataResponse:
    out: GetReferenceMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("referenceStoreId") is not None:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        out["reference_store_id"] = ""
    if data.get("md5") is not None:
        out["md5"] = data["md5"]
    else:
        out["md5"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("files") is not None:
        import capo_omics.types.reference_files

        out["files"] = capo_omics.types.reference_files.deserialize_json(data["files"])
    if data.get("creationType") is not None:
        out["creation_type"] = data["creationType"]
    if data.get("creationJobId") is not None:
        out["creation_job_id"] = data["creationJobId"]
    return out
