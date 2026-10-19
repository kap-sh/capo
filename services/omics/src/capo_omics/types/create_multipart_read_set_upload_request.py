"""Generated from Smithy shape ``com.amazonaws.omics#CreateMultipartReadSetUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.client_token
    import capo_omics.types.file_type
    import capo_omics.types.generated_from
    import capo_omics.types.read_set_description
    import capo_omics.types.read_set_name
    import capo_omics.types.reference_arn
    import capo_omics.types.sample_id
    import capo_omics.types.sequence_store_id
    import capo_omics.types.subject_id
    import capo_omics.types.tag_map


class CreateMultipartReadSetUploadRequest(TypedDict, closed=True):
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The sequence store ID for the store that is the destination of the multipart uploads.</p>"""
    client_token: NotRequired["capo_omics.types.client_token.ClientToken"]
    """<p>An idempotency token that can be used to avoid triggering multiple multipart uploads.</p>"""
    source_file_type: "capo_omics.types.file_type.FileType"
    """<p>The type of file being uploaded.</p>"""
    subject_id: "capo_omics.types.subject_id.SubjectId"
    """<p>The source's subject ID.</p>"""
    sample_id: "capo_omics.types.sample_id.SampleId"
    """<p>The source's sample ID.</p>"""
    generated_from: NotRequired["capo_omics.types.generated_from.GeneratedFrom"]
    """<p>Where the source originated.</p>"""
    reference_arn: NotRequired["capo_omics.types.reference_arn.ReferenceArn"]
    """<p>The ARN of the reference.</p>"""
    name: "capo_omics.types.read_set_name.ReadSetName"
    """<p>The name of the read set.</p>"""
    description: NotRequired["capo_omics.types.read_set_description.ReadSetDescription"]
    """<p>The description of the read set.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Any tags to add to the read set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultipartReadSetUploadRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["sourceFileType"] = value["source_file_type"]
    out["subjectId"] = value["subject_id"]
    out["sampleId"] = value["sample_id"]
    if "generated_from" in value:
        out["generatedFrom"] = value["generated_from"]
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMultipartReadSetUploadRequest:
    out: CreateMultipartReadSetUploadRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
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
    if data.get("referenceArn") is not None:
        out["reference_arn"] = data["referenceArn"]
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
