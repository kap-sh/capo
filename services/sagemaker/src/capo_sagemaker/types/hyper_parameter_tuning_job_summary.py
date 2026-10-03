"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_tuning_job_arn
    import capo_sagemaker.types.hyper_parameter_tuning_job_name
    import capo_sagemaker.types.hyper_parameter_tuning_job_status
    import capo_sagemaker.types.hyper_parameter_tuning_job_strategy_type
    import capo_sagemaker.types.objective_status_counters
    import capo_sagemaker.types.resource_limits
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_job_status_counters


class HyperParameterTuningJobSummary(TypedDict, closed=True):
    hyper_parameter_tuning_job_name: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_name.HyperParameterTuningJobName"
    ]
    """<p>The name of the tuning job.</p>"""
    hyper_parameter_tuning_job_arn: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_arn.HyperParameterTuningJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the tuning job.</p>"""
    hyper_parameter_tuning_job_status: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_status.HyperParameterTuningJobStatus"
    ]
    """<p>The status of the tuning job.</p>"""
    strategy: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_strategy_type.HyperParameterTuningJobStrategyType"
    ]
    """<p>Specifies the search strategy hyperparameter tuning uses to choose which hyperparameters to evaluate at each iteration.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the tuning job was created.</p>"""
    hyper_parameter_tuning_end_time: NotRequired[
        "capo_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the tuning job ended.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the tuning job was modified.</p>"""
    training_job_status_counters: NotRequired[
        "capo_sagemaker.types.training_job_status_counters.TrainingJobStatusCounters"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobStatusCounters.html">TrainingJobStatusCounters</a> object that specifies the numbers of training jobs, categorized by status, that this tuning job launched.</p>"""
    objective_status_counters: NotRequired[
        "capo_sagemaker.types.objective_status_counters.ObjectiveStatusCounters"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ObjectiveStatusCounters.html">ObjectiveStatusCounters</a> object that specifies the numbers of training jobs, categorized by objective metric status, that this tuning job launched.</p>"""
    resource_limits: NotRequired["capo_sagemaker.types.resource_limits.ResourceLimits"]
    """<p>The <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html">ResourceLimits</a> object that specifies the maximum number of training jobs and parallel training jobs allowed for this tuning job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobSummary) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_name" in value:
        out["HyperParameterTuningJobName"] = value["hyper_parameter_tuning_job_name"]
    if "hyper_parameter_tuning_job_arn" in value:
        out["HyperParameterTuningJobArn"] = value["hyper_parameter_tuning_job_arn"]
    if "hyper_parameter_tuning_job_status" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_status

        out["HyperParameterTuningJobStatus"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_status.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job_status"]
            )
        )
    if "strategy" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_strategy_type

        out["Strategy"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_strategy_type.serialize_aws_json_1_1(
                value["strategy"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "hyper_parameter_tuning_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["HyperParameterTuningEndTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_end_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "training_job_status_counters" in value:
        import capo_sagemaker.types.training_job_status_counters

        out["TrainingJobStatusCounters"] = (
            capo_sagemaker.types.training_job_status_counters.serialize_aws_json_1_1(
                value["training_job_status_counters"]
            )
        )
    if "objective_status_counters" in value:
        import capo_sagemaker.types.objective_status_counters

        out["ObjectiveStatusCounters"] = (
            capo_sagemaker.types.objective_status_counters.serialize_aws_json_1_1(
                value["objective_status_counters"]
            )
        )
    if "resource_limits" in value:
        import capo_sagemaker.types.resource_limits

        out["ResourceLimits"] = (
            capo_sagemaker.types.resource_limits.serialize_aws_json_1_1(
                value["resource_limits"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobSummary:
    out: HyperParameterTuningJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("HyperParameterTuningJobName") is not None:
        out["hyper_parameter_tuning_job_name"] = data["HyperParameterTuningJobName"]
    if data.get("HyperParameterTuningJobArn") is not None:
        out["hyper_parameter_tuning_job_arn"] = data["HyperParameterTuningJobArn"]
    if data.get("HyperParameterTuningJobStatus") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_status

        out["hyper_parameter_tuning_job_status"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_status.deserialize_aws_json_1_1(
                data["HyperParameterTuningJobStatus"]
            )
        )
    if data.get("Strategy") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_strategy_type

        out["strategy"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_strategy_type.deserialize_aws_json_1_1(
                data["Strategy"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("HyperParameterTuningEndTime") is not None:
        import capo_sagemaker.types.timestamp

        out["hyper_parameter_tuning_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["HyperParameterTuningEndTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("TrainingJobStatusCounters") is not None:
        import capo_sagemaker.types.training_job_status_counters

        out["training_job_status_counters"] = (
            capo_sagemaker.types.training_job_status_counters.deserialize_aws_json_1_1(
                data["TrainingJobStatusCounters"]
            )
        )
    if data.get("ObjectiveStatusCounters") is not None:
        import capo_sagemaker.types.objective_status_counters

        out["objective_status_counters"] = (
            capo_sagemaker.types.objective_status_counters.deserialize_aws_json_1_1(
                data["ObjectiveStatusCounters"]
            )
        )
    if data.get("ResourceLimits") is not None:
        import capo_sagemaker.types.resource_limits

        out["resource_limits"] = (
            capo_sagemaker.types.resource_limits.deserialize_aws_json_1_1(
                data["ResourceLimits"]
            )
        )
    return out
