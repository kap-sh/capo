"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportVectorEnrichmentJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_arn


class ExportVectorEnrichmentJobInput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn"
    """<p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""
    execution_role_arn: (
        "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM rolewith permission to upload to the location in OutputConfig.</p>"""
    output_config: "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.ExportVectorEnrichmentJobOutputConfig"
    """<p>Output location information for exporting Vector Enrichment Job results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportVectorEnrichmentJobInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config

    out["OutputConfig"] = (
        capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.serialize_json(
            value["output_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExportVectorEnrichmentJobInput:
    out: ExportVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("OutputConfig") is not None:
        import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config

        out["output_config"] = (
            capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.deserialize_json(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ExportVectorEnrichmentJobInput.output_config required"
        )
    return out
