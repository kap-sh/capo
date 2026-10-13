"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeActivitiesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.search_marker_type
    import capo_workdocs.types.user_activities


class DescribeActivitiesResponse(TypedDict, closed=True):
    user_activities: NotRequired["capo_workdocs.types.user_activities.UserActivities"]
    """<p>The list of activities for the specified user and time period.</p>"""
    marker: NotRequired["capo_workdocs.types.search_marker_type.SearchMarkerType"]
    """<p>The marker for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActivitiesResponse) -> dict:
    out: dict = {}
    if "user_activities" in value:
        import capo_workdocs.types.user_activities

        out["UserActivities"] = capo_workdocs.types.user_activities.serialize_json(
            value["user_activities"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeActivitiesResponse:
    out: DescribeActivitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("UserActivities") is not None:
        import capo_workdocs.types.user_activities

        out["user_activities"] = capo_workdocs.types.user_activities.deserialize_json(
            data["UserActivities"]
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out


def redact_sensitive(value: DescribeActivitiesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_activities" in value:
        import capo_workdocs.types.user_activities

        out["user_activities"] = capo_workdocs.types.user_activities.redact_sensitive(
            value["user_activities"]
        )
    return out
