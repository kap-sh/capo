"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeActivitiesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.activity_names_filter_type
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.limit_type
    import capo_workdocs.types.search_marker_type
    import capo_workdocs.types.timestamp_type


class DescribeActivitiesRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    start_time: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The timestamp that determines the starting time of the activities. The response includes the activities performed after the specified timestamp.</p>"""
    end_time: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The timestamp that determines the end time of the activities. The response includes the activities performed before the specified timestamp.</p>"""
    organization_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization. This is a mandatory parameter when using administrative API (SigV4) requests.</p>"""
    activity_types: NotRequired[
        "capo_workdocs.types.activity_names_filter_type.ActivityNamesFilterType"
    ]
    """<p>Specifies which activity types to include in the response. If this field is left empty, all activity types are returned.</p>"""
    resource_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The document or folder ID for which to describe activity types.</p>"""
    user_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the user who performed the action. The response includes activities pertaining to this user. This is an optional parameter and is only applicable for administrative API (SigV4) requests.</p>"""
    include_indirect_activities: "capo_workdocs.types.boolean_type.BooleanType"
    """<p>Includes indirect activities. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).</p>"""
    limit: NotRequired["capo_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of items to return.</p>"""
    marker: NotRequired["capo_workdocs.types.search_marker_type.SearchMarkerType"]
    """<p>The marker for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActivitiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeActivitiesRequest:
    out: DescribeActivitiesRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DescribeActivitiesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
