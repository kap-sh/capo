"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListDevEnvironmentSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.dev_environment_sessions_summary_list


class ListDevEnvironmentSessionsResponse(TypedDict, closed=True):
    items: "capo_codecatalyst.types.dev_environment_sessions_summary_list.DevEnvironmentSessionsSummaryList"
    """<p>Information about each session retrieved in the list.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevEnvironmentSessionsResponse) -> dict:
    out: dict = {}
    import capo_codecatalyst.types.dev_environment_sessions_summary_list

    out["items"] = (
        capo_codecatalyst.types.dev_environment_sessions_summary_list.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDevEnvironmentSessionsResponse:
    out: ListDevEnvironmentSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_codecatalyst.types.dev_environment_sessions_summary_list

        out["items"] = (
            capo_codecatalyst.types.dev_environment_sessions_summary_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
