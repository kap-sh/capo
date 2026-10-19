"""Generated from Smithy shape ``com.amazonaws.forecast#DescribePredictorBacktestExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DescribePredictorBacktestExportJobRequest(TypedDict, closed=True):
    predictor_backtest_export_job_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the predictor backtest export job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePredictorBacktestExportJobRequest) -> dict:
    out: dict = {}
    out["PredictorBacktestExportJobArn"] = value["predictor_backtest_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePredictorBacktestExportJobRequest:
    out: DescribePredictorBacktestExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("PredictorBacktestExportJobArn") is not None:
        out["predictor_backtest_export_job_arn"] = data["PredictorBacktestExportJobArn"]
    else:
        out["predictor_backtest_export_job_arn"] = ""
    return out
