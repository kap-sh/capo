"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLAlgorithmConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_algorithms


class AutoMLAlgorithmConfig(TypedDict, closed=True):
    auto_ml_algorithms: NotRequired[
        "capo_sagemaker.types.auto_ml_algorithms.AutoMLAlgorithms"
    ]
    """<p>The selection of algorithms trained on your dataset to generate the model candidates for an Autopilot job.</p> <ul> <li> <p> <b>For the tabular problem type <code>TabularJobConfig</code>:</b> </p> <note> <p>Selected algorithms must belong to the list corresponding to the training mode set in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html#sagemaker-Type-AutoMLJobConfig-Mode">AutoMLJobConfig.Mode</a> (<code>ENSEMBLING</code> or <code>HYPERPARAMETER_TUNING</code>). Choose a minimum of 1 algorithm.</p> </note> <ul> <li> <p>In <code>ENSEMBLING</code> mode:</p> <ul> <li> <p>"catboost"</p> </li> <li> <p>"extra-trees"</p> </li> <li> <p>"fastai"</p> </li> <li> <p>"lightgbm"</p> </li> <li> <p>"linear-learner"</p> </li> <li> <p>"nn-torch"</p> </li> <li> <p>"randomforest"</p> </li> <li> <p>"xgboost"</p> </li> </ul> </li> <li> <p>In <code>HYPERPARAMETER_TUNING</code> mode:</p> <ul> <li> <p>"linear-learner"</p> </li> <li> <p>"mlp"</p> </li> <li> <p>"xgboost"</p> </li> </ul> </li> </ul> </li> <li> <p> <b>For the time-series forecasting problem type <code>TimeSeriesForecastingJobConfig</code>:</b> </p> <ul> <li> <p>Choose your algorithms from this list.</p> <ul> <li> <p>"cnn-qr"</p> </li> <li> <p>"deepar"</p> </li> <li> <p>"prophet"</p> </li> <li> <p>"arima"</p> </li> <li> <p>"npts"</p> </li> <li> <p>"ets"</p> </li> </ul> </li> </ul> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLAlgorithmConfig) -> dict:
    out: dict = {}
    if "auto_ml_algorithms" in value:
        import capo_sagemaker.types.auto_ml_algorithms

        out["AutoMLAlgorithms"] = (
            capo_sagemaker.types.auto_ml_algorithms.serialize_aws_json_1_1(
                value["auto_ml_algorithms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLAlgorithmConfig:
    out: AutoMLAlgorithmConfig = {}  # type: ignore[typeddict-item]
    if data.get("AutoMLAlgorithms") is not None:
        import capo_sagemaker.types.auto_ml_algorithms

        out["auto_ml_algorithms"] = (
            capo_sagemaker.types.auto_ml_algorithms.deserialize_aws_json_1_1(
                data["AutoMLAlgorithms"]
            )
        )
    return out
