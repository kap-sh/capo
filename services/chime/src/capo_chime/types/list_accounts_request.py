"""Generated from Smithy shape ``com.amazonaws.chime#ListAccountsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.account_name
    import capo_chime.types.email_address
    import capo_chime.types.profile_service_max_results
    import capo_chime.types.string


class ListAccountsRequest(TypedDict, closed=True):
    name: NotRequired["capo_chime.types.account_name.AccountName"]
    """<p>Amazon Chime account name prefix with which to filter results.</p>"""
    user_email: NotRequired["capo_chime.types.email_address.EmailAddress"]
    """<p>User email address with which to filter results.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_chime.types.profile_service_max_results.ProfileServiceMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. Defaults to 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccountsRequest:
    out: ListAccountsRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListAccountsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_email" in value:
        out["user_email"] = "*** Sensitive Data Redacted ***"
    return out
