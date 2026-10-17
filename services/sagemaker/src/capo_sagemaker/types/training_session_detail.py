"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingSessionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.billable_token_usage
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.java_integer
    import capo_sagemaker.types.lora_config
    import capo_sagemaker.types.model_package_group_arn
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_session_arn
    import capo_sagemaker.types.training_session_model_config
    import capo_sagemaker.types.training_session_name
    import capo_sagemaker.types.training_session_output_config
    import capo_sagemaker.types.training_session_status
    import capo_sagemaker.types.vpc_config


class TrainingSessionDetail(TypedDict, closed=True):
    training_session_arn: NotRequired[
        "capo_sagemaker.types.training_session_arn.TrainingSessionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training session.</p>"""
    training_session_name: NotRequired[
        "capo_sagemaker.types.training_session_name.TrainingSessionName"
    ]
    """<p>The name of the training session.</p>"""
    training_session_status: NotRequired[
        "capo_sagemaker.types.training_session_status.TrainingSessionStatus"
    ]
    """<p>The current status of the training session.</p>"""
    model_package_group_arn: NotRequired[
        "capo_sagemaker.types.model_package_group_arn.ModelPackageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package group where checkpoints are published.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the training session was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the training session was last modified.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the training session ended.</p>"""
    error_details: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the training session failed or is blocked, detailed error information.</p>"""
    last_received_sequence_number: NotRequired[
        "capo_sagemaker.types.java_integer.JavaInteger"
    ]
    """<p>The sequence number of the last training operation received by the session.</p>"""
    billable_token_usage: NotRequired[
        "capo_sagemaker.types.billable_token_usage.BillableTokenUsage"
    ]
    """<p>The billable token usage for the training session.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    """<p>The Virtual Private Cloud (VPC) configuration for the training session.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the training session.</p>"""
    lora_config: NotRequired["capo_sagemaker.types.lora_config.LoraConfig"]
    """<p>The Low-Rank Adaptation (LoRA) configuration for the training session.</p>"""
    model_config: NotRequired[
        "capo_sagemaker.types.training_session_model_config.TrainingSessionModelConfig"
    ]
    """<p>The configuration for the base model.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.training_session_output_config.TrainingSessionOutputConfig"
    ]
    """<p>The output configuration for the training session.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The tags associated with the training session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingSessionDetail) -> dict:
    out: dict = {}
    if "training_session_arn" in value:
        out["TrainingSessionArn"] = value["training_session_arn"]
    if "training_session_name" in value:
        out["TrainingSessionName"] = value["training_session_name"]
    if "training_session_status" in value:
        import capo_sagemaker.types.training_session_status

        out["TrainingSessionStatus"] = (
            capo_sagemaker.types.training_session_status.serialize_aws_json_1_1(
                value["training_session_status"]
            )
        )
    if "model_package_group_arn" in value:
        out["ModelPackageGroupArn"] = value["model_package_group_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "error_details" in value:
        out["ErrorDetails"] = value["error_details"]
    if "last_received_sequence_number" in value:
        out["LastReceivedSequenceNumber"] = value["last_received_sequence_number"]
    if "billable_token_usage" in value:
        import capo_sagemaker.types.billable_token_usage

        out["BillableTokenUsage"] = (
            capo_sagemaker.types.billable_token_usage.serialize_aws_json_1_1(
                value["billable_token_usage"]
            )
        )
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "lora_config" in value:
        import capo_sagemaker.types.lora_config

        out["LoraConfig"] = capo_sagemaker.types.lora_config.serialize_aws_json_1_1(
            value["lora_config"]
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


def deserialize_aws_json_1_1(data: dict) -> TrainingSessionDetail:
    out: TrainingSessionDetail = {}  # type: ignore[typeddict-item]
    if data.get("TrainingSessionArn") is not None:
        out["training_session_arn"] = data["TrainingSessionArn"]
    if data.get("TrainingSessionName") is not None:
        out["training_session_name"] = data["TrainingSessionName"]
    if data.get("TrainingSessionStatus") is not None:
        import capo_sagemaker.types.training_session_status

        out["training_session_status"] = (
            capo_sagemaker.types.training_session_status.deserialize_aws_json_1_1(
                data["TrainingSessionStatus"]
            )
        )
    if data.get("ModelPackageGroupArn") is not None:
        out["model_package_group_arn"] = data["ModelPackageGroupArn"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("ErrorDetails") is not None:
        out["error_details"] = data["ErrorDetails"]
    if data.get("LastReceivedSequenceNumber") is not None:
        out["last_received_sequence_number"] = data["LastReceivedSequenceNumber"]
    if data.get("BillableTokenUsage") is not None:
        import capo_sagemaker.types.billable_token_usage

        out["billable_token_usage"] = (
            capo_sagemaker.types.billable_token_usage.deserialize_aws_json_1_1(
                data["BillableTokenUsage"]
            )
        )
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("LoraConfig") is not None:
        import capo_sagemaker.types.lora_config

        out["lora_config"] = capo_sagemaker.types.lora_config.deserialize_aws_json_1_1(
            data["LoraConfig"]
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
