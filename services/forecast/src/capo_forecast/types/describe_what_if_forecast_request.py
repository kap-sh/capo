"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeWhatIfForecastRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.long_arn


class DescribeWhatIfForecastRequest(TypedDict, closed=True):
    what_if_forecast_arn: "capo_forecast.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of the what-if forecast that you are interested in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWhatIfForecastRequest) -> dict:
    out: dict = {}
    out["WhatIfForecastArn"] = value["what_if_forecast_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWhatIfForecastRequest:
    out: DescribeWhatIfForecastRequest = {}  # type: ignore[typeddict-item]
    if data.get("WhatIfForecastArn") is not None:
        out["what_if_forecast_arn"] = data["WhatIfForecastArn"]
    else:
        out["what_if_forecast_arn"] = ""
    return out
