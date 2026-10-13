"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelsModeratedByAppInstanceUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.max_results
    import capo_chime_sdk_messaging.types.next_token


class ListChannelsModeratedByAppInstanceUserRequest(TypedDict, closed=True):
    app_instance_user_arn: NotRequired[
        "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the user or bot in the moderated channel.</p>"""
    max_results: NotRequired["capo_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of channels in the request.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token returned from previous API requests until the number of channels moderated by the user is reached.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsModeratedByAppInstanceUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelsModeratedByAppInstanceUserRequest:
    out: ListChannelsModeratedByAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(
    value: ListChannelsModeratedByAppInstanceUserRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
