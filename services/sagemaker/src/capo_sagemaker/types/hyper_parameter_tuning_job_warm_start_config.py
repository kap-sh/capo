"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobWarmStartConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_type
    import capo_sagemaker.types.parent_hyper_parameter_tuning_jobs


class HyperParameterTuningJobWarmStartConfig(TypedDict, closed=True):
    parent_hyper_parameter_tuning_jobs: NotRequired[
        "capo_sagemaker.types.parent_hyper_parameter_tuning_jobs.ParentHyperParameterTuningJobs"
    ]
    """<p>An array of hyperparameter tuning jobs that are used as the starting point for the new hyperparameter tuning job. For more information about warm starting a hyperparameter tuning job, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html">Using a Previous Hyperparameter Tuning Job as a Starting Point</a>.</p> <p>Hyperparameter tuning jobs created before October 1, 2018 cannot be used as parent jobs for warm start tuning jobs.</p>"""
    warm_start_type: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_type.HyperParameterTuningJobWarmStartType"
    ]
    """<p>Specifies one of the following:</p> <dl> <dt>IDENTICAL_DATA_AND_ALGORITHM</dt> <dd> <p>The new hyperparameter tuning job uses the same input data and training image as the parent tuning jobs. You can change the hyperparameter ranges to search and the maximum number of training jobs that the hyperparameter tuning job launches. You cannot use a new version of the training algorithm, unless the changes in the new version do not affect the algorithm itself. For example, changes that improve logging or adding support for a different data format are allowed. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.</p> </dd> <dt>TRANSFER_LEARNING</dt> <dd> <p>The new hyperparameter tuning job can include input data, hyperparameter ranges, maximum number of concurrent training jobs, and maximum number of training jobs that are different than those of its parent hyperparameter tuning jobs. The training image can also be a different version from the version used in the parent hyperparameter tuning job. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobWarmStartConfig) -> dict:
    out: dict = {}
    if "parent_hyper_parameter_tuning_jobs" in value:
        import capo_sagemaker.types.parent_hyper_parameter_tuning_jobs

        out["ParentHyperParameterTuningJobs"] = (
            capo_sagemaker.types.parent_hyper_parameter_tuning_jobs.serialize_aws_json_1_1(
                value["parent_hyper_parameter_tuning_jobs"]
            )
        )
    if "warm_start_type" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_type

        out["WarmStartType"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_type.serialize_aws_json_1_1(
                value["warm_start_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobWarmStartConfig:
    out: HyperParameterTuningJobWarmStartConfig = {}  # type: ignore[typeddict-item]
    if data.get("ParentHyperParameterTuningJobs") is not None:
        import capo_sagemaker.types.parent_hyper_parameter_tuning_jobs

        out["parent_hyper_parameter_tuning_jobs"] = (
            capo_sagemaker.types.parent_hyper_parameter_tuning_jobs.deserialize_aws_json_1_1(
                data["ParentHyperParameterTuningJobs"]
            )
        )
    if data.get("WarmStartType") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_type

        out["warm_start_type"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_warm_start_type.deserialize_aws_json_1_1(
                data["WarmStartType"]
            )
        )
    return out
