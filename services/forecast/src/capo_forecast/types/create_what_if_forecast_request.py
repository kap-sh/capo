"""Generated from Smithy shape ``com.amazonaws.forecast#CreateWhatIfForecastRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.name
    import capo_forecast.types.tags
    import capo_forecast.types.time_series_replacements_data_source
    import capo_forecast.types.time_series_transformations


class CreateWhatIfForecastRequest(TypedDict, closed=True):
    what_if_forecast_name: "capo_forecast.types.name.Name"
    """<p>The name of the what-if forecast. Names must be unique within each what-if analysis.</p>"""
    what_if_analysis_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the what-if analysis.</p>"""
    time_series_transformations: NotRequired[
        "capo_forecast.types.time_series_transformations.TimeSeriesTransformations"
    ]
    """<p>The transformations that are applied to the baseline time series. Each transformation contains an action and a set of conditions. An action is applied only when all conditions are met. If no conditions are provided, the action is applied to all items.</p>"""
    time_series_replacements_data_source: NotRequired[
        "capo_forecast.types.time_series_replacements_data_source.TimeSeriesReplacementsDataSource"
    ]
    """<p>The replacement time series dataset, which contains the rows that you want to change in the related time series dataset. A replacement time series does not need to contain all rows that are in the baseline related time series. Include only the rows (measure-dimension combinations) that you want to include in the what-if forecast.</p> <p>This dataset is merged with the original time series to create a transformed dataset that is used for the what-if analysis.</p> <p>This dataset should contain the items to modify (such as item_id or workforce_type), any relevant dimensions, the timestamp column, and at least one of the related time series columns. This file should not contain duplicate timestamps for the same time series.</p> <p>Timestamps and item_ids not included in this dataset are not included in the what-if analysis. </p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html">tags</a> to apply to the what if forecast.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWhatIfForecastRequest) -> dict:
    out: dict = {}
    out["WhatIfForecastName"] = value["what_if_forecast_name"]
    out["WhatIfAnalysisArn"] = value["what_if_analysis_arn"]
    if "time_series_transformations" in value:
        import capo_forecast.types.time_series_transformations

        out["TimeSeriesTransformations"] = (
            capo_forecast.types.time_series_transformations.serialize_aws_json_1_1(
                value["time_series_transformations"]
            )
        )
    if "time_series_replacements_data_source" in value:
        import capo_forecast.types.time_series_replacements_data_source

        out["TimeSeriesReplacementsDataSource"] = (
            capo_forecast.types.time_series_replacements_data_source.serialize_aws_json_1_1(
                value["time_series_replacements_data_source"]
            )
        )
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWhatIfForecastRequest:
    out: CreateWhatIfForecastRequest = {}  # type: ignore[typeddict-item]
    if data.get("WhatIfForecastName") is not None:
        out["what_if_forecast_name"] = data["WhatIfForecastName"]
    else:
        raise DeserializationError(
            "CreateWhatIfForecastRequest.what_if_forecast_name required"
        )
    if data.get("WhatIfAnalysisArn") is not None:
        out["what_if_analysis_arn"] = data["WhatIfAnalysisArn"]
    else:
        raise DeserializationError(
            "CreateWhatIfForecastRequest.what_if_analysis_arn required"
        )
    if data.get("TimeSeriesTransformations") is not None:
        import capo_forecast.types.time_series_transformations

        out["time_series_transformations"] = (
            capo_forecast.types.time_series_transformations.deserialize_aws_json_1_1(
                data["TimeSeriesTransformations"]
            )
        )
    if data.get("TimeSeriesReplacementsDataSource") is not None:
        import capo_forecast.types.time_series_replacements_data_source

        out["time_series_replacements_data_source"] = (
            capo_forecast.types.time_series_replacements_data_source.deserialize_aws_json_1_1(
                data["TimeSeriesReplacementsDataSource"]
            )
        )
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
