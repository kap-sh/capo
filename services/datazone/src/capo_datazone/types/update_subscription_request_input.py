"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateSubscriptionRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.request_reason
    import capo_datazone.types.subscription_request_id


class UpdateSubscriptionRequestInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a subscription request is to be updated.</p>"""
    identifier: "capo_datazone.types.subscription_request_id.SubscriptionRequestId"
    """<p>The identifier of the subscription request that is to be updated.</p>"""
    request_reason: "capo_datazone.types.request_reason.RequestReason"
    """<p>The reason for the <code>UpdateSubscriptionRequest</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionRequestInput) -> dict:
    out: dict = {}
    out["requestReason"] = value["request_reason"]
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionRequestInput:
    out: UpdateSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("requestReason") is not None:
        out["request_reason"] = data["requestReason"]
    else:
        out["request_reason"] = ""
    return out


def redact_sensitive(value: UpdateSubscriptionRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_reason" in value:
        out["request_reason"] = "*** Sensitive Data Redacted ***"
    return out
