"""Generated from Smithy shape ``com.amazonaws.forecastquery#QueryForecastRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_forecastquery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecastquery.types.arn
    import capo_forecastquery.types.date_time
    import capo_forecastquery.types.filters
    import capo_forecastquery.types.next_token


class QueryForecastRequest(TypedDict, closed=True):
    forecast_arn: "capo_forecastquery.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the forecast to query.</p>"""
    start_date: NotRequired["capo_forecastquery.types.date_time.DateTime"]
    """<p>The start date for the forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T08:00:00.</p>"""
    end_date: NotRequired["capo_forecastquery.types.date_time.DateTime"]
    """<p>The end date for the forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T20:00:00. </p>"""
    filters: "capo_forecastquery.types.filters.Filters"
    """<p>The filtering criteria to apply when retrieving the forecast. For example, to get the forecast for <code>client_21</code> in the electricity usage dataset, specify the following:</p> <p> <code>{"item_id" : "client_21"}</code> </p> <p>To get the full forecast, use the <a href="https://docs.aws.amazon.com/en_us/forecast/latest/dg/API_CreateForecastExportJob.html">CreateForecastExportJob</a> operation.</p>"""
    next_token: NotRequired["capo_forecastquery.types.next_token.NextToken"]
    """<p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryForecastRequest) -> dict:
    out: dict = {}
    out["ForecastArn"] = value["forecast_arn"]
    if "start_date" in value:
        out["StartDate"] = value["start_date"]
    if "end_date" in value:
        out["EndDate"] = value["end_date"]
    import capo_forecastquery.types.filters

    out["Filters"] = capo_forecastquery.types.filters.serialize_aws_json_1_1(
        value["filters"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryForecastRequest:
    out: QueryForecastRequest = {}  # type: ignore[typeddict-item]
    if data.get("ForecastArn") is not None:
        out["forecast_arn"] = data["ForecastArn"]
    else:
        raise DeserializationError("QueryForecastRequest.forecast_arn required")
    if data.get("StartDate") is not None:
        out["start_date"] = data["StartDate"]
    if data.get("EndDate") is not None:
        out["end_date"] = data["EndDate"]
    if data.get("Filters") is not None:
        import capo_forecastquery.types.filters

        out["filters"] = capo_forecastquery.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    else:
        raise DeserializationError("QueryForecastRequest.filters required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
