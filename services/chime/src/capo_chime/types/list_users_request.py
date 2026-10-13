"""Generated from Smithy shape ``com.amazonaws.chime#ListUsersRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.email_address
    import capo_chime.types.non_empty_string
    import capo_chime.types.profile_service_max_results
    import capo_chime.types.string
    import capo_chime.types.user_type


class ListUsersRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    user_email: NotRequired["capo_chime.types.email_address.EmailAddress"]
    """<p>Optional. The user email address used to filter results. Maximum 1.</p>"""
    user_type: NotRequired["capo_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""
    max_results: NotRequired[
        "capo_chime.types.profile_service_max_results.ProfileServiceMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. Defaults to 100.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUsersRequest:
    out: ListUsersRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListUsersRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_email" in value:
        out["user_email"] = "*** Sensitive Data Redacted ***"
    return out
