"""Generated from Smithy shape ``com.amazonaws.qconnect#ImportJobData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.arn
    import capo_qconnect.types.content_metadata
    import capo_qconnect.types.external_source_configuration
    import capo_qconnect.types.import_job_status
    import capo_qconnect.types.import_job_type
    import capo_qconnect.types.upload_id
    import capo_qconnect.types.url
    import capo_qconnect.types.uuid


class ImportJobData(TypedDict, closed=True):
    import_job_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the import job.</p>"""
    knowledge_base_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    upload_id: "capo_qconnect.types.upload_id.UploadId"
    """<p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>"""
    knowledge_base_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    import_job_type: "capo_qconnect.types.import_job_type.ImportJobType"
    """<p>The type of the import job.</p>"""
    status: "capo_qconnect.types.import_job_status.ImportJobStatus"
    """<p>The status of the import job.</p>"""
    url: "capo_qconnect.types.url.Url"
    """<p>The download link to the resource file that is uploaded to the import job.</p>"""
    failed_record_report: NotRequired["capo_qconnect.types.url.Url"]
    """<p>The link to download the information of resource data that failed to be imported.</p>"""
    url_expiry: "datetime.datetime"
    """<p>The expiration time of the URL as an epoch timestamp.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the import job was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the import job data was last modified.</p>"""
    metadata: NotRequired["capo_qconnect.types.content_metadata.ContentMetadata"]
    """<p>The metadata fields of the imported Amazon Q in Connect resources.</p>"""
    external_source_configuration: NotRequired[
        "capo_qconnect.types.external_source_configuration.ExternalSourceConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ImportJobData) -> dict:
    out: dict = {}
    out["importJobId"] = value["import_job_id"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["uploadId"] = value["upload_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["importJobType"] = value["import_job_type"]
    out["status"] = value["status"]
    out["url"] = value["url"]
    if "failed_record_report" in value:
        out["failedRecordReport"] = value["failed_record_report"]
    out["urlExpiry"] = value["url_expiry"].timestamp()
    out["createdTime"] = value["created_time"].timestamp()
    out["lastModifiedTime"] = value["last_modified_time"].timestamp()
    if "metadata" in value:
        import capo_qconnect.types.content_metadata

        out["metadata"] = capo_qconnect.types.content_metadata.serialize_json(
            value["metadata"]
        )
    if "external_source_configuration" in value:
        import capo_qconnect.types.external_source_configuration

        out["externalSourceConfiguration"] = (
            capo_qconnect.types.external_source_configuration.serialize_json(
                value["external_source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportJobData:
    out: ImportJobData = {}  # type: ignore[typeddict-item]
    if data.get("importJobId") is not None:
        out["import_job_id"] = data["importJobId"]
    else:
        raise DeserializationError("ImportJobData.import_job_id required")
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("ImportJobData.knowledge_base_id required")
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("ImportJobData.upload_id required")
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("ImportJobData.knowledge_base_arn required")
    if data.get("importJobType") is not None:
        out["import_job_type"] = data["importJobType"]
    else:
        raise DeserializationError("ImportJobData.import_job_type required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportJobData.status required")
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        raise DeserializationError("ImportJobData.url required")
    if data.get("failedRecordReport") is not None:
        out["failed_record_report"] = data["failedRecordReport"]
    if data.get("urlExpiry") is not None:
        import datetime

        out["url_expiry"] = datetime.datetime.fromtimestamp(
            float(data["urlExpiry"]), tz=datetime.timezone.utc
        )
    else:
        raise DeserializationError("ImportJobData.url_expiry required")
    if data.get("createdTime") is not None:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            float(data["createdTime"]), tz=datetime.timezone.utc
        )
    else:
        raise DeserializationError("ImportJobData.created_time required")
    if data.get("lastModifiedTime") is not None:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            float(data["lastModifiedTime"]), tz=datetime.timezone.utc
        )
    else:
        raise DeserializationError("ImportJobData.last_modified_time required")
    if data.get("metadata") is not None:
        import capo_qconnect.types.content_metadata

        out["metadata"] = capo_qconnect.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("externalSourceConfiguration") is not None:
        import capo_qconnect.types.external_source_configuration

        out["external_source_configuration"] = (
            capo_qconnect.types.external_source_configuration.deserialize_json(
                data["externalSourceConfiguration"]
            )
        )
    return out
