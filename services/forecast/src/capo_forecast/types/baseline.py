"""Generated from Smithy shape ``com.amazonaws.forecast#Baseline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.predictor_baseline


class Baseline(TypedDict, closed=True):
    predictor_baseline: NotRequired[
        "capo_forecast.types.predictor_baseline.PredictorBaseline"
    ]
    """<p>The initial <a href="https://docs.aws.amazon.com/forecast/latest/dg/metrics.html">accuracy metrics</a> for the predictor you are monitoring. Use these metrics as a baseline for comparison purposes as you use your predictor and the metrics change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Baseline) -> dict:
    out: dict = {}
    if "predictor_baseline" in value:
        import capo_forecast.types.predictor_baseline

        out["PredictorBaseline"] = (
            capo_forecast.types.predictor_baseline.serialize_aws_json_1_1(
                value["predictor_baseline"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Baseline:
    out: Baseline = {}  # type: ignore[typeddict-item]
    if data.get("PredictorBaseline") is not None:
        import capo_forecast.types.predictor_baseline

        out["predictor_baseline"] = (
            capo_forecast.types.predictor_baseline.deserialize_aws_json_1_1(
                data["PredictorBaseline"]
            )
        )
    return out
