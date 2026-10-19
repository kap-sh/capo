"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteWhatIfForecastExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.long_arn


class DeleteWhatIfForecastExportRequest(TypedDict, closed=True):
    what_if_forecast_export_arn: "capo_forecast.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of the what-if forecast export that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWhatIfForecastExportRequest) -> dict:
    out: dict = {}
    out["WhatIfForecastExportArn"] = value["what_if_forecast_export_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWhatIfForecastExportRequest:
    out: DeleteWhatIfForecastExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("WhatIfForecastExportArn") is not None:
        out["what_if_forecast_export_arn"] = data["WhatIfForecastExportArn"]
    else:
        out["what_if_forecast_export_arn"] = ""
    return out
