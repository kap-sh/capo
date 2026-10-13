"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListSessionLoggersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.session_logger_list


class ListSessionLoggersResponse(TypedDict, closed=True):
    session_loggers: NotRequired[
        "capo_workspaces_web.types.session_logger_list.SessionLoggerList"
    ]
    """<p>The list of session loggers, including summaries of their details.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionLoggersResponse) -> dict:
    out: dict = {}
    if "session_loggers" in value:
        import capo_workspaces_web.types.session_logger_list

        out["sessionLoggers"] = (
            capo_workspaces_web.types.session_logger_list.serialize_json(
                value["session_loggers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionLoggersResponse:
    out: ListSessionLoggersResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionLoggers") is not None:
        import capo_workspaces_web.types.session_logger_list

        out["session_loggers"] = (
            capo_workspaces_web.types.session_logger_list.deserialize_json(
                data["sessionLoggers"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSessionLoggersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session_loggers" in value:
        import capo_workspaces_web.types.session_logger_list

        out["session_loggers"] = (
            capo_workspaces_web.types.session_logger_list.redact_sensitive(
                value["session_loggers"]
            )
        )
    return out
