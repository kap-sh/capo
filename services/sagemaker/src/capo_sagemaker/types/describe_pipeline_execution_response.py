"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePipelineExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.m_lflow_configuration
    import capo_sagemaker.types.parallelism_configuration
    import capo_sagemaker.types.pipeline_arn
    import capo_sagemaker.types.pipeline_execution_arn
    import capo_sagemaker.types.pipeline_execution_description
    import capo_sagemaker.types.pipeline_execution_failure_reason
    import capo_sagemaker.types.pipeline_execution_name
    import capo_sagemaker.types.pipeline_execution_status
    import capo_sagemaker.types.pipeline_experiment_config
    import capo_sagemaker.types.pipeline_version_alias_list
    import capo_sagemaker.types.pipeline_version_id
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.selective_execution_config
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class DescribePipelineExecutionResponse(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_execution_arn: NotRequired[
        "capo_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline execution.</p>"""
    pipeline_execution_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_execution_name.PipelineExecutionName"
    ]
    """<p>The display name of the pipeline execution.</p>"""
    pipeline_execution_status: NotRequired[
        "capo_sagemaker.types.pipeline_execution_status.PipelineExecutionStatus"
    ]
    """<p>The status of the pipeline execution.</p>"""
    pipeline_execution_description: NotRequired[
        "capo_sagemaker.types.pipeline_execution_description.PipelineExecutionDescription"
    ]
    """<p>The description of the pipeline execution.</p>"""
    pipeline_experiment_config: NotRequired[
        "capo_sagemaker.types.pipeline_experiment_config.PipelineExperimentConfig"
    ]
    failure_reason: NotRequired[
        "capo_sagemaker.types.pipeline_execution_failure_reason.PipelineExecutionFailureReason"
    ]
    """<p>If the execution failed, a message describing why.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline execution was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline execution was modified last.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    parallelism_configuration: NotRequired[
        "capo_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>The parallelism configuration applied to the pipeline.</p>"""
    selective_execution_config: NotRequired[
        "capo_sagemaker.types.selective_execution_config.SelectiveExecutionConfig"
    ]
    """<p>The selective execution configuration applied to the pipeline run.</p>"""
    pipeline_version_id: NotRequired[
        "capo_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The ID of the pipeline version.</p>"""
    m_lflow_config: NotRequired[
        "capo_sagemaker.types.m_lflow_configuration.MLflowConfiguration"
    ]
    """<p> The MLflow configuration of the pipeline execution. </p>"""
    pipeline_version_aliases: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias_list.PipelineVersionAliasList"
    ]
    """<p>The aliases currently assigned to the pipeline version that the execution ran.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the execution uses. SageMaker returns this value only for executions of pipelines that AWS manages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelineExecutionResponse) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_execution_arn" in value:
        out["PipelineExecutionArn"] = value["pipeline_execution_arn"]
    if "pipeline_execution_display_name" in value:
        out["PipelineExecutionDisplayName"] = value["pipeline_execution_display_name"]
    if "pipeline_execution_status" in value:
        import capo_sagemaker.types.pipeline_execution_status

        out["PipelineExecutionStatus"] = (
            capo_sagemaker.types.pipeline_execution_status.serialize_aws_json_1_1(
                value["pipeline_execution_status"]
            )
        )
    if "pipeline_execution_description" in value:
        out["PipelineExecutionDescription"] = value["pipeline_execution_description"]
    if "pipeline_experiment_config" in value:
        import capo_sagemaker.types.pipeline_experiment_config

        out["PipelineExperimentConfig"] = (
            capo_sagemaker.types.pipeline_experiment_config.serialize_aws_json_1_1(
                value["pipeline_experiment_config"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
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
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "parallelism_configuration" in value:
        import capo_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            capo_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    if "selective_execution_config" in value:
        import capo_sagemaker.types.selective_execution_config

        out["SelectiveExecutionConfig"] = (
            capo_sagemaker.types.selective_execution_config.serialize_aws_json_1_1(
                value["selective_execution_config"]
            )
        )
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    if "m_lflow_config" in value:
        import capo_sagemaker.types.m_lflow_configuration

        out["MLflowConfig"] = (
            capo_sagemaker.types.m_lflow_configuration.serialize_aws_json_1_1(
                value["m_lflow_config"]
            )
        )
    if "pipeline_version_aliases" in value:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["PipelineVersionAliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.serialize_aws_json_1_1(
                value["pipeline_version_aliases"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelineExecutionResponse:
    out: DescribePipelineExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("PipelineArn") is not None:
        out["pipeline_arn"] = data["PipelineArn"]
    if data.get("PipelineExecutionArn") is not None:
        out["pipeline_execution_arn"] = data["PipelineExecutionArn"]
    if data.get("PipelineExecutionDisplayName") is not None:
        out["pipeline_execution_display_name"] = data["PipelineExecutionDisplayName"]
    if data.get("PipelineExecutionStatus") is not None:
        import capo_sagemaker.types.pipeline_execution_status

        out["pipeline_execution_status"] = (
            capo_sagemaker.types.pipeline_execution_status.deserialize_aws_json_1_1(
                data["PipelineExecutionStatus"]
            )
        )
    if data.get("PipelineExecutionDescription") is not None:
        out["pipeline_execution_description"] = data["PipelineExecutionDescription"]
    if data.get("PipelineExperimentConfig") is not None:
        import capo_sagemaker.types.pipeline_experiment_config

        out["pipeline_experiment_config"] = (
            capo_sagemaker.types.pipeline_experiment_config.deserialize_aws_json_1_1(
                data["PipelineExperimentConfig"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
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
    if data.get("CreatedBy") is not None:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if data.get("LastModifiedBy") is not None:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if data.get("ParallelismConfiguration") is not None:
        import capo_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            capo_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    if data.get("SelectiveExecutionConfig") is not None:
        import capo_sagemaker.types.selective_execution_config

        out["selective_execution_config"] = (
            capo_sagemaker.types.selective_execution_config.deserialize_aws_json_1_1(
                data["SelectiveExecutionConfig"]
            )
        )
    if data.get("PipelineVersionId") is not None:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    if data.get("MLflowConfig") is not None:
        import capo_sagemaker.types.m_lflow_configuration

        out["m_lflow_config"] = (
            capo_sagemaker.types.m_lflow_configuration.deserialize_aws_json_1_1(
                data["MLflowConfig"]
            )
        )
    if data.get("PipelineVersionAliases") is not None:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["pipeline_version_aliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.deserialize_aws_json_1_1(
                data["PipelineVersionAliases"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
