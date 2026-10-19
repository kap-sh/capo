"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteForecastExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DeleteForecastExportJobRequest(TypedDict, closed=True):
    forecast_export_job_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the forecast export job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteForecastExportJobRequest) -> dict:
    out: dict = {}
    out["ForecastExportJobArn"] = value["forecast_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteForecastExportJobRequest:
    out: DeleteForecastExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("ForecastExportJobArn") is not None:
        out["forecast_export_job_arn"] = data["ForecastExportJobArn"]
    else:
        out["forecast_export_job_arn"] = ""
    return out
