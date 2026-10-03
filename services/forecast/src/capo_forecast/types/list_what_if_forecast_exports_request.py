"""Generated from Smithy shape ``com.amazonaws.forecast#ListWhatIfForecastExportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.filters
    import capo_forecast.types.max_results
    import capo_forecast.types.next_token


class ListWhatIfForecastExportsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>"""
    max_results: NotRequired["capo_forecast.types.max_results.MaxResults"]
    """<p>The number of items to return in the response.</p>"""
    filters: NotRequired["capo_forecast.types.filters.Filters"]
    """<p>An array of filters. For each filter, you provide a condition and a match statement. The condition is either <code>IS</code> or <code>IS_NOT</code>, which specifies whether to include or exclude the what-if forecast export jobs that match the statement from the list, respectively. The match statement consists of a key and a value.</p> <p> <b>Filter properties</b> </p> <ul> <li> <p> <code>Condition</code> - The condition to apply. Valid values are <code>IS</code> and <code>IS_NOT</code>. To include the forecast export jobs that match the statement, specify <code>IS</code>. To exclude matching forecast export jobs, specify <code>IS_NOT</code>.</p> </li> <li> <p> <code>Key</code> - The name of the parameter to filter on. Valid values are <code>WhatIfForecastExportArn</code> and <code>Status</code>.</p> </li> <li> <p> <code>Value</code> - The value to match.</p> </li> </ul> <p>For example, to list all jobs that export a forecast named <i>electricityWIFExport</i>, specify the following filter:</p> <p> <code>"Filters": [ { "Condition": "IS", "Key": "WhatIfForecastExportArn", "Value": "arn:aws:forecast:us-west-2:<acct-id>:forecast/electricityWIFExport" } ]</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWhatIfForecastExportsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_forecast.types.filters

        out["Filters"] = capo_forecast.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWhatIfForecastExportsRequest:
    out: ListWhatIfForecastExportsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_forecast.types.filters

        out["filters"] = capo_forecast.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out
