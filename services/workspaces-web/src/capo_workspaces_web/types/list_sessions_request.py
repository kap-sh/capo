"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListSessionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.max_results
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.portal_id
    import capo_workspaces_web.types.session_id
    import capo_workspaces_web.types.session_sort_by
    import capo_workspaces_web.types.session_status
    import capo_workspaces_web.types.username


class ListSessionsRequest(TypedDict, closed=True):
    portal_id: "capo_workspaces_web.types.portal_id.PortalId"
    """<p>The ID of the web portal for the sessions.</p>"""
    username: NotRequired["capo_workspaces_web.types.username.Username"]
    """<p>The username of the session.</p>"""
    session_id: NotRequired["capo_workspaces_web.types.session_id.SessionId"]
    """<p>The ID of the session.</p>"""
    sort_by: NotRequired["capo_workspaces_web.types.session_sort_by.SessionSortBy"]
    """<p>The method in which the returned sessions should be sorted.</p>"""
    status: NotRequired["capo_workspaces_web.types.session_status.SessionStatus"]
    """<p>The status of the session.</p>"""
    max_results: NotRequired["capo_workspaces_web.types.max_results.MaxResults"]
    """<p>The maximum number of results to be included in the next page.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSessionsRequest:
    out: ListSessionsRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListSessionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
