"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListSessionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.session_summary_list


class ListSessionsResponse(TypedDict, closed=True):
    sessions: "capo_workspaces_web.types.session_summary_list.SessionSummaryList"
    """<p>The sessions in a list.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponse) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.session_summary_list

    out["sessions"] = capo_workspaces_web.types.session_summary_list.serialize_json(
        value["sessions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionsResponse:
    out: ListSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessions") is not None:
        import capo_workspaces_web.types.session_summary_list

        out["sessions"] = (
            capo_workspaces_web.types.session_summary_list.deserialize_json(
                data["sessions"]
            )
        )
    else:
        out["sessions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSessionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sessions" in value:
        import capo_workspaces_web.types.session_summary_list

        out["sessions"] = (
            capo_workspaces_web.types.session_summary_list.redact_sensitive(
                value["sessions"]
            )
        )
    return out
