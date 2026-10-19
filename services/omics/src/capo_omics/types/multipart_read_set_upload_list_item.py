"""Generated from Smithy shape ``com.amazonaws.omics#MultipartReadSetUploadListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.file_type
    import capo_omics.types.generated_from
    import capo_omics.types.read_set_description
    import capo_omics.types.read_set_name
    import capo_omics.types.reference_arn
    import capo_omics.types.sample_id
    import capo_omics.types.sequence_store_id
    import capo_omics.types.subject_id
    import capo_omics.types.tag_map
    import capo_omics.types.upload_id


class MultipartReadSetUploadListItem(TypedDict, closed=True):
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p> The sequence store ID used for the multipart upload. </p>"""
    upload_id: "capo_omics.types.upload_id.UploadId"
    """<p> The ID for the initiated multipart upload. </p>"""
    source_file_type: "capo_omics.types.file_type.FileType"
    """<p> The type of file the read set originated from. </p>"""
    subject_id: "capo_omics.types.subject_id.SubjectId"
    """<p> The read set source's subject ID. </p>"""
    sample_id: "capo_omics.types.sample_id.SampleId"
    """<p> The read set source's sample ID. </p>"""
    generated_from: "capo_omics.types.generated_from.GeneratedFrom"
    """<p> The source of an uploaded part. </p>"""
    reference_arn: "capo_omics.types.reference_arn.ReferenceArn"
    """<p> The source's reference ARN. </p>"""
    name: NotRequired["capo_omics.types.read_set_name.ReadSetName"]
    """<p> The name of a read set. </p>"""
    description: NotRequired["capo_omics.types.read_set_description.ReadSetDescription"]
    """<p> The description of a read set. </p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p> Any tags you wish to add to a read set. </p>"""
    creation_time: "datetime.datetime"
    """<p> The time stamp for when a direct upload was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultipartReadSetUploadListItem) -> dict:
    out: dict = {}
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["uploadId"] = value["upload_id"]
    out["sourceFileType"] = value["source_file_type"]
    out["subjectId"] = value["subject_id"]
    out["sampleId"] = value["sample_id"]
    out["generatedFrom"] = value["generated_from"]
    out["referenceArn"] = value["reference_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> MultipartReadSetUploadListItem:
    out: MultipartReadSetUploadListItem = {}  # type: ignore[typeddict-item]
    if data.get("sequenceStoreId") is not None:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        out["sequence_store_id"] = ""
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    if data.get("sourceFileType") is not None:
        out["source_file_type"] = data["sourceFileType"]
    else:
        out["source_file_type"] = ""
    if data.get("subjectId") is not None:
        out["subject_id"] = data["subjectId"]
    else:
        out["subject_id"] = ""
    if data.get("sampleId") is not None:
        out["sample_id"] = data["sampleId"]
    else:
        out["sample_id"] = ""
    if data.get("generatedFrom") is not None:
        out["generated_from"] = data["generatedFrom"]
    else:
        out["generated_from"] = ""
    if data.get("referenceArn") is not None:
        out["reference_arn"] = data["referenceArn"]
    else:
        out["reference_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
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
    return out
