"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeWhatIfForecastResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.error_message
    import capo_forecast.types.forecast_types
    import capo_forecast.types.long
    import capo_forecast.types.long_arn
    import capo_forecast.types.name
    import capo_forecast.types.string
    import capo_forecast.types.time_series_replacements_data_source
    import capo_forecast.types.time_series_transformations
    import capo_forecast.types.timestamp


class DescribeWhatIfForecastResponse(TypedDict, closed=True):
    what_if_forecast_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the what-if forecast.</p>"""
    what_if_forecast_arn: NotRequired["capo_forecast.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the what-if forecast.</p>"""
    what_if_analysis_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the what-if analysis that contains this forecast.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["capo_forecast.types.long.Long"]
    """<p>The approximate time remaining to complete the what-if forecast, in minutes.</p>"""
    status: NotRequired["capo_forecast.types.string.String"]
    """<p>The status of the what-if forecast. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the what-if forecast must be <code>ACTIVE</code> before you can access the forecast.</p> </note>"""
    message: NotRequired["capo_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the what-if forecast was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    time_series_transformations: NotRequired[
        "capo_forecast.types.time_series_transformations.TimeSeriesTransformations"
    ]
    """<p>An array of <code>Action</code> and <code>TimeSeriesConditions</code> elements that describe what transformations were applied to which time series.</p>"""
    time_series_replacements_data_source: NotRequired[
        "capo_forecast.types.time_series_replacements_data_source.TimeSeriesReplacementsDataSource"
    ]
    """<p>An array of <code>S3Config</code>, <code>Schema</code>, and <code>Format</code> elements that describe the replacement time series.</p>"""
    forecast_types: NotRequired["capo_forecast.types.forecast_types.ForecastTypes"]
    """<p>The quantiles at which probabilistic forecasts are generated. You can specify up to five quantiles per what-if forecast in the <a>CreateWhatIfForecast</a> operation. If you didn't specify quantiles, the default values are <code>["0.1", "0.5", "0.9"]</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWhatIfForecastResponse) -> dict:
    out: dict = {}
    if "what_if_forecast_name" in value:
        out["WhatIfForecastName"] = value["what_if_forecast_name"]
    if "what_if_forecast_arn" in value:
        out["WhatIfForecastArn"] = value["what_if_forecast_arn"]
    if "what_if_analysis_arn" in value:
        out["WhatIfAnalysisArn"] = value["what_if_analysis_arn"]
    if "estimated_time_remaining_in_minutes" in value:
        out["EstimatedTimeRemainingInMinutes"] = value[
            "estimated_time_remaining_in_minutes"
        ]
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import capo_forecast.types.timestamp

        out["CreationTime"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import capo_forecast.types.timestamp

        out["LastModificationTime"] = (
            capo_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
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
    if "forecast_types" in value:
        import capo_forecast.types.forecast_types

        out["ForecastTypes"] = (
            capo_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWhatIfForecastResponse:
    out: DescribeWhatIfForecastResponse = {}  # type: ignore[typeddict-item]
    if data.get("WhatIfForecastName") is not None:
        out["what_if_forecast_name"] = data["WhatIfForecastName"]
    if data.get("WhatIfForecastArn") is not None:
        out["what_if_forecast_arn"] = data["WhatIfForecastArn"]
    if data.get("WhatIfAnalysisArn") is not None:
        out["what_if_analysis_arn"] = data["WhatIfAnalysisArn"]
    if data.get("EstimatedTimeRemainingInMinutes") is not None:
        out["estimated_time_remaining_in_minutes"] = data[
            "EstimatedTimeRemainingInMinutes"
        ]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("CreationTime") is not None:
        import capo_forecast.types.timestamp

        out["creation_time"] = capo_forecast.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModificationTime") is not None:
        import capo_forecast.types.timestamp

        out["last_modification_time"] = (
            capo_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
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
    if data.get("ForecastTypes") is not None:
        import capo_forecast.types.forecast_types

        out["forecast_types"] = (
            capo_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    return out
