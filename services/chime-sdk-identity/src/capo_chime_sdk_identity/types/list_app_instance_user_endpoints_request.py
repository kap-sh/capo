"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceUserEndpointsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.max_results
    import capo_chime_sdk_identity.types.next_token
    import capo_chime_sdk_identity.types.sensitive_chime_arn


class ListAppInstanceUserEndpointsRequest(TypedDict, closed=True):
    app_instance_user_arn: (
        "capo_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn"
    )
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    max_results: NotRequired["capo_chime_sdk_identity.types.max_results.MaxResults"]
    """<p>The maximum number of endpoints that you want to return.</p>"""
    next_token: NotRequired["capo_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested endpoints are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceUserEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppInstanceUserEndpointsRequest:
    out: ListAppInstanceUserEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListAppInstanceUserEndpointsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_user_arn" in value:
        out["app_instance_user_arn"] = "*** Sensitive Data Redacted ***"
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
