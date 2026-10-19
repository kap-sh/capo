"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteWhatIfForecastRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.long_arn


class DeleteWhatIfForecastRequest(TypedDict, closed=True):
    what_if_forecast_arn: "capo_forecast.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of the what-if forecast that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWhatIfForecastRequest) -> dict:
    out: dict = {}
    out["WhatIfForecastArn"] = value["what_if_forecast_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWhatIfForecastRequest:
    out: DeleteWhatIfForecastRequest = {}  # type: ignore[typeddict-item]
    if data.get("WhatIfForecastArn") is not None:
        out["what_if_forecast_arn"] = data["WhatIfForecastArn"]
    else:
        out["what_if_forecast_arn"] = ""
    return out
