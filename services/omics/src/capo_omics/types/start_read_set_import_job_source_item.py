"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetImportJobSourceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.file_type
    import capo_omics.types.generated_from
    import capo_omics.types.read_set_description
    import capo_omics.types.read_set_name
    import capo_omics.types.reference_arn
    import capo_omics.types.sample_id
    import capo_omics.types.source_files
    import capo_omics.types.subject_id
    import capo_omics.types.tag_map


class StartReadSetImportJobSourceItem(TypedDict, closed=True):
    source_files: "capo_omics.types.source_files.SourceFiles"
    """<p>The source files' location in Amazon S3.</p>"""
    source_file_type: "capo_omics.types.file_type.FileType"
    """<p>The source's file type.</p>"""
    subject_id: "capo_omics.types.subject_id.SubjectId"
    """<p>The source's subject ID.</p>"""
    sample_id: "capo_omics.types.sample_id.SampleId"
    """<p>The source's sample ID.</p>"""
    generated_from: NotRequired["capo_omics.types.generated_from.GeneratedFrom"]
    """<p>Where the source originated.</p>"""
    reference_arn: NotRequired["capo_omics.types.reference_arn.ReferenceArn"]
    """<p>The source's reference ARN.</p>"""
    name: NotRequired["capo_omics.types.read_set_name.ReadSetName"]
    """<p>The source's name.</p>"""
    description: NotRequired["capo_omics.types.read_set_description.ReadSetDescription"]
    """<p>The source's description.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>The source's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetImportJobSourceItem) -> dict:
    out: dict = {}
    import capo_omics.types.source_files

    out["sourceFiles"] = capo_omics.types.source_files.serialize_json(
        value["source_files"]
    )
    out["sourceFileType"] = value["source_file_type"]
    out["subjectId"] = value["subject_id"]
    out["sampleId"] = value["sample_id"]
    if "generated_from" in value:
        out["generatedFrom"] = value["generated_from"]
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartReadSetImportJobSourceItem:
    out: StartReadSetImportJobSourceItem = {}  # type: ignore[typeddict-item]
    if data.get("sourceFiles") is not None:
        import capo_omics.types.source_files

        out["source_files"] = capo_omics.types.source_files.deserialize_json(
            data["sourceFiles"]
        )
    else:
        raise DeserializationError(
            "StartReadSetImportJobSourceItem.source_files required"
        )
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
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    return out
