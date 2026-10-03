"""Generated from Smithy shape ``com.amazonaws.pinpoint#ApplicationDateRangeKpiResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.__timestamp_iso8601
    import capo_pinpoint.types.base_kpi_result


class ApplicationDateRangeKpiResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the metric applies to.</p>"""
    end_time: NotRequired["capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The last date and time of the date range that was used to filter the query results, in extended ISO 8601 format. The date range is inclusive.</p>"""
    kpi_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, that the data was retrieved for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. For a list of possible values, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html">Amazon Pinpoint Developer Guide</a>.</p>"""
    kpi_result: NotRequired["capo_pinpoint.types.base_kpi_result.BaseKpiResult"]
    """<p>An array of objects that contains the results of the query. Each object contains the value for the metric and metadata about that value.</p>"""
    next_token: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null for the Application Metrics resource because the resource returns all results in a single page.</p>"""
    start_time: NotRequired[
        "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The first date and time of the date range that was used to filter the query results, in extended ISO 8601 format. The date range is inclusive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationDateRangeKpiResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "end_time" in value:
        import capo_pinpoint.types.__timestamp_iso8601

        out["EndTime"] = capo_pinpoint.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    if "kpi_name" in value:
        out["KpiName"] = value["kpi_name"]
    if "kpi_result" in value:
        import capo_pinpoint.types.base_kpi_result

        out["KpiResult"] = capo_pinpoint.types.base_kpi_result.serialize_json(
            value["kpi_result"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "start_time" in value:
        import capo_pinpoint.types.__timestamp_iso8601

        out["StartTime"] = capo_pinpoint.types.__timestamp_iso8601.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> ApplicationDateRangeKpiResponse:
    out: ApplicationDateRangeKpiResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("EndTime") is not None:
        import capo_pinpoint.types.__timestamp_iso8601

        out["end_time"] = capo_pinpoint.types.__timestamp_iso8601.deserialize_json(
            data["EndTime"]
        )
    if data.get("KpiName") is not None:
        out["kpi_name"] = data["KpiName"]
    if data.get("KpiResult") is not None:
        import capo_pinpoint.types.base_kpi_result

        out["kpi_result"] = capo_pinpoint.types.base_kpi_result.deserialize_json(
            data["KpiResult"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("StartTime") is not None:
        import capo_pinpoint.types.__timestamp_iso8601

        out["start_time"] = capo_pinpoint.types.__timestamp_iso8601.deserialize_json(
            data["StartTime"]
        )
    return out
