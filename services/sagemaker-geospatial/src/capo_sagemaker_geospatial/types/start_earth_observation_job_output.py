"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StartEarthObservationJobOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_sagemaker_geospatial.types.earth_observation_job_status
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.input_config_output
    import capo_sagemaker_geospatial.types.job_config_input
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.tags


class StartEarthObservationJobOutput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the Earth Observation job.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    duration_in_seconds: "int"
    """<p>The duration of the session, in seconds.</p>"""
    status: "capo_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
    """<p>The status of the Earth Observation job.</p>"""
    kms_key_id: NotRequired["capo_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""
    input_config: NotRequired[
        "capo_sagemaker_geospatial.types.input_config_output.InputConfigOutput"
    ]
    """<p>Input configuration information for the Earth Observation job.</p>"""
    job_config: "capo_sagemaker_geospatial.types.job_config_input.JobConfigInput"
    """<p>An object containing information about the job configuration.</p>"""
    execution_role_arn: (
        "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>"""
    tags: NotRequired["capo_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartEarthObservationJobOutput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    import capo_sagemaker_geospatial._protocol.serialize

    out["CreationTime"] = capo_sagemaker_geospatial._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    out["DurationInSeconds"] = value["duration_in_seconds"]
    out["Status"] = value["status"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "input_config" in value:
        import capo_sagemaker_geospatial.types.input_config_output

        out["InputConfig"] = (
            capo_sagemaker_geospatial.types.input_config_output.serialize_json(
                value["input_config"]
            )
        )
    import capo_sagemaker_geospatial.types.job_config_input

    out["JobConfig"] = capo_sagemaker_geospatial.types.job_config_input.serialize_json(
        value["job_config"]
    )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "tags" in value:
        import capo_sagemaker_geospatial.types.tags

        out["Tags"] = capo_sagemaker_geospatial.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartEarthObservationJobOutput:
    out: StartEarthObservationJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartEarthObservationJobOutput.name required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("StartEarthObservationJobOutput.arn required")
    if data.get("CreationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["CreationTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "StartEarthObservationJobOutput.creation_time required"
        )
    if data.get("DurationInSeconds") is not None:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        raise DeserializationError(
            "StartEarthObservationJobOutput.duration_in_seconds required"
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("StartEarthObservationJobOutput.status required")
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("InputConfig") is not None:
        import capo_sagemaker_geospatial.types.input_config_output

        out["input_config"] = (
            capo_sagemaker_geospatial.types.input_config_output.deserialize_json(
                data["InputConfig"]
            )
        )
    if data.get("JobConfig") is not None:
        import capo_sagemaker_geospatial.types.job_config_input

        out["job_config"] = (
            capo_sagemaker_geospatial.types.job_config_input.deserialize_json(
                data["JobConfig"]
            )
        )
    else:
        raise DeserializationError("StartEarthObservationJobOutput.job_config required")
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError(
            "StartEarthObservationJobOutput.execution_role_arn required"
        )
    if data.get("Tags") is not None:
        import capo_sagemaker_geospatial.types.tags

        out["tags"] = capo_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: StartEarthObservationJobOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_config" in value:
        import capo_sagemaker_geospatial.types.input_config_output

        out["input_config"] = (
            capo_sagemaker_geospatial.types.input_config_output.redact_sensitive(
                value["input_config"]
            )
        )
    return out
