"""Generated from Smithy shape ``com.amazonaws.datazone#RejectSubscriptionRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.decision_comment
    import capo_datazone.types.domain_id
    import capo_datazone.types.subscription_request_id


class RejectSubscriptionRequestInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the subscription request was rejected.</p>"""
    identifier: "capo_datazone.types.subscription_request_id.SubscriptionRequestId"
    """<p>The identifier of the subscription request that was rejected.</p>"""
    decision_comment: NotRequired[
        "capo_datazone.types.decision_comment.DecisionComment"
    ]
    """<p>The decision comment of the rejected subscription request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectSubscriptionRequestInput) -> dict:
    out: dict = {}
    if "decision_comment" in value:
        out["decisionComment"] = value["decision_comment"]
    return out


def deserialize_json(data: dict) -> RejectSubscriptionRequestInput:
    out: RejectSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("decisionComment") is not None:
        out["decision_comment"] = data["decisionComment"]
    return out


def redact_sensitive(value: RejectSubscriptionRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "decision_comment" in value:
        out["decision_comment"] = "*** Sensitive Data Redacted ***"
    return out
