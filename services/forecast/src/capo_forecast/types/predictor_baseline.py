"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorBaseline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.baseline_metrics


class PredictorBaseline(TypedDict, closed=True):
    baseline_metrics: NotRequired[
        "capo_forecast.types.baseline_metrics.BaselineMetrics"
    ]
    """<p>The initial <a href="https://docs.aws.amazon.com/forecast/latest/dg/metrics.html">accuracy metrics</a> for the predictor. Use these metrics as a baseline for comparison purposes as you use your predictor and the metrics change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorBaseline) -> dict:
    out: dict = {}
    if "baseline_metrics" in value:
        import capo_forecast.types.baseline_metrics

        out["BaselineMetrics"] = (
            capo_forecast.types.baseline_metrics.serialize_aws_json_1_1(
                value["baseline_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictorBaseline:
    out: PredictorBaseline = {}  # type: ignore[typeddict-item]
    if data.get("BaselineMetrics") is not None:
        import capo_forecast.types.baseline_metrics

        out["baseline_metrics"] = (
            capo_forecast.types.baseline_metrics.deserialize_aws_json_1_1(
                data["BaselineMetrics"]
            )
        )
    return out
