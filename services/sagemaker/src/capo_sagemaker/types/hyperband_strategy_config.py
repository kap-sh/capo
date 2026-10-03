"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperbandStrategyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyperband_strategy_max_resource
    import capo_sagemaker.types.hyperband_strategy_min_resource


class HyperbandStrategyConfig(TypedDict, closed=True):
    min_resource: NotRequired[
        "capo_sagemaker.types.hyperband_strategy_min_resource.HyperbandStrategyMinResource"
    ]
    """<p>The minimum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. If the value for <code>MinResource</code> has not been reached, the training job is not stopped by <code>Hyperband</code>.</p>"""
    max_resource: NotRequired[
        "capo_sagemaker.types.hyperband_strategy_max_resource.HyperbandStrategyMaxResource"
    ]
    """<p>The maximum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. Once a job reaches the <code>MaxResource</code> value, it is stopped. If a value for <code>MaxResource</code> is not provided, and <code>Hyperband</code> is selected as the hyperparameter tuning strategy, <code>HyperbandTraining</code> attempts to infer <code>MaxResource</code> from the following keys (if present) in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-StaticHyperParameters">StaticsHyperParameters</a>:</p> <ul> <li> <p> <code>epochs</code> </p> </li> <li> <p> <code>numepochs</code> </p> </li> <li> <p> <code>n-epochs</code> </p> </li> <li> <p> <code>n_epochs</code> </p> </li> <li> <p> <code>num_epochs</code> </p> </li> </ul> <p>If <code>HyperbandStrategyConfig</code> is unable to infer a value for <code>MaxResource</code>, it generates a validation error. The maximum value is 20,000 epochs. All metrics that correspond to an objective metric are used to derive <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html">early stopping decisions</a>. For <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html">distributed</a> training jobs, ensure that duplicate metrics are not printed in the logs across the individual nodes in a training job. If multiple nodes are publishing duplicate or incorrect metrics, training jobs may make an incorrect stopping decision and stop the job prematurely. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperbandStrategyConfig) -> dict:
    out: dict = {}
    if "min_resource" in value:
        out["MinResource"] = value["min_resource"]
    if "max_resource" in value:
        out["MaxResource"] = value["max_resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperbandStrategyConfig:
    out: HyperbandStrategyConfig = {}  # type: ignore[typeddict-item]
    if data.get("MinResource") is not None:
        out["min_resource"] = data["MinResource"]
    if data.get("MaxResource") is not None:
        out["max_resource"] = data["MaxResource"]
    return out
