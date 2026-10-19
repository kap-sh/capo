"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportEarthObservationJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.earth_observation_job_arn
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.output_config_input


class ExportEarthObservationJobInput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    """<p>The input Amazon Resource Name (ARN) of the Earth Observation job being exported.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""
    execution_role_arn: (
        "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>"""
    output_config: (
        "capo_sagemaker_geospatial.types.output_config_input.OutputConfigInput"
    )
    """<p>An object containing information about the output file.</p>"""
    export_source_images: NotRequired["bool"]
    """<p>The source images provided to the Earth Observation job being exported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportEarthObservationJobInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import capo_sagemaker_geospatial.types.output_config_input

    out["OutputConfig"] = (
        capo_sagemaker_geospatial.types.output_config_input.serialize_json(
            value["output_config"]
        )
    )
    if "export_source_images" in value:
        out["ExportSourceImages"] = value["export_source_images"]
    return out


def deserialize_json(data: dict) -> ExportEarthObservationJobInput:
    out: ExportEarthObservationJobInput = {}  # type: ignore[typeddict-item]
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
        import capo_sagemaker_geospatial.types.output_config_input

        out["output_config"] = (
            capo_sagemaker_geospatial.types.output_config_input.deserialize_json(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ExportEarthObservationJobInput.output_config required"
        )
    if data.get("ExportSourceImages") is not None:
        out["export_source_images"] = data["ExportSourceImages"]
    return out
