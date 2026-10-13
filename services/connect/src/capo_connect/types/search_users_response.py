"""Generated from Smithy shape ``com.amazonaws.connect#SearchUsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500
    import capo_connect.types.user_search_summary_list


class SearchUsersResponse(TypedDict, closed=True):
    users: NotRequired[
        "capo_connect.types.user_search_summary_list.UserSearchSummaryList"
    ]
    """<p>Information about the users.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of users who matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_connect.types.user_search_summary_list

        out["Users"] = capo_connect.types.user_search_summary_list.serialize_json(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchUsersResponse:
    out: SearchUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_connect.types.user_search_summary_list

        out["users"] = capo_connect.types.user_search_summary_list.deserialize_json(
            data["Users"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ApproximateTotalCount") is not None:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out


def redact_sensitive(value: SearchUsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_connect.types.user_search_summary_list

        out["users"] = capo_connect.types.user_search_summary_list.redact_sensitive(
            value["users"]
        )
    return out
