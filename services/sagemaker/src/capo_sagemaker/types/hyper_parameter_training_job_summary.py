"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTrainingJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.final_hyper_parameter_tuning_job_objective_metric
    import capo_sagemaker.types.hyper_parameter_training_job_definition_name
    import capo_sagemaker.types.hyper_parameter_tuning_job_name
    import capo_sagemaker.types.hyper_parameters
    import capo_sagemaker.types.objective_status
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_job_arn
    import capo_sagemaker.types.training_job_name
    import capo_sagemaker.types.training_job_status


class HyperParameterTrainingJobSummary(TypedDict, closed=True):
    training_job_definition_name: NotRequired[
        "capo_sagemaker.types.hyper_parameter_training_job_definition_name.HyperParameterTrainingJobDefinitionName"
    ]
    """<p>The training job definition name.</p>"""
    training_job_name: NotRequired[
        "capo_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of the training job.</p>"""
    training_job_arn: NotRequired[
        "capo_sagemaker.types.training_job_arn.TrainingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training job.</p>"""
    tuning_job_name: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_name.HyperParameterTuningJobName"
    ]
    """<p>The HyperParameter tuning job that launched the training job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the training job was created.</p>"""
    training_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the training job started.</p>"""
    training_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Specifies the time when the training job ends on training instances. You are billed for the time interval between the value of <code>TrainingStartTime</code> and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.</p>"""
    training_job_status: NotRequired[
        "capo_sagemaker.types.training_job_status.TrainingJobStatus"
    ]
    """<p>The status of the training job.</p>"""
    tuned_hyper_parameters: NotRequired[
        "capo_sagemaker.types.hyper_parameters.HyperParameters"
    ]
    """<p>A list of the hyperparameters for which you specified ranges to search.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>The reason that the training job failed. </p>"""
    final_hyper_parameter_tuning_job_objective_metric: NotRequired[
        "capo_sagemaker.types.final_hyper_parameter_tuning_job_objective_metric.FinalHyperParameterTuningJobObjectiveMetric"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalHyperParameterTuningJobObjectiveMetric.html">FinalHyperParameterTuningJobObjectiveMetric</a> object that specifies the value of the objective metric of the tuning job that launched this training job.</p>"""
    objective_status: NotRequired[
        "capo_sagemaker.types.objective_status.ObjectiveStatus"
    ]
    """<p>The status of the objective metric for the training job:</p> <ul> <li> <p>Succeeded: The final objective metric for the training job was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.</p> </li> </ul> <ul> <li> <p>Pending: The training job is in progress and evaluation of its final objective metric is pending.</p> </li> </ul> <ul> <li> <p>Failed: The final objective metric for the training job was not evaluated, and was not used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTrainingJobSummary) -> dict:
    out: dict = {}
    if "training_job_definition_name" in value:
        out["TrainingJobDefinitionName"] = value["training_job_definition_name"]
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
    if "training_job_arn" in value:
        out["TrainingJobArn"] = value["training_job_arn"]
    if "tuning_job_name" in value:
        out["TuningJobName"] = value["tuning_job_name"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "training_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["TrainingStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["training_start_time"]
            )
        )
    if "training_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["TrainingEndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["training_end_time"]
        )
    if "training_job_status" in value:
        import capo_sagemaker.types.training_job_status

        out["TrainingJobStatus"] = (
            capo_sagemaker.types.training_job_status.serialize_aws_json_1_1(
                value["training_job_status"]
            )
        )
    if "tuned_hyper_parameters" in value:
        import capo_sagemaker.types.hyper_parameters

        out["TunedHyperParameters"] = (
            capo_sagemaker.types.hyper_parameters.serialize_aws_json_1_1(
                value["tuned_hyper_parameters"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "final_hyper_parameter_tuning_job_objective_metric" in value:
        import capo_sagemaker.types.final_hyper_parameter_tuning_job_objective_metric

        out["FinalHyperParameterTuningJobObjectiveMetric"] = (
            capo_sagemaker.types.final_hyper_parameter_tuning_job_objective_metric.serialize_aws_json_1_1(
                value["final_hyper_parameter_tuning_job_objective_metric"]
            )
        )
    if "objective_status" in value:
        import capo_sagemaker.types.objective_status

        out["ObjectiveStatus"] = (
            capo_sagemaker.types.objective_status.serialize_aws_json_1_1(
                value["objective_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTrainingJobSummary:
    out: HyperParameterTrainingJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("TrainingJobDefinitionName") is not None:
        out["training_job_definition_name"] = data["TrainingJobDefinitionName"]
    if data.get("TrainingJobName") is not None:
        out["training_job_name"] = data["TrainingJobName"]
    if data.get("TrainingJobArn") is not None:
        out["training_job_arn"] = data["TrainingJobArn"]
    if data.get("TuningJobName") is not None:
        out["tuning_job_name"] = data["TuningJobName"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("TrainingStartTime") is not None:
        import capo_sagemaker.types.timestamp

        out["training_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingStartTime"]
            )
        )
    if data.get("TrainingEndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["training_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingEndTime"]
            )
        )
    if data.get("TrainingJobStatus") is not None:
        import capo_sagemaker.types.training_job_status

        out["training_job_status"] = (
            capo_sagemaker.types.training_job_status.deserialize_aws_json_1_1(
                data["TrainingJobStatus"]
            )
        )
    if data.get("TunedHyperParameters") is not None:
        import capo_sagemaker.types.hyper_parameters

        out["tuned_hyper_parameters"] = (
            capo_sagemaker.types.hyper_parameters.deserialize_aws_json_1_1(
                data["TunedHyperParameters"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("FinalHyperParameterTuningJobObjectiveMetric") is not None:
        import capo_sagemaker.types.final_hyper_parameter_tuning_job_objective_metric

        out["final_hyper_parameter_tuning_job_objective_metric"] = (
            capo_sagemaker.types.final_hyper_parameter_tuning_job_objective_metric.deserialize_aws_json_1_1(
                data["FinalHyperParameterTuningJobObjectiveMetric"]
            )
        )
    if data.get("ObjectiveStatus") is not None:
        import capo_sagemaker.types.objective_status

        out["objective_status"] = (
            capo_sagemaker.types.objective_status.deserialize_aws_json_1_1(
                data["ObjectiveStatus"]
            )
        )
    return out
