"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateGenerationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_algorithms_config


class CandidateGenerationConfig(TypedDict, closed=True):
    algorithms_config: NotRequired[
        "capo_sagemaker.types.auto_ml_algorithms_config.AutoMLAlgorithmsConfig"
    ]
    """<p>Your Autopilot job trains a default set of algorithms on your dataset. For tabular and time-series data, you can customize the algorithm list by selecting a subset of algorithms for your problem type.</p> <p> <code>AlgorithmsConfig</code> stores the customized selection of algorithms to train on your data.</p> <ul> <li> <p> <b>For the tabular problem type <code>TabularJobConfig</code>,</b> the list of available algorithms to choose from depends on the training mode set in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html"> <code>AutoMLJobConfig.Mode</code> </a>.</p> <ul> <li> <p> <code>AlgorithmsConfig</code> should not be set when the training mode <code>AutoMLJobConfig.Mode</code> is set to <code>AUTO</code>.</p> </li> <li> <p>When <code>AlgorithmsConfig</code> is provided, one <code>AutoMLAlgorithms</code> attribute must be set and one only.</p> <p>If the list of algorithms provided as values for <code>AutoMLAlgorithms</code> is empty, <code>CandidateGenerationConfig</code> uses the full set of algorithms for the given training mode.</p> </li> <li> <p>When <code>AlgorithmsConfig</code> is not provided, <code>CandidateGenerationConfig</code> uses the full set of algorithms for the given training mode.</p> </li> </ul> <p>For the list of all algorithms per training mode, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html"> AlgorithmConfig</a>.</p> <p>For more information on each algorithm, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-algorithm-support">Algorithm support</a> section in the Autopilot developer guide.</p> </li> <li> <p> <b>For the time-series forecasting problem type <code>TimeSeriesForecastingJobConfig</code>,</b> choose your algorithms from the list provided in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html"> AlgorithmConfig</a>.</p> <p>For more information on each algorithm, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-algorithms.html">Algorithms support for time-series forecasting</a> section in the Autopilot developer guide.</p> <ul> <li> <p>When <code>AlgorithmsConfig</code> is provided, one <code>AutoMLAlgorithms</code> attribute must be set and one only.</p> <p>If the list of algorithms provided as values for <code>AutoMLAlgorithms</code> is empty, <code>CandidateGenerationConfig</code> uses the full set of algorithms for time-series forecasting.</p> </li> <li> <p>When <code>AlgorithmsConfig</code> is not provided, <code>CandidateGenerationConfig</code> uses the full set of algorithms for time-series forecasting.</p> </li> </ul> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CandidateGenerationConfig) -> dict:
    out: dict = {}
    if "algorithms_config" in value:
        import capo_sagemaker.types.auto_ml_algorithms_config

        out["AlgorithmsConfig"] = (
            capo_sagemaker.types.auto_ml_algorithms_config.serialize_aws_json_1_1(
                value["algorithms_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CandidateGenerationConfig:
    out: CandidateGenerationConfig = {}  # type: ignore[typeddict-item]
    if data.get("AlgorithmsConfig") is not None:
        import capo_sagemaker.types.auto_ml_algorithms_config

        out["algorithms_config"] = (
            capo_sagemaker.types.auto_ml_algorithms_config.deserialize_aws_json_1_1(
                data["AlgorithmsConfig"]
            )
        )
    return out
