"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAdvancedPromptOptimizationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_input_config
    import capo_bedrock.types.advanced_prompt_optimization_job_arn
    import capo_bedrock.types.advanced_prompt_optimization_job_description
    import capo_bedrock.types.advanced_prompt_optimization_job_name
    import capo_bedrock.types.advanced_prompt_optimization_job_status
    import capo_bedrock.types.advanced_prompt_optimization_output_config
    import capo_bedrock.types.error_message
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.model_configurations
    import capo_bedrock.types.timestamp


class GetAdvancedPromptOptimizationJobResponse(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.advanced_prompt_optimization_job_arn.AdvancedPromptOptimizationJobArn"
    """<p>The Amazon Resource Name (ARN) of the advanced prompt optimization job.</p>"""
    job_name: "capo_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName"
    """<p>The name of the advanced prompt optimization job.</p>"""
    job_description: NotRequired[
        "capo_bedrock.types.advanced_prompt_optimization_job_description.AdvancedPromptOptimizationJobDescription"
    ]
    """<p>The description of the advanced prompt optimization job.</p>"""
    job_status: "capo_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus"
    """<p>The status of the advanced prompt optimization job.</p>"""
    input_config: "capo_bedrock.types.advanced_prompt_optimization_input_config.AdvancedPromptOptimizationInputConfig"
    """<p>The input data configuration for the optimization job.</p>"""
    output_config: "capo_bedrock.types.advanced_prompt_optimization_output_config.AdvancedPromptOptimizationOutputConfig"
    """<p>The output data configuration for the optimization job.</p>"""
    encryption_key_arn: NotRequired["capo_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the output data.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The time at which the advanced prompt optimization job was created.</p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the advanced prompt optimization job was last modified.</p>"""
    failure_message: NotRequired["capo_bedrock.types.error_message.ErrorMessage"]
    """<p>If the job failed, a message describing the reason for the failure.</p>"""
    model_configurations: "capo_bedrock.types.model_configurations.ModelConfigurations"
    """<p>The model configurations used in the optimization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAdvancedPromptOptimizationJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    if "job_description" in value:
        out["jobDescription"] = value["job_description"]
    import capo_bedrock.types.advanced_prompt_optimization_job_status

    out["jobStatus"] = (
        capo_bedrock.types.advanced_prompt_optimization_job_status.serialize_json(
            value["job_status"]
        )
    )
    import capo_bedrock.types.advanced_prompt_optimization_input_config

    out["inputConfig"] = (
        capo_bedrock.types.advanced_prompt_optimization_input_config.serialize_json(
            value["input_config"]
        )
    )
    import capo_bedrock.types.advanced_prompt_optimization_output_config

    out["outputConfig"] = (
        capo_bedrock.types.advanced_prompt_optimization_output_config.serialize_json(
            value["output_config"]
        )
    )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    import capo_bedrock.types.model_configurations

    out["modelConfigurations"] = capo_bedrock.types.model_configurations.serialize_json(
        value["model_configurations"]
    )
    return out


def deserialize_json(data: dict) -> GetAdvancedPromptOptimizationJobResponse:
    out: GetAdvancedPromptOptimizationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("jobDescription") is not None:
        out["job_description"] = data["jobDescription"]
    if data.get("jobStatus") is not None:
        import capo_bedrock.types.advanced_prompt_optimization_job_status

        out["job_status"] = (
            capo_bedrock.types.advanced_prompt_optimization_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus",
            "",
        )
    if data.get("inputConfig") is not None:
        import capo_bedrock.types.advanced_prompt_optimization_input_config

        out["input_config"] = (
            capo_bedrock.types.advanced_prompt_optimization_input_config.deserialize_json(
                data["inputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.input_config required"
        )
    if data.get("outputConfig") is not None:
        import capo_bedrock.types.advanced_prompt_optimization_output_config

        out["output_config"] = (
            capo_bedrock.types.advanced_prompt_optimization_output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.output_config required"
        )
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("modelConfigurations") is not None:
        import capo_bedrock.types.model_configurations

        out["model_configurations"] = (
            capo_bedrock.types.model_configurations.deserialize_json(
                data["modelConfigurations"]
            )
        )
    else:
        out["model_configurations"] = []
    return out
