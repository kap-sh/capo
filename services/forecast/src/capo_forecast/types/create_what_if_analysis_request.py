"""Generated from Smithy shape ``com.amazonaws.forecast#CreateWhatIfAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.name
    import capo_forecast.types.tags
    import capo_forecast.types.time_series_selector


class CreateWhatIfAnalysisRequest(TypedDict, closed=True):
    what_if_analysis_name: "capo_forecast.types.name.Name"
    """<p>The name of the what-if analysis. Each name must be unique.</p>"""
    forecast_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the baseline forecast.</p>"""
    time_series_selector: NotRequired[
        "capo_forecast.types.time_series_selector.TimeSeriesSelector"
    ]
    """<p>Defines the set of time series that are used in the what-if analysis with a <code>TimeSeriesIdentifiers</code> object. What-if analyses are performed only for the time series in this object.</p> <p>The <code>TimeSeriesIdentifiers</code> object needs the following information:</p> <ul> <li> <p> <code>DataSource</code> </p> </li> <li> <p> <code>Format</code> </p> </li> <li> <p> <code>Schema</code> </p> </li> </ul>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html">tags</a> to apply to the what if forecast.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWhatIfAnalysisRequest) -> dict:
    out: dict = {}
    out["WhatIfAnalysisName"] = value["what_if_analysis_name"]
    out["ForecastArn"] = value["forecast_arn"]
    if "time_series_selector" in value:
        import capo_forecast.types.time_series_selector

        out["TimeSeriesSelector"] = (
            capo_forecast.types.time_series_selector.serialize_aws_json_1_1(
                value["time_series_selector"]
            )
        )
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWhatIfAnalysisRequest:
    out: CreateWhatIfAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("WhatIfAnalysisName") is not None:
        out["what_if_analysis_name"] = data["WhatIfAnalysisName"]
    else:
        raise DeserializationError(
            "CreateWhatIfAnalysisRequest.what_if_analysis_name required"
        )
    if data.get("ForecastArn") is not None:
        out["forecast_arn"] = data["ForecastArn"]
    else:
        raise DeserializationError("CreateWhatIfAnalysisRequest.forecast_arn required")
    if data.get("TimeSeriesSelector") is not None:
        import capo_forecast.types.time_series_selector

        out["time_series_selector"] = (
            capo_forecast.types.time_series_selector.deserialize_aws_json_1_1(
                data["TimeSeriesSelector"]
            )
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
