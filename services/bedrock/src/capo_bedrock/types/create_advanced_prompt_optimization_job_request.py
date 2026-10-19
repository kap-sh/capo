"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAdvancedPromptOptimizationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_input_config
    import capo_bedrock.types.advanced_prompt_optimization_job_description
    import capo_bedrock.types.advanced_prompt_optimization_job_name
    import capo_bedrock.types.advanced_prompt_optimization_output_config
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.model_configurations
    import capo_bedrock.types.tag_list


class CreateAdvancedPromptOptimizationJobRequest(TypedDict, closed=True):
    job_name: "capo_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName"
    """<p>A name for the advanced prompt optimization job.</p>"""
    job_description: NotRequired[
        "capo_bedrock.types.advanced_prompt_optimization_job_description.AdvancedPromptOptimizationJobDescription"
    ]
    """<p>A description of the advanced prompt optimization job.</p>"""
    client_token: NotRequired["capo_bedrock.types.idempotency_token.IdempotencyToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>"""
    input_config: "capo_bedrock.types.advanced_prompt_optimization_input_config.AdvancedPromptOptimizationInputConfig"
    """<p>Specifies the S3 location of your JSONL input file containing prompt templates and evaluation samples.</p>"""
    output_config: "capo_bedrock.types.advanced_prompt_optimization_output_config.AdvancedPromptOptimizationOutputConfig"
    """<p>Specifies the S3 location where optimization results will be stored.</p>"""
    encryption_key_arn: NotRequired["capo_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used for encrypting the output data. If not specified, the output is encrypted with an Amazon-owned KMS key.</p>"""
    tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>Tags to associate with the advanced prompt optimization job.</p>"""
    model_configurations: "capo_bedrock.types.model_configurations.ModelConfigurations"
    """<p>A list of model configurations specifying the target models for prompt optimization. You can specify up to 5 models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAdvancedPromptOptimizationJobRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    if "job_description" in value:
        out["jobDescription"] = value["job_description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
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
    if "tags" in value:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.serialize_json(value["tags"])
    import capo_bedrock.types.model_configurations

    out["modelConfigurations"] = capo_bedrock.types.model_configurations.serialize_json(
        value["model_configurations"]
    )
    return out


def deserialize_json(data: dict) -> CreateAdvancedPromptOptimizationJobRequest:
    out: CreateAdvancedPromptOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("jobDescription") is not None:
        out["job_description"] = data["jobDescription"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("inputConfig") is not None:
        import capo_bedrock.types.advanced_prompt_optimization_input_config

        out["input_config"] = (
            capo_bedrock.types.advanced_prompt_optimization_input_config.deserialize_json(
                data["inputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAdvancedPromptOptimizationJobRequest.input_config required"
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
            "CreateAdvancedPromptOptimizationJobRequest.output_config required"
        )
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if data.get("tags") is not None:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.deserialize_json(data["tags"])
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
