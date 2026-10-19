"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeForecastRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DescribeForecastRequest(TypedDict, closed=True):
    forecast_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the forecast.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeForecastRequest) -> dict:
    out: dict = {}
    out["ForecastArn"] = value["forecast_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeForecastRequest:
    out: DescribeForecastRequest = {}  # type: ignore[typeddict-item]
    if data.get("ForecastArn") is not None:
        out["forecast_arn"] = data["ForecastArn"]
    else:
        out["forecast_arn"] = ""
    return out
