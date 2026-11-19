"""Generated from Smithy shape ``com.amazonaws.mgn#ListRemoteSourceActionJobsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.pagination_token
    import capo_mgn.types.remote_source_action_jobs_list


class ListRemoteSourceActionJobsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.remote_source_action_jobs_list.RemoteSourceActionJobsList"
    ]
    """<p>A list of source action jobs.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRemoteSourceActionJobsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.remote_source_action_jobs_list

        out["items"] = capo_mgn.types.remote_source_action_jobs_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRemoteSourceActionJobsResponse:
    out: ListRemoteSourceActionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.remote_source_action_jobs_list

        out["items"] = capo_mgn.types.remote_source_action_jobs_list.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListRemoteSourceActionJobsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_mgn.types.remote_source_action_jobs_list

        out["items"] = capo_mgn.types.remote_source_action_jobs_list.redact_sensitive(
            value["items"]
        )
    return out
