"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartPipelineExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.idempotency_token
    import capo_sagemaker.types.mlflow_experiment_entity_name
    import capo_sagemaker.types.parallelism_configuration
    import capo_sagemaker.types.parameter_list
    import capo_sagemaker.types.pipeline_execution_description
    import capo_sagemaker.types.pipeline_execution_name
    import capo_sagemaker.types.pipeline_name_or_arn
    import capo_sagemaker.types.pipeline_version_alias
    import capo_sagemaker.types.pipeline_version_id
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.selective_execution_config


class StartPipelineExecutionRequest(TypedDict, closed=True):
    pipeline_name: NotRequired[
        "capo_sagemaker.types.pipeline_name_or_arn.PipelineNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_execution_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_execution_name.PipelineExecutionName"
    ]
    """<p>The display name of the pipeline execution.</p>"""
    pipeline_parameters: NotRequired[
        "capo_sagemaker.types.parameter_list.ParameterList"
    ]
    """<p>Contains a list of pipeline parameters. This list can be empty. </p>"""
    pipeline_execution_description: NotRequired[
        "capo_sagemaker.types.pipeline_execution_description.PipelineExecutionDescription"
    ]
    """<p>The description of the pipeline execution.</p>"""
    client_request_token: NotRequired[
        "capo_sagemaker.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once.</p>"""
    parallelism_configuration: NotRequired[
        "capo_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>This configuration, if specified, overrides the parallelism configuration of the parent pipeline for this specific run.</p>"""
    selective_execution_config: NotRequired[
        "capo_sagemaker.types.selective_execution_config.SelectiveExecutionConfig"
    ]
    """<p>The selective execution configuration applied to the pipeline run.</p>"""
    pipeline_version_id: NotRequired[
        "capo_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The ID of the pipeline version to start execution from. You can't specify this with <code>PipelineVersionAlias</code>.</p>"""
    mlflow_experiment_name: NotRequired[
        "capo_sagemaker.types.mlflow_experiment_entity_name.MlflowExperimentEntityName"
    ]
    """<p> The MLflow experiment name of the pipeline execution. </p>"""
    pipeline_version_alias: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias.PipelineVersionAlias"
    ]
    """<p>The alias of the pipeline version to start the execution from. You can't specify this with <code>PipelineVersionId</code>. If no version of the pipeline has this alias, the request fails with a <code>ResourceNotFound</code> error.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the execution uses. You must specify this parameter when you start an execution of a pipeline that AWS manages. You can't specify it for a pipeline that you create, because its executions use the pipeline's role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartPipelineExecutionRequest) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_execution_display_name" in value:
        out["PipelineExecutionDisplayName"] = value["pipeline_execution_display_name"]
    if "pipeline_parameters" in value:
        import capo_sagemaker.types.parameter_list

        out["PipelineParameters"] = (
            capo_sagemaker.types.parameter_list.serialize_aws_json_1_1(
                value["pipeline_parameters"]
            )
        )
    if "pipeline_execution_description" in value:
        out["PipelineExecutionDescription"] = value["pipeline_execution_description"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
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
    if "mlflow_experiment_name" in value:
        out["MlflowExperimentName"] = value["mlflow_experiment_name"]
    if "pipeline_version_alias" in value:
        out["PipelineVersionAlias"] = value["pipeline_version_alias"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartPipelineExecutionRequest:
    out: StartPipelineExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineName") is not None:
        out["pipeline_name"] = data["PipelineName"]
    if data.get("PipelineExecutionDisplayName") is not None:
        out["pipeline_execution_display_name"] = data["PipelineExecutionDisplayName"]
    if data.get("PipelineParameters") is not None:
        import capo_sagemaker.types.parameter_list

        out["pipeline_parameters"] = (
            capo_sagemaker.types.parameter_list.deserialize_aws_json_1_1(
                data["PipelineParameters"]
            )
        )
    if data.get("PipelineExecutionDescription") is not None:
        out["pipeline_execution_description"] = data["PipelineExecutionDescription"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
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
    if data.get("MlflowExperimentName") is not None:
        out["mlflow_experiment_name"] = data["MlflowExperimentName"]
    if data.get("PipelineVersionAlias") is not None:
        out["pipeline_version_alias"] = data["PipelineVersionAlias"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
