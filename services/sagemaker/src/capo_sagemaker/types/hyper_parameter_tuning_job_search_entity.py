"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobSearchEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.hyper_parameter_training_job_definition
    import capo_sagemaker.types.hyper_parameter_training_job_definitions
    import capo_sagemaker.types.hyper_parameter_training_job_summary
    import capo_sagemaker.types.hyper_parameter_tuning_job_arn
    import capo_sagemaker.types.hyper_parameter_tuning_job_completion_details
    import capo_sagemaker.types.hyper_parameter_tuning_job_config
    import capo_sagemaker.types.hyper_parameter_tuning_job_consumed_resources
    import capo_sagemaker.types.hyper_parameter_tuning_job_name
    import capo_sagemaker.types.hyper_parameter_tuning_job_status
    import capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_config
    import capo_sagemaker.types.objective_status_counters
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_job_status_counters


class HyperParameterTuningJobSearchEntity(TypedDict, closed=True):
    hyper_parameter_tuning_job_name: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_name.HyperParameterTuningJobName"
    ]
    """<p>The name of a hyperparameter tuning job.</p>"""
    hyper_parameter_tuning_job_arn: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_arn.HyperParameterTuningJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a hyperparameter tuning job.</p>"""
    hyper_parameter_tuning_job_config: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_config.HyperParameterTuningJobConfig"
    ]
    training_job_definition: NotRequired[
        "capo_sagemaker.types.hyper_parameter_training_job_definition.HyperParameterTrainingJobDefinition"
    ]
    training_job_definitions: NotRequired[
        "capo_sagemaker.types.hyper_parameter_training_job_definitions.HyperParameterTrainingJobDefinitions"
    ]
    """<p>The job definitions included in a hyperparameter tuning job.</p>"""
    hyper_parameter_tuning_job_status: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_status.HyperParameterTuningJobStatus"
    ]
    """<p>The status of a hyperparameter tuning job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that a hyperparameter tuning job was created.</p>"""
    hyper_parameter_tuning_end_time: NotRequired[
        "capo_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>The time that a hyperparameter tuning job ended.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that a hyperparameter tuning job was last modified.</p>"""
    training_job_status_counters: NotRequired[
        "capo_sagemaker.types.training_job_status_counters.TrainingJobStatusCounters"
    ]
    objective_status_counters: NotRequired[
        "capo_sagemaker.types.objective_status_counters.ObjectiveStatusCounters"
    ]
    best_training_job: NotRequired[
        "capo_sagemaker.types.hyper_parameter_training_job_summary.HyperParameterTrainingJobSummary"
    ]
    overall_best_training_job: NotRequired[
        "capo_sagemaker.types.hyper_parameter_training_job_summary.HyperParameterTrainingJobSummary"
    ]
    warm_start_config: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.HyperParameterTuningJobWarmStartConfig"
    ]
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>The error that was created when a hyperparameter tuning job failed.</p>"""
    tuning_job_completion_details: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_completion_details.HyperParameterTuningJobCompletionDetails"
    ]
    """<p>Information about either a current or completed hyperparameter tuning job.</p>"""
    consumed_resources: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_consumed_resources.HyperParameterTuningJobConsumedResources"
    ]
    """<p>The total amount of resources consumed by a hyperparameter tuning job.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>The tags associated with a hyperparameter tuning job. For more information see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobSearchEntity) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_name" in value:
        out["HyperParameterTuningJobName"] = value["hyper_parameter_tuning_job_name"]
    if "hyper_parameter_tuning_job_arn" in value:
        out["HyperParameterTuningJobArn"] = value["hyper_parameter_tuning_job_arn"]
    if "hyper_parameter_tuning_job_config" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_config

        out["HyperParameterTuningJobConfig"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_config.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job_config"]
            )
        )
    if "training_job_definition" in value:
        import capo_sagemaker.types.hyper_parameter_training_job_definition

        out["TrainingJobDefinition"] = (
            capo_sagemaker.types.hyper_parameter_training_job_definition.serialize_aws_json_1_1(
                value["training_job_definition"]
            )
        )
    if "training_job_definitions" in value:
        import capo_sagemaker.types.hyper_parameter_training_job_definitions

        out["TrainingJobDefinitions"] = (
            capo_sagemaker.types.hyper_parameter_training_job_definitions.serialize_aws_json_1_1(
                value["training_job_definitions"]
            )
        )
    if "hyper_parameter_tuning_job_status" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_status

        out["HyperParameterTuningJobStatus"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_status.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job_status"]
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
    if "best_training_job" in value:
        import capo_sagemaker.types.hyper_parameter_training_job_summary

        out["BestTrainingJob"] = (
            capo_sagemaker.types.hyper_parameter_training_job_summary.serialize_aws_json_1_1(
                value["best_training_job"]
            )
        )
    if "overall_best_training_job" in value:
        import capo_sagemaker.types.hyper_parameter_training_job_summary

        out["OverallBestTrainingJob"] = (
            capo_sagemaker.types.hyper_parameter_training_job_summary.serialize_aws_json_1_1(
                value["overall_best_training_job"]
            )
        )
    if "warm_start_config" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_config

        out["WarmStartConfig"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.serialize_aws_json_1_1(
                value["warm_start_config"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "tuning_job_completion_details" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_completion_details

        out["TuningJobCompletionDetails"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_completion_details.serialize_aws_json_1_1(
                value["tuning_job_completion_details"]
            )
        )
    if "consumed_resources" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_consumed_resources

        out["ConsumedResources"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_consumed_resources.serialize_aws_json_1_1(
                value["consumed_resources"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobSearchEntity:
    out: HyperParameterTuningJobSearchEntity = {}  # type: ignore[typeddict-item]
    if data.get("HyperParameterTuningJobName") is not None:
        out["hyper_parameter_tuning_job_name"] = data["HyperParameterTuningJobName"]
    if data.get("HyperParameterTuningJobArn") is not None:
        out["hyper_parameter_tuning_job_arn"] = data["HyperParameterTuningJobArn"]
    if data.get("HyperParameterTuningJobConfig") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_config

        out["hyper_parameter_tuning_job_config"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_config.deserialize_aws_json_1_1(
                data["HyperParameterTuningJobConfig"]
            )
        )
    if data.get("TrainingJobDefinition") is not None:
        import capo_sagemaker.types.hyper_parameter_training_job_definition

        out["training_job_definition"] = (
            capo_sagemaker.types.hyper_parameter_training_job_definition.deserialize_aws_json_1_1(
                data["TrainingJobDefinition"]
            )
        )
    if data.get("TrainingJobDefinitions") is not None:
        import capo_sagemaker.types.hyper_parameter_training_job_definitions

        out["training_job_definitions"] = (
            capo_sagemaker.types.hyper_parameter_training_job_definitions.deserialize_aws_json_1_1(
                data["TrainingJobDefinitions"]
            )
        )
    if data.get("HyperParameterTuningJobStatus") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_status

        out["hyper_parameter_tuning_job_status"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_status.deserialize_aws_json_1_1(
                data["HyperParameterTuningJobStatus"]
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
    if data.get("BestTrainingJob") is not None:
        import capo_sagemaker.types.hyper_parameter_training_job_summary

        out["best_training_job"] = (
            capo_sagemaker.types.hyper_parameter_training_job_summary.deserialize_aws_json_1_1(
                data["BestTrainingJob"]
            )
        )
    if data.get("OverallBestTrainingJob") is not None:
        import capo_sagemaker.types.hyper_parameter_training_job_summary

        out["overall_best_training_job"] = (
            capo_sagemaker.types.hyper_parameter_training_job_summary.deserialize_aws_json_1_1(
                data["OverallBestTrainingJob"]
            )
        )
    if data.get("WarmStartConfig") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_config

        out["warm_start_config"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_config.deserialize_aws_json_1_1(
                data["WarmStartConfig"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("TuningJobCompletionDetails") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_completion_details

        out["tuning_job_completion_details"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_completion_details.deserialize_aws_json_1_1(
                data["TuningJobCompletionDetails"]
            )
        )
    if data.get("ConsumedResources") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_consumed_resources

        out["consumed_resources"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_consumed_resources.deserialize_aws_json_1_1(
                data["ConsumedResources"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
