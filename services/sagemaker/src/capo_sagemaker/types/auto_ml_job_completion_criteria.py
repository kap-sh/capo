"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobCompletionCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_auto_ml_job_runtime_in_seconds
    import capo_sagemaker.types.max_candidates
    import capo_sagemaker.types.max_runtime_per_training_job_in_seconds


class AutoMLJobCompletionCriteria(TypedDict, closed=True):
    max_candidates: NotRequired["capo_sagemaker.types.max_candidates.MaxCandidates"]
    """<p>The maximum number of times a training job is allowed to run.</p> <p>For text and image classification, time-series forecasting, as well as text generation (LLMs fine-tuning) problem types, the supported value is 1. For tabular problem types, the maximum value is 750.</p>"""
    max_runtime_per_training_job_in_seconds: NotRequired[
        "capo_sagemaker.types.max_runtime_per_training_job_in_seconds.MaxRuntimePerTrainingJobInSeconds"
    ]
    """<p>The maximum time, in seconds, that each training job executed inside hyperparameter tuning is allowed to run as part of a hyperparameter tuning job. For more information, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StoppingCondition.html">StoppingCondition</a> used by the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html">CreateHyperParameterTuningJob</a> action.</p> <p>For job V2s (jobs created by calling <code>CreateAutoMLJobV2</code>), this field controls the runtime of the job candidate.</p> <p>For <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextClassificationJobConfig.html">TextGenerationJobConfig</a> problem types, the maximum time defaults to 72 hours (259200 seconds).</p>"""
    max_auto_ml_job_runtime_in_seconds: NotRequired[
        "capo_sagemaker.types.max_auto_ml_job_runtime_in_seconds.MaxAutoMLJobRuntimeInSeconds"
    ]
    """<p>The maximum runtime, in seconds, an AutoML job has to complete.</p> <p>If an AutoML job exceeds the maximum runtime, the job is stopped automatically and its processing is ended gracefully. The AutoML job identifies the best model whose training was completed and marks it as the best-performing model. Any unfinished steps of the job, such as automatic one-click Autopilot model deployment, are not completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobCompletionCriteria) -> dict:
    out: dict = {}
    if "max_candidates" in value:
        out["MaxCandidates"] = value["max_candidates"]
    if "max_runtime_per_training_job_in_seconds" in value:
        out["MaxRuntimePerTrainingJobInSeconds"] = value[
            "max_runtime_per_training_job_in_seconds"
        ]
    if "max_auto_ml_job_runtime_in_seconds" in value:
        out["MaxAutoMLJobRuntimeInSeconds"] = value[
            "max_auto_ml_job_runtime_in_seconds"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLJobCompletionCriteria:
    out: AutoMLJobCompletionCriteria = {}  # type: ignore[typeddict-item]
    if data.get("MaxCandidates") is not None:
        out["max_candidates"] = data["MaxCandidates"]
    if data.get("MaxRuntimePerTrainingJobInSeconds") is not None:
        out["max_runtime_per_training_job_in_seconds"] = data[
            "MaxRuntimePerTrainingJobInSeconds"
        ]
    if data.get("MaxAutoMLJobRuntimeInSeconds") is not None:
        out["max_auto_ml_job_runtime_in_seconds"] = data["MaxAutoMLJobRuntimeInSeconds"]
    return out
