"""Generated from Smithy shape ``com.amazonaws.forecastquery#Forecast``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecastquery.types.predictions


class Forecast(TypedDict, closed=True):
    predictions: NotRequired["capo_forecastquery.types.predictions.Predictions"]
    """<p>The forecast.</p> <p>The <i>string</i> of the string-to-array map is one of the following values:</p> <ul> <li> <p>p10</p> </li> <li> <p>p50</p> </li> <li> <p>p90</p> </li> </ul> <p>The default setting is <code>["0.1", "0.5", "0.9"]</code>. Use the optional <code>ForecastTypes</code> parameter of the <a href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecast.html">CreateForecast</a> operation to change the values. The values will vary depending on how this is set, with a minimum of <code>1</code> and a maximum of <code>5.</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Forecast) -> dict:
    out: dict = {}
    if "predictions" in value:
        import capo_forecastquery.types.predictions

        out["Predictions"] = (
            capo_forecastquery.types.predictions.serialize_aws_json_1_1(
                value["predictions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Forecast:
    out: Forecast = {}  # type: ignore[typeddict-item]
    if data.get("Predictions") is not None:
        import capo_forecastquery.types.predictions

        out["predictions"] = (
            capo_forecastquery.types.predictions.deserialize_aws_json_1_1(
                data["Predictions"]
            )
        )
    return out
