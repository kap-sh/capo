"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceUsersRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.max_results
    import capo_chime_sdk_identity.types.next_token


class ListAppInstanceUsersRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    max_results: NotRequired["capo_chime_sdk_identity.types.max_results.MaxResults"]
    """<p>The maximum number of requests that you want returned.</p>"""
    next_token: NotRequired["capo_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested users are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppInstanceUsersRequest:
    out: ListAppInstanceUsersRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListAppInstanceUsersRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
