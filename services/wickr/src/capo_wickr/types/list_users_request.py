"""Generated from Smithy shape ``com.amazonaws.wickr#ListUsersRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.sensitive_string
    import capo_wickr.types.sort_direction
    import capo_wickr.types.user_status


class ListUsersRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which to list users.</p>"""
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token for retrieving the next page of results. This is returned from a previous request when there are more results available.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of users to return in a single page. Valid range is 1-100. Default is 10.</p>"""
    sort_fields: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The fields to sort users by. Multiple fields can be specified by separating them with '+'. Accepted values include 'username', 'firstName', 'lastName', 'status', and 'groupId'.</p>"""
    sort_direction: NotRequired["capo_wickr.types.sort_direction.SortDirection"]
    """<p>The direction to sort results. Valid values are 'ASC' (ascending) or 'DESC' (descending). Default is 'DESC'.</p>"""
    first_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>Filter results to only include users with first names matching this value.</p>"""
    last_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>Filter results to only include users with last names matching this value.</p>"""
    username: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include users with usernames matching this value.</p>"""
    status: NotRequired["capo_wickr.types.user_status.UserStatus"]
    """<p>Filter results to only include users with this status (1 for pending, 2 for active).</p>"""
    group_id: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>Filter results to only include users belonging to this security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUsersRequest:
    out: ListUsersRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListUsersRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
