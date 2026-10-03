"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAutoMLJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_candidate
    import capo_sagemaker.types.auto_ml_failure_reason
    import capo_sagemaker.types.auto_ml_input_data_config
    import capo_sagemaker.types.auto_ml_job_arn
    import capo_sagemaker.types.auto_ml_job_artifacts
    import capo_sagemaker.types.auto_ml_job_config
    import capo_sagemaker.types.auto_ml_job_name
    import capo_sagemaker.types.auto_ml_job_objective
    import capo_sagemaker.types.auto_ml_job_secondary_status
    import capo_sagemaker.types.auto_ml_job_status
    import capo_sagemaker.types.auto_ml_output_data_config
    import capo_sagemaker.types.auto_ml_partial_failure_reasons
    import capo_sagemaker.types.generate_candidate_definitions_only
    import capo_sagemaker.types.model_deploy_config
    import capo_sagemaker.types.model_deploy_result
    import capo_sagemaker.types.problem_type
    import capo_sagemaker.types.resolved_attributes
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp


class DescribeAutoMLJobResponse(TypedDict, closed=True):
    auto_ml_job_name: NotRequired["capo_sagemaker.types.auto_ml_job_name.AutoMLJobName"]
    """<p>Returns the name of the AutoML job.</p>"""
    auto_ml_job_arn: NotRequired["capo_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>Returns the ARN of the AutoML job.</p>"""
    input_data_config: NotRequired[
        "capo_sagemaker.types.auto_ml_input_data_config.AutoMLInputDataConfig"
    ]
    """<p>Returns the input data configuration for the AutoML job.</p>"""
    output_data_config: NotRequired[
        "capo_sagemaker.types.auto_ml_output_data_config.AutoMLOutputDataConfig"
    ]
    """<p>Returns the job's output data config.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that has read permission to the input data location and write permission to the output data location in Amazon S3.</p>"""
    auto_ml_job_objective: NotRequired[
        "capo_sagemaker.types.auto_ml_job_objective.AutoMLJobObjective"
    ]
    """<p>Returns the job's objective.</p>"""
    problem_type: NotRequired["capo_sagemaker.types.problem_type.ProblemType"]
    """<p>Returns the job's problem type.</p>"""
    auto_ml_job_config: NotRequired[
        "capo_sagemaker.types.auto_ml_job_config.AutoMLJobConfig"
    ]
    """<p>Returns the configuration for the AutoML job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Returns the creation time of the AutoML job.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Returns the end time of the AutoML job.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Returns the job's last modified time.</p>"""
    failure_reason: NotRequired[
        "capo_sagemaker.types.auto_ml_failure_reason.AutoMLFailureReason"
    ]
    """<p>Returns the failure reason for an AutoML job, when applicable.</p>"""
    partial_failure_reasons: NotRequired[
        "capo_sagemaker.types.auto_ml_partial_failure_reasons.AutoMLPartialFailureReasons"
    ]
    """<p>Returns a list of reasons for partial failures within an AutoML job.</p>"""
    best_candidate: NotRequired[
        "capo_sagemaker.types.auto_ml_candidate.AutoMLCandidate"
    ]
    """<p>The best model candidate selected by SageMaker AI Autopilot using both the best objective metric and lowest <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html">InferenceLatency</a> for an experiment.</p>"""
    auto_ml_job_status: NotRequired[
        "capo_sagemaker.types.auto_ml_job_status.AutoMLJobStatus"
    ]
    """<p>Returns the status of the AutoML job.</p>"""
    auto_ml_job_secondary_status: NotRequired[
        "capo_sagemaker.types.auto_ml_job_secondary_status.AutoMLJobSecondaryStatus"
    ]
    """<p>Returns the secondary status of the AutoML job.</p>"""
    generate_candidate_definitions_only: NotRequired[
        "capo_sagemaker.types.generate_candidate_definitions_only.GenerateCandidateDefinitionsOnly"
    ]
    """<p>Indicates whether the output for an AutoML job generates candidate definitions only.</p>"""
    auto_ml_job_artifacts: NotRequired[
        "capo_sagemaker.types.auto_ml_job_artifacts.AutoMLJobArtifacts"
    ]
    """<p>Returns information on the job's artifacts found in <code>AutoMLJobArtifacts</code>.</p>"""
    resolved_attributes: NotRequired[
        "capo_sagemaker.types.resolved_attributes.ResolvedAttributes"
    ]
    """<p>Contains <code>ProblemType</code>, <code>AutoMLJobObjective</code>, and <code>CompletionCriteria</code>. If you do not provide these values, they are inferred.</p>"""
    model_deploy_config: NotRequired[
        "capo_sagemaker.types.model_deploy_config.ModelDeployConfig"
    ]
    """<p>Indicates whether the model was deployed automatically to an endpoint and the name of that endpoint if deployed automatically.</p>"""
    model_deploy_result: NotRequired[
        "capo_sagemaker.types.model_deploy_result.ModelDeployResult"
    ]
    """<p>Provides information about endpoint for the model deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutoMLJobResponse) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "input_data_config" in value:
        import capo_sagemaker.types.auto_ml_input_data_config

        out["InputDataConfig"] = (
            capo_sagemaker.types.auto_ml_input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_sagemaker.types.auto_ml_output_data_config

        out["OutputDataConfig"] = (
            capo_sagemaker.types.auto_ml_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "auto_ml_job_objective" in value:
        import capo_sagemaker.types.auto_ml_job_objective

        out["AutoMLJobObjective"] = (
            capo_sagemaker.types.auto_ml_job_objective.serialize_aws_json_1_1(
                value["auto_ml_job_objective"]
            )
        )
    if "problem_type" in value:
        import capo_sagemaker.types.problem_type

        out["ProblemType"] = capo_sagemaker.types.problem_type.serialize_aws_json_1_1(
            value["problem_type"]
        )
    if "auto_ml_job_config" in value:
        import capo_sagemaker.types.auto_ml_job_config

        out["AutoMLJobConfig"] = (
            capo_sagemaker.types.auto_ml_job_config.serialize_aws_json_1_1(
                value["auto_ml_job_config"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "partial_failure_reasons" in value:
        import capo_sagemaker.types.auto_ml_partial_failure_reasons

        out["PartialFailureReasons"] = (
            capo_sagemaker.types.auto_ml_partial_failure_reasons.serialize_aws_json_1_1(
                value["partial_failure_reasons"]
            )
        )
    if "best_candidate" in value:
        import capo_sagemaker.types.auto_ml_candidate

        out["BestCandidate"] = (
            capo_sagemaker.types.auto_ml_candidate.serialize_aws_json_1_1(
                value["best_candidate"]
            )
        )
    if "auto_ml_job_status" in value:
        import capo_sagemaker.types.auto_ml_job_status

        out["AutoMLJobStatus"] = (
            capo_sagemaker.types.auto_ml_job_status.serialize_aws_json_1_1(
                value["auto_ml_job_status"]
            )
        )
    if "auto_ml_job_secondary_status" in value:
        import capo_sagemaker.types.auto_ml_job_secondary_status

        out["AutoMLJobSecondaryStatus"] = (
            capo_sagemaker.types.auto_ml_job_secondary_status.serialize_aws_json_1_1(
                value["auto_ml_job_secondary_status"]
            )
        )
    if "generate_candidate_definitions_only" in value:
        out["GenerateCandidateDefinitionsOnly"] = value[
            "generate_candidate_definitions_only"
        ]
    if "auto_ml_job_artifacts" in value:
        import capo_sagemaker.types.auto_ml_job_artifacts

        out["AutoMLJobArtifacts"] = (
            capo_sagemaker.types.auto_ml_job_artifacts.serialize_aws_json_1_1(
                value["auto_ml_job_artifacts"]
            )
        )
    if "resolved_attributes" in value:
        import capo_sagemaker.types.resolved_attributes

        out["ResolvedAttributes"] = (
            capo_sagemaker.types.resolved_attributes.serialize_aws_json_1_1(
                value["resolved_attributes"]
            )
        )
    if "model_deploy_config" in value:
        import capo_sagemaker.types.model_deploy_config

        out["ModelDeployConfig"] = (
            capo_sagemaker.types.model_deploy_config.serialize_aws_json_1_1(
                value["model_deploy_config"]
            )
        )
    if "model_deploy_result" in value:
        import capo_sagemaker.types.model_deploy_result

        out["ModelDeployResult"] = (
            capo_sagemaker.types.model_deploy_result.serialize_aws_json_1_1(
                value["model_deploy_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutoMLJobResponse:
    out: DescribeAutoMLJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("AutoMLJobName") is not None:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    if data.get("AutoMLJobArn") is not None:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if data.get("InputDataConfig") is not None:
        import capo_sagemaker.types.auto_ml_input_data_config

        out["input_data_config"] = (
            capo_sagemaker.types.auto_ml_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_sagemaker.types.auto_ml_output_data_config

        out["output_data_config"] = (
            capo_sagemaker.types.auto_ml_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("AutoMLJobObjective") is not None:
        import capo_sagemaker.types.auto_ml_job_objective

        out["auto_ml_job_objective"] = (
            capo_sagemaker.types.auto_ml_job_objective.deserialize_aws_json_1_1(
                data["AutoMLJobObjective"]
            )
        )
    if data.get("ProblemType") is not None:
        import capo_sagemaker.types.problem_type

        out["problem_type"] = (
            capo_sagemaker.types.problem_type.deserialize_aws_json_1_1(
                data["ProblemType"]
            )
        )
    if data.get("AutoMLJobConfig") is not None:
        import capo_sagemaker.types.auto_ml_job_config

        out["auto_ml_job_config"] = (
            capo_sagemaker.types.auto_ml_job_config.deserialize_aws_json_1_1(
                data["AutoMLJobConfig"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("EndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("PartialFailureReasons") is not None:
        import capo_sagemaker.types.auto_ml_partial_failure_reasons

        out["partial_failure_reasons"] = (
            capo_sagemaker.types.auto_ml_partial_failure_reasons.deserialize_aws_json_1_1(
                data["PartialFailureReasons"]
            )
        )
    if data.get("BestCandidate") is not None:
        import capo_sagemaker.types.auto_ml_candidate

        out["best_candidate"] = (
            capo_sagemaker.types.auto_ml_candidate.deserialize_aws_json_1_1(
                data["BestCandidate"]
            )
        )
    if data.get("AutoMLJobStatus") is not None:
        import capo_sagemaker.types.auto_ml_job_status

        out["auto_ml_job_status"] = (
            capo_sagemaker.types.auto_ml_job_status.deserialize_aws_json_1_1(
                data["AutoMLJobStatus"]
            )
        )
    if data.get("AutoMLJobSecondaryStatus") is not None:
        import capo_sagemaker.types.auto_ml_job_secondary_status

        out["auto_ml_job_secondary_status"] = (
            capo_sagemaker.types.auto_ml_job_secondary_status.deserialize_aws_json_1_1(
                data["AutoMLJobSecondaryStatus"]
            )
        )
    if data.get("GenerateCandidateDefinitionsOnly") is not None:
        out["generate_candidate_definitions_only"] = data[
            "GenerateCandidateDefinitionsOnly"
        ]
    if data.get("AutoMLJobArtifacts") is not None:
        import capo_sagemaker.types.auto_ml_job_artifacts

        out["auto_ml_job_artifacts"] = (
            capo_sagemaker.types.auto_ml_job_artifacts.deserialize_aws_json_1_1(
                data["AutoMLJobArtifacts"]
            )
        )
    if data.get("ResolvedAttributes") is not None:
        import capo_sagemaker.types.resolved_attributes

        out["resolved_attributes"] = (
            capo_sagemaker.types.resolved_attributes.deserialize_aws_json_1_1(
                data["ResolvedAttributes"]
            )
        )
    if data.get("ModelDeployConfig") is not None:
        import capo_sagemaker.types.model_deploy_config

        out["model_deploy_config"] = (
            capo_sagemaker.types.model_deploy_config.deserialize_aws_json_1_1(
                data["ModelDeployConfig"]
            )
        )
    if data.get("ModelDeployResult") is not None:
        import capo_sagemaker.types.model_deploy_result

        out["model_deploy_result"] = (
            capo_sagemaker.types.model_deploy_result.deserialize_aws_json_1_1(
                data["ModelDeployResult"]
            )
        )
    return out
