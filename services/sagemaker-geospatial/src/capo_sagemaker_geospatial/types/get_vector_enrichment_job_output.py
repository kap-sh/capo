"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetVectorEnrichmentJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.tags
    import capo_sagemaker_geospatial.types.vector_enrichment_job_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_error_details
    import capo_sagemaker_geospatial.types.vector_enrichment_job_export_error_details
    import capo_sagemaker_geospatial.types.vector_enrichment_job_export_status
    import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_status
    import capo_sagemaker_geospatial.types.vector_enrichment_job_type


class GetVectorEnrichmentJobOutput(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>"""
    type: "capo_sagemaker_geospatial.types.vector_enrichment_job_type.VectorEnrichmentJobType"
    """<p>The type of the Vector Enrichment job being initiated.</p>"""
    name: "str"
    """<p>The name of the Vector Enrichment job.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    duration_in_seconds: "int"
    """<p>The duration of the Vector Enrichment job, in seconds.</p>"""
    status: "capo_sagemaker_geospatial.types.vector_enrichment_job_status.VectorEnrichmentJobStatus"
    """<p>The status of the initiated Vector Enrichment job.</p>"""
    kms_key_id: NotRequired["capo_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""
    input_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.VectorEnrichmentJobInputConfig"
    """<p>Input configuration information for the Vector Enrichment job.</p>"""
    job_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_config.VectorEnrichmentJobConfig"
    """<p>An object containing information about the job configuration.</p>"""
    execution_role_arn: (
        "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>"""
    error_details: NotRequired[
        "capo_sagemaker_geospatial.types.vector_enrichment_job_error_details.VectorEnrichmentJobErrorDetails"
    ]
    """<p>Details about the errors generated during the Vector Enrichment job.</p>"""
    export_status: NotRequired[
        "capo_sagemaker_geospatial.types.vector_enrichment_job_export_status.VectorEnrichmentJobExportStatus"
    ]
    """<p>The export status of the Vector Enrichment job being initiated.</p>"""
    export_error_details: NotRequired[
        "capo_sagemaker_geospatial.types.vector_enrichment_job_export_error_details.VectorEnrichmentJobExportErrorDetails"
    ]
    """<p>Details about the errors generated during the ExportVectorEnrichmentJob.</p>"""
    tags: NotRequired["capo_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVectorEnrichmentJobOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Type"] = value["type"]
    out["Name"] = value["name"]
    import capo_sagemaker_geospatial._protocol.serialize

    out["CreationTime"] = capo_sagemaker_geospatial._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    out["DurationInSeconds"] = value["duration_in_seconds"]
    out["Status"] = value["status"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config

    out["InputConfig"] = (
        capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.serialize_json(
            value["input_config"]
        )
    )
    import capo_sagemaker_geospatial.types.vector_enrichment_job_config

    out["JobConfig"] = (
        capo_sagemaker_geospatial.types.vector_enrichment_job_config.serialize_json(
            value["job_config"]
        )
    )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "error_details" in value:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_error_details

        out["ErrorDetails"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_error_details.serialize_json(
                value["error_details"]
            )
        )
    if "export_status" in value:
        out["ExportStatus"] = value["export_status"]
    if "export_error_details" in value:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_export_error_details

        out["ExportErrorDetails"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_export_error_details.serialize_json(
                value["export_error_details"]
            )
        )
    if "tags" in value:
        import capo_sagemaker_geospatial.types.tags

        out["Tags"] = capo_sagemaker_geospatial.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetVectorEnrichmentJobOutput:
    out: GetVectorEnrichmentJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CreationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["CreationTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("DurationInSeconds") is not None:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        out["duration_in_seconds"] = 0
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("InputConfig") is not None:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config

        out["input_config"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError("GetVectorEnrichmentJobOutput.input_config required")
    if data.get("JobConfig") is not None:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_config

        out["job_config"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_config.deserialize_json(
                data["JobConfig"]
            )
        )
    else:
        import capo_sagemaker_geospatial.types._unknown

        out["job_config"] = capo_sagemaker_geospatial.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("ErrorDetails") is not None:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_error_details

        out["error_details"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_error_details.deserialize_json(
                data["ErrorDetails"]
            )
        )
    if data.get("ExportStatus") is not None:
        out["export_status"] = data["ExportStatus"]
    if data.get("ExportErrorDetails") is not None:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_export_error_details

        out["export_error_details"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_export_error_details.deserialize_json(
                data["ExportErrorDetails"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker_geospatial.types.tags

        out["tags"] = capo_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
