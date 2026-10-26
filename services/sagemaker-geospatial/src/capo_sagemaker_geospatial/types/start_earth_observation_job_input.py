"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StartEarthObservationJobInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.input_config_input
    import capo_sagemaker_geospatial.types.job_config_input
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.tags


class StartEarthObservationJobInput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the Earth Observation job.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""
    kms_key_id: NotRequired["capo_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""
    input_config: "capo_sagemaker_geospatial.types.input_config_input.InputConfigInput"
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
def serialize_json(value: StartEarthObservationJobInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    import capo_sagemaker_geospatial.types.input_config_input

    out["InputConfig"] = (
        capo_sagemaker_geospatial.types.input_config_input.serialize_json(
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


def deserialize_json(data: dict) -> StartEarthObservationJobInput:
    out: StartEarthObservationJobInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("InputConfig") is not None:
        import capo_sagemaker_geospatial.types.input_config_input

        out["input_config"] = (
            capo_sagemaker_geospatial.types.input_config_input.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartEarthObservationJobInput.input_config required"
        )
    if data.get("JobConfig") is not None:
        import capo_sagemaker_geospatial.types.job_config_input

        out["job_config"] = (
            capo_sagemaker_geospatial.types.job_config_input.deserialize_json(
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


def redact_sensitive(value: StartEarthObservationJobInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_config" in value:
        import capo_sagemaker_geospatial.types.input_config_input

        out["input_config"] = (
            capo_sagemaker_geospatial.types.input_config_input.redact_sensitive(
                value["input_config"]
            )
        )
    return out
