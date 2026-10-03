"""Generated from Smithy shape ``com.amazonaws.forecast#CreateForecastRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.forecast_types
    import capo_forecast.types.name
    import capo_forecast.types.tags
    import capo_forecast.types.time_series_selector


class CreateForecastRequest(TypedDict, closed=True):
    forecast_name: "capo_forecast.types.name.Name"
    """<p>A name for the forecast.</p>"""
    predictor_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the predictor to use to generate the forecast.</p>"""
    forecast_types: NotRequired["capo_forecast.types.forecast_types.ForecastTypes"]
    """<p>The quantiles at which probabilistic forecasts are generated. <b>You can currently specify up to 5 quantiles per forecast</b>. Accepted values include <code>0.01 to 0.99</code> (increments of .01 only) and <code>mean</code>. The mean forecast is different from the median (0.50) when the distribution is not symmetric (for example, Beta and Negative Binomial). </p> <p>The default quantiles are the quantiles you specified during predictor creation. If you didn't specify quantiles, the default values are <code>["0.1", "0.5", "0.9"]</code>. </p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>The optional metadata that you apply to the forecast to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>"""
    time_series_selector: NotRequired[
        "capo_forecast.types.time_series_selector.TimeSeriesSelector"
    ]
    """<p>Defines the set of time series that are used to create the forecasts in a <code>TimeSeriesIdentifiers</code> object.</p> <p>The <code>TimeSeriesIdentifiers</code> object needs the following information:</p> <ul> <li> <p> <code>DataSource</code> </p> </li> <li> <p> <code>Format</code> </p> </li> <li> <p> <code>Schema</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateForecastRequest) -> dict:
    out: dict = {}
    out["ForecastName"] = value["forecast_name"]
    out["PredictorArn"] = value["predictor_arn"]
    if "forecast_types" in value:
        import capo_forecast.types.forecast_types

        out["ForecastTypes"] = (
            capo_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    if "time_series_selector" in value:
        import capo_forecast.types.time_series_selector

        out["TimeSeriesSelector"] = (
            capo_forecast.types.time_series_selector.serialize_aws_json_1_1(
                value["time_series_selector"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateForecastRequest:
    out: CreateForecastRequest = {}  # type: ignore[typeddict-item]
    if data.get("ForecastName") is not None:
        out["forecast_name"] = data["ForecastName"]
    else:
        raise DeserializationError("CreateForecastRequest.forecast_name required")
    if data.get("PredictorArn") is not None:
        out["predictor_arn"] = data["PredictorArn"]
    else:
        raise DeserializationError("CreateForecastRequest.predictor_arn required")
    if data.get("ForecastTypes") is not None:
        import capo_forecast.types.forecast_types

        out["forecast_types"] = (
            capo_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("TimeSeriesSelector") is not None:
        import capo_forecast.types.time_series_selector

        out["time_series_selector"] = (
            capo_forecast.types.time_series_selector.deserialize_aws_json_1_1(
                data["TimeSeriesSelector"]
            )
        )
    return out
