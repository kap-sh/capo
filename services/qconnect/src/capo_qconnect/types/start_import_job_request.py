"""Generated from Smithy shape ``com.amazonaws.qconnect#StartImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.content_metadata
    import capo_qconnect.types.external_source_configuration
    import capo_qconnect.types.import_job_type
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.upload_id
    import capo_qconnect.types.uuid_or_arn


class StartImportJobRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p> <ul> <li> <p>For importing Amazon Q in Connect quick responses, this should be a <code>QUICK_RESPONSES</code> type knowledge base.</p> </li> </ul>"""
    import_job_type: "capo_qconnect.types.import_job_type.ImportJobType"
    """<p>The type of the import job.</p> <ul> <li> <p>For importing quick response resource, set the value to <code>QUICK_RESPONSES</code>.</p> </li> </ul>"""
    upload_id: "capo_qconnect.types.upload_id.UploadId"
    """<p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>"""
    client_token: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    metadata: NotRequired["capo_qconnect.types.content_metadata.ContentMetadata"]
    """<p>The metadata fields of the imported Amazon Q in Connect resources.</p>"""
    external_source_configuration: NotRequired[
        "capo_qconnect.types.external_source_configuration.ExternalSourceConfiguration"
    ]
    """<p>The configuration information of the external source that the resource data are imported from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportJobRequest) -> dict:
    out: dict = {}
    out["importJobType"] = value["import_job_type"]
    out["uploadId"] = value["upload_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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


def deserialize_json(data: dict) -> StartImportJobRequest:
    out: StartImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("importJobType") is not None:
        out["import_job_type"] = data["importJobType"]
    else:
        raise DeserializationError("StartImportJobRequest.import_job_type required")
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("StartImportJobRequest.upload_id required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
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
