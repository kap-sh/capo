"""Generated from Smithy shape ``com.amazonaws.wisdom#ImportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_wisdom.types.arn
    import capo_wisdom.types.content_metadata
    import capo_wisdom.types.external_source_configuration
    import capo_wisdom.types.import_job_status
    import capo_wisdom.types.import_job_type
    import capo_wisdom.types.upload_id
    import capo_wisdom.types.uuid


class ImportJobSummary(TypedDict, closed=True):
    import_job_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the import job.</p>"""
    knowledge_base_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    upload_id: "capo_wisdom.types.upload_id.UploadId"
    """<p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>"""
    knowledge_base_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    import_job_type: "capo_wisdom.types.import_job_type.ImportJobType"
    """<p>The type of import job.</p>"""
    status: "capo_wisdom.types.import_job_status.ImportJobStatus"
    """<p>The status of the import job.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the import job was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the import job was last modified.</p>"""
    metadata: NotRequired["capo_wisdom.types.content_metadata.ContentMetadata"]
    """<p>The metadata fields of the imported Wisdom resources.</p>"""
    external_source_configuration: NotRequired[
        "capo_wisdom.types.external_source_configuration.ExternalSourceConfiguration"
    ]
    """<p>The configuration information of the external source that the resource data are imported from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportJobSummary) -> dict:
    out: dict = {}
    out["importJobId"] = value["import_job_id"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["uploadId"] = value["upload_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["importJobType"] = value["import_job_type"]
    out["status"] = value["status"]
    out["createdTime"] = value["created_time"].timestamp()
    out["lastModifiedTime"] = value["last_modified_time"].timestamp()
    if "metadata" in value:
        import capo_wisdom.types.content_metadata

        out["metadata"] = capo_wisdom.types.content_metadata.serialize_json(
            value["metadata"]
        )
    if "external_source_configuration" in value:
        import capo_wisdom.types.external_source_configuration

        out["externalSourceConfiguration"] = (
            capo_wisdom.types.external_source_configuration.serialize_json(
                value["external_source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportJobSummary:
    out: ImportJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("importJobId") is not None:
        out["import_job_id"] = data["importJobId"]
    else:
        raise DeserializationError("ImportJobSummary.import_job_id required")
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("ImportJobSummary.knowledge_base_id required")
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("ImportJobSummary.upload_id required")
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("ImportJobSummary.knowledge_base_arn required")
    if data.get("importJobType") is not None:
        out["import_job_type"] = data["importJobType"]
    else:
        raise DeserializationError("ImportJobSummary.import_job_type required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportJobSummary.status required")
    if data.get("createdTime") is not None:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            float(data["createdTime"]), tz=datetime.timezone.utc
        )
    else:
        raise DeserializationError("ImportJobSummary.created_time required")
    if data.get("lastModifiedTime") is not None:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            float(data["lastModifiedTime"]), tz=datetime.timezone.utc
        )
    else:
        raise DeserializationError("ImportJobSummary.last_modified_time required")
    if data.get("metadata") is not None:
        import capo_wisdom.types.content_metadata

        out["metadata"] = capo_wisdom.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("externalSourceConfiguration") is not None:
        import capo_wisdom.types.external_source_configuration

        out["external_source_configuration"] = (
            capo_wisdom.types.external_source_configuration.deserialize_json(
                data["externalSourceConfiguration"]
            )
        )
    return out
