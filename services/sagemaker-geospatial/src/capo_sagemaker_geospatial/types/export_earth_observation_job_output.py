"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportEarthObservationJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_sagemaker_geospatial.types.earth_observation_job_arn
    import capo_sagemaker_geospatial.types.earth_observation_job_export_status
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.output_config_input


class ExportEarthObservationJobOutput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    """<p>The output Amazon Resource Name (ARN) of the Earth Observation job being exported.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    export_status: "capo_sagemaker_geospatial.types.earth_observation_job_export_status.EarthObservationJobExportStatus"
    """<p>The status of the results of the Earth Observation job being exported.</p>"""
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
def serialize_json(value: ExportEarthObservationJobOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_sagemaker_geospatial._protocol.serialize

    out["CreationTime"] = capo_sagemaker_geospatial._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    out["ExportStatus"] = value["export_status"]
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


def deserialize_json(data: dict) -> ExportEarthObservationJobOutput:
    out: ExportEarthObservationJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
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
    if data.get("ExportStatus") is not None:
        out["export_status"] = data["ExportStatus"]
    else:
        out["export_status"] = ""
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
            "ExportEarthObservationJobOutput.output_config required"
        )
    if data.get("ExportSourceImages") is not None:
        out["export_source_images"] = data["ExportSourceImages"]
    return out
