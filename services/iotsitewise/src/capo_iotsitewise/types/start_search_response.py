"""Generated from Smithy shape ``com.amazonaws.iotsitewise#StartSearchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.group_id
    import capo_iotsitewise.types.search_id
    import capo_iotsitewise.types.search_status
    import capo_iotsitewise.types.workspace_name


class StartSearchResponse(TypedDict, closed=True):
    search_id: "capo_iotsitewise.types.search_id.SearchId"
    """<p>The unique identifier assigned to the newly started search.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace the search runs against.</p>"""
    status: "capo_iotsitewise.types.search_status.SearchStatus"
    """<p>The initial status of the search. A newly started search is <code>QUEUED</code>.</p>"""
    group_id: NotRequired["capo_iotsitewise.types.group_id.GroupId"]
    """<p>The group identifier associated with the search, if one was supplied on the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSearchResponse) -> dict:
    out: dict = {}
    out["searchId"] = value["search_id"]
    out["workspaceName"] = value["workspace_name"]
    import capo_iotsitewise.types.search_status

    out["status"] = capo_iotsitewise.types.search_status.serialize_json(value["status"])
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> StartSearchResponse:
    out: StartSearchResponse = {}  # type: ignore[typeddict-item]
    if data.get("searchId") is not None:
        out["search_id"] = data["searchId"]
    else:
        out["search_id"] = ""
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.search_status

        out["status"] = capo_iotsitewise.types.search_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iotsitewise.types.search_status.SearchStatus", ""
        )
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    return out
