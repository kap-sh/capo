"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.creation_type
    import capo_omics.types.e_tag
    import capo_omics.types.file_type
    import capo_omics.types.read_set_arn
    import capo_omics.types.read_set_description
    import capo_omics.types.read_set_id
    import capo_omics.types.read_set_name
    import capo_omics.types.read_set_status
    import capo_omics.types.read_set_status_message
    import capo_omics.types.reference_arn
    import capo_omics.types.sample_id
    import capo_omics.types.sequence_information
    import capo_omics.types.sequence_store_id
    import capo_omics.types.subject_id


class ReadSetListItem(TypedDict, closed=True):
    id: "capo_omics.types.read_set_id.ReadSetId"
    """<p>The read set's ID.</p>"""
    arn: "capo_omics.types.read_set_arn.ReadSetArn"
    """<p>The read set's ARN.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    subject_id: NotRequired["capo_omics.types.subject_id.SubjectId"]
    """<p>The read set's subject ID.</p>"""
    sample_id: NotRequired["capo_omics.types.sample_id.SampleId"]
    """<p>The read set's sample ID.</p>"""
    status: "capo_omics.types.read_set_status.ReadSetStatus"
    """<p>The read set's status.</p>"""
    name: NotRequired["capo_omics.types.read_set_name.ReadSetName"]
    """<p>The read set's name.</p>"""
    description: NotRequired["capo_omics.types.read_set_description.ReadSetDescription"]
    """<p>The read set's description.</p>"""
    reference_arn: NotRequired["capo_omics.types.reference_arn.ReferenceArn"]
    """<p>The read set's genome reference ARN.</p>"""
    file_type: "capo_omics.types.file_type.FileType"
    """<p>The read set's file type.</p>"""
    sequence_information: NotRequired[
        "capo_omics.types.sequence_information.SequenceInformation"
    ]
    creation_time: "datetime.datetime"
    """<p>When the read set was created.</p>"""
    status_message: NotRequired[
        "capo_omics.types.read_set_status_message.ReadSetStatusMessage"
    ]
    """<p> The status for a read set. It provides more detail as to why the read set has a status. </p>"""
    creation_type: NotRequired["capo_omics.types.creation_type.CreationType"]
    """<p> The creation type of the read set. </p>"""
    etag: NotRequired["capo_omics.types.e_tag.ETag"]
    """<p>The entity tag (ETag) is a hash of the object representing its semantic content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetListItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    if "subject_id" in value:
        out["subjectId"] = value["subject_id"]
    if "sample_id" in value:
        out["sampleId"] = value["sample_id"]
    out["status"] = value["status"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    out["fileType"] = value["file_type"]
    if "sequence_information" in value:
        import capo_omics.types.sequence_information

        out["sequenceInformation"] = (
            capo_omics.types.sequence_information.serialize_json(
                value["sequence_information"]
            )
        )
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_type" in value:
        out["creationType"] = value["creation_type"]
    if "etag" in value:
        import capo_omics.types.e_tag

        out["etag"] = capo_omics.types.e_tag.serialize_json(value["etag"])
    return out


def deserialize_json(data: dict) -> ReadSetListItem:
    out: ReadSetListItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("sequenceStoreId") is not None:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        out["sequence_store_id"] = ""
    if data.get("subjectId") is not None:
        out["subject_id"] = data["subjectId"]
    if data.get("sampleId") is not None:
        out["sample_id"] = data["sampleId"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("referenceArn") is not None:
        out["reference_arn"] = data["referenceArn"]
    if data.get("fileType") is not None:
        out["file_type"] = data["fileType"]
    else:
        out["file_type"] = ""
    if data.get("sequenceInformation") is not None:
        import capo_omics.types.sequence_information

        out["sequence_information"] = (
            capo_omics.types.sequence_information.deserialize_json(
                data["sequenceInformation"]
            )
        )
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
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("creationType") is not None:
        out["creation_type"] = data["creationType"]
    if data.get("etag") is not None:
        import capo_omics.types.e_tag

        out["etag"] = capo_omics.types.e_tag.deserialize_json(data["etag"])
    return out
