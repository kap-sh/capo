"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StartVectorEnrichmentJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.tags
    import capo_sagemaker_geospatial.types.vector_enrichment_job_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config


class StartVectorEnrichmentJobInput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the Vector Enrichment job.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""
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
    tags: NotRequired["capo_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartVectorEnrichmentJobInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
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
    if "tags" in value:
        import capo_sagemaker_geospatial.types.tags

        out["Tags"] = capo_sagemaker_geospatial.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartVectorEnrichmentJobInput:
    out: StartVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
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
        raise DeserializationError(
            "StartVectorEnrichmentJobInput.input_config required"
        )
    if data.get("JobConfig") is not None:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_config

        out["job_config"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_config.deserialize_json(
                data["JobConfig"]
            )
        )
    else:
        out["job_config"] = {"$unknown": {"name": ""}}
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("Tags") is not None:
        import capo_sagemaker_geospatial.types.tags

        out["tags"] = capo_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
