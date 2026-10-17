"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrainingSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.lora_config
    import capo_sagemaker.types.model_package_group_arn
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.training_session_model_config
    import capo_sagemaker.types.training_session_name
    import capo_sagemaker.types.training_session_output_config
    import capo_sagemaker.types.vpc_config


class CreateTrainingSessionRequest(TypedDict, closed=True):
    training_session_name: NotRequired[
        "capo_sagemaker.types.training_session_name.TrainingSessionName"
    ]
    """<p>The name of the training session.</p>"""
    model_package_group_arn: NotRequired[
        "capo_sagemaker.types.model_package_group_arn.ModelPackageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package group where checkpoints and fine-tuned model artifacts are published.</p>"""
    lora_config: NotRequired["capo_sagemaker.types.lora_config.LoraConfig"]
    """<p>The Low-Rank Adaptation (LoRA) configuration for the training session, including the rank and alpha parameters.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker assumes to access resources on your behalf. The role must have permissions to access the output S3 path and model package group.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    """<p>The Virtual Private Cloud (VPC) configuration for the training session. Specify subnets and security groups to run the training session in your VPC.</p>"""
    model_config: NotRequired[
        "capo_sagemaker.types.training_session_model_config.TrainingSessionModelConfig"
    ]
    """<p>The configuration for the base model, including the model ARN and end-user license agreement (EULA) acceptance.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.training_session_output_config.TrainingSessionOutputConfig"
    ]
    """<p>The output configuration for the training session, including the S3 location and optional encryption settings.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply to the training session as tags. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrainingSessionRequest) -> dict:
    out: dict = {}
    if "training_session_name" in value:
        out["TrainingSessionName"] = value["training_session_name"]
    if "model_package_group_arn" in value:
        out["ModelPackageGroupArn"] = value["model_package_group_arn"]
    if "lora_config" in value:
        import capo_sagemaker.types.lora_config

        out["LoraConfig"] = capo_sagemaker.types.lora_config.serialize_aws_json_1_1(
            value["lora_config"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "model_config" in value:
        import capo_sagemaker.types.training_session_model_config

        out["ModelConfig"] = (
            capo_sagemaker.types.training_session_model_config.serialize_aws_json_1_1(
                value["model_config"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.training_session_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.training_session_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrainingSessionRequest:
    out: CreateTrainingSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrainingSessionName") is not None:
        out["training_session_name"] = data["TrainingSessionName"]
    if data.get("ModelPackageGroupArn") is not None:
        out["model_package_group_arn"] = data["ModelPackageGroupArn"]
    if data.get("LoraConfig") is not None:
        import capo_sagemaker.types.lora_config

        out["lora_config"] = capo_sagemaker.types.lora_config.deserialize_aws_json_1_1(
            data["LoraConfig"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("ModelConfig") is not None:
        import capo_sagemaker.types.training_session_model_config

        out["model_config"] = (
            capo_sagemaker.types.training_session_model_config.deserialize_aws_json_1_1(
                data["ModelConfig"]
            )
        )
    if data.get("OutputConfig") is not None:
        import capo_sagemaker.types.training_session_output_config

        out["output_config"] = (
            capo_sagemaker.types.training_session_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
