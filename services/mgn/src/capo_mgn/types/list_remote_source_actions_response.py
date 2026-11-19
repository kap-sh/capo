"""Generated from Smithy shape ``com.amazonaws.mgn#ListRemoteSourceActionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.pagination_token
    import capo_mgn.types.remote_source_actions_list


class ListRemoteSourceActionsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.remote_source_actions_list.RemoteSourceActionsList"
    ]
    """<p>A list of source actions.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRemoteSourceActionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.remote_source_actions_list

        out["items"] = capo_mgn.types.remote_source_actions_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRemoteSourceActionsResponse:
    out: ListRemoteSourceActionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.remote_source_actions_list

        out["items"] = capo_mgn.types.remote_source_actions_list.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListRemoteSourceActionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_mgn.types.remote_source_actions_list

        out["items"] = capo_mgn.types.remote_source_actions_list.redact_sensitive(
            value["items"]
        )
    return out
