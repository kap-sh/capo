"""Generated from Smithy shape ``com.amazonaws.sagemaker#TextGenerationJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_completion_criteria
    import capo_sagemaker.types.base_model_name
    import capo_sagemaker.types.model_access_config
    import capo_sagemaker.types.text_generation_hyper_parameters


class TextGenerationJobConfig(TypedDict, closed=True):
    completion_criteria: NotRequired[
        "capo_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]
    """<p>How long a fine-tuning job is allowed to run. For <code>TextGenerationJobConfig</code> problem types, the <code>MaxRuntimePerTrainingJobInSeconds</code> attribute of <code>AutoMLJobCompletionCriteria</code> defaults to 72h (259200s).</p>"""
    base_model_name: NotRequired["capo_sagemaker.types.base_model_name.BaseModelName"]
    """<p>The name of the base model to fine-tune. Autopilot supports fine-tuning a variety of large language models. For information on the list of supported models, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-models.html#autopilot-llms-finetuning-supported-llms">Text generation models supporting fine-tuning in Autopilot</a>. If no <code>BaseModelName</code> is provided, the default model used is <b>Falcon7BInstruct</b>. </p>"""
    text_generation_hyper_parameters: NotRequired[
        "capo_sagemaker.types.text_generation_hyper_parameters.TextGenerationHyperParameters"
    ]
    """<p>The hyperparameters used to configure and optimize the learning process of the base model. You can set any combination of the following hyperparameters for all base models. For more information on each supported hyperparameter, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-llms-finetuning-set-hyperparameters.html">Optimize the learning process of your text generation models with hyperparameters</a>.</p> <ul> <li> <p> <code>"epochCount"</code>: The number of times the model goes through the entire training dataset. Its value should be a string containing an integer value within the range of "1" to "10".</p> </li> <li> <p> <code>"batchSize"</code>: The number of data samples used in each iteration of training. Its value should be a string containing an integer value within the range of "1" to "64".</p> </li> <li> <p> <code>"learningRate"</code>: The step size at which a model's parameters are updated during training. Its value should be a string containing a floating-point value within the range of "0" to "1".</p> </li> <li> <p> <code>"learningRateWarmupSteps"</code>: The number of training steps during which the learning rate gradually increases before reaching its target or maximum value. Its value should be a string containing an integer value within the range of "0" to "250".</p> </li> </ul> <p>Here is an example where all four hyperparameters are configured.</p> <p> <code>{ "epochCount":"5", "learningRate":"0.5", "batchSize": "32", "learningRateWarmupSteps": "10" }</code> </p>"""
    model_access_config: NotRequired[
        "capo_sagemaker.types.model_access_config.ModelAccessConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextGenerationJobConfig) -> dict:
    out: dict = {}
    if "completion_criteria" in value:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    if "base_model_name" in value:
        out["BaseModelName"] = value["base_model_name"]
    if "text_generation_hyper_parameters" in value:
        import capo_sagemaker.types.text_generation_hyper_parameters

        out["TextGenerationHyperParameters"] = (
            capo_sagemaker.types.text_generation_hyper_parameters.serialize_aws_json_1_1(
                value["text_generation_hyper_parameters"]
            )
        )
    if "model_access_config" in value:
        import capo_sagemaker.types.model_access_config

        out["ModelAccessConfig"] = (
            capo_sagemaker.types.model_access_config.serialize_aws_json_1_1(
                value["model_access_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextGenerationJobConfig:
    out: TextGenerationJobConfig = {}  # type: ignore[typeddict-item]
    if data.get("CompletionCriteria") is not None:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    if data.get("BaseModelName") is not None:
        out["base_model_name"] = data["BaseModelName"]
    if data.get("TextGenerationHyperParameters") is not None:
        import capo_sagemaker.types.text_generation_hyper_parameters

        out["text_generation_hyper_parameters"] = (
            capo_sagemaker.types.text_generation_hyper_parameters.deserialize_aws_json_1_1(
                data["TextGenerationHyperParameters"]
            )
        )
    if data.get("ModelAccessConfig") is not None:
        import capo_sagemaker.types.model_access_config

        out["model_access_config"] = (
            capo_sagemaker.types.model_access_config.deserialize_aws_json_1_1(
                data["ModelAccessConfig"]
            )
        )
    return out
