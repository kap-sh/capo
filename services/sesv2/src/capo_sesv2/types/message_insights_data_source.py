"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageInsightsDataSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.message_insights_export_max_results
    import capo_sesv2.types.message_insights_filters
    import capo_sesv2.types.timestamp


class MessageInsightsDataSource(TypedDict, closed=True):
    start_date: "capo_sesv2.types.timestamp.Timestamp"
    """<p>Represents the start date for the export interval as a timestamp. The start date is inclusive.</p>"""
    end_date: "capo_sesv2.types.timestamp.Timestamp"
    """<p>Represents the end date for the export interval as a timestamp. The end date is inclusive.</p>"""
    include: NotRequired[
        "capo_sesv2.types.message_insights_filters.MessageInsightsFilters"
    ]
    """<p>Filters for results to be included in the export file.</p>"""
    exclude: NotRequired[
        "capo_sesv2.types.message_insights_filters.MessageInsightsFilters"
    ]
    """<p>Filters for results to be excluded from the export file.</p>"""
    max_results: NotRequired[
        "capo_sesv2.types.message_insights_export_max_results.MessageInsightsExportMaxResults"
    ]
    """<p>The maximum number of results.</p> <note> <p>If you don't specify <code>MaxResults</code>, the export returns a maximum of 1,000 results.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageInsightsDataSource) -> dict:
    out: dict = {}
    import capo_sesv2.types.timestamp

    out["StartDate"] = capo_sesv2.types.timestamp.serialize_json(value["start_date"])
    import capo_sesv2.types.timestamp

    out["EndDate"] = capo_sesv2.types.timestamp.serialize_json(value["end_date"])
    if "include" in value:
        import capo_sesv2.types.message_insights_filters

        out["Include"] = capo_sesv2.types.message_insights_filters.serialize_json(
            value["include"]
        )
    if "exclude" in value:
        import capo_sesv2.types.message_insights_filters

        out["Exclude"] = capo_sesv2.types.message_insights_filters.serialize_json(
            value["exclude"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> MessageInsightsDataSource:
    out: MessageInsightsDataSource = {}  # type: ignore[typeddict-item]
    if data.get("StartDate") is not None:
        import capo_sesv2.types.timestamp

        out["start_date"] = capo_sesv2.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndDate") is not None:
        import capo_sesv2.types.timestamp

        out["end_date"] = capo_sesv2.types.timestamp.deserialize_json(data["EndDate"])
    else:
        import datetime

        out["end_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Include") is not None:
        import capo_sesv2.types.message_insights_filters

        out["include"] = capo_sesv2.types.message_insights_filters.deserialize_json(
            data["Include"]
        )
    if data.get("Exclude") is not None:
        import capo_sesv2.types.message_insights_filters

        out["exclude"] = capo_sesv2.types.message_insights_filters.deserialize_json(
            data["Exclude"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


def redact_sensitive(value: MessageInsightsDataSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "include" in value:
        import capo_sesv2.types.message_insights_filters

        out["include"] = capo_sesv2.types.message_insights_filters.redact_sensitive(
            value["include"]
        )
    if "exclude" in value:
        import capo_sesv2.types.message_insights_filters

        out["exclude"] = capo_sesv2.types.message_insights_filters.redact_sensitive(
            value["exclude"]
        )
    return out
