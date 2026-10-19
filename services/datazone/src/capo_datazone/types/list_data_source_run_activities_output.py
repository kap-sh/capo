"""Generated from Smithy shape ``com.amazonaws.datazone#ListDataSourceRunActivitiesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_source_run_activities
    import capo_datazone.types.pagination_token


class ListDataSourceRunActivitiesOutput(TypedDict, closed=True):
    items: "capo_datazone.types.data_source_run_activities.DataSourceRunActivities"
    """<p>The results of the <code>ListDataSourceRunActivities</code> action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of activities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of activities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRunActivities</code> to list the next set of activities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourceRunActivitiesOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.data_source_run_activities

    out["items"] = capo_datazone.types.data_source_run_activities.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSourceRunActivitiesOutput:
    out: ListDataSourceRunActivitiesOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.data_source_run_activities

        out["items"] = capo_datazone.types.data_source_run_activities.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListDataSourceRunActivitiesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_datazone.types.data_source_run_activities

        out["items"] = capo_datazone.types.data_source_run_activities.redact_sensitive(
            value["items"]
        )
    return out
