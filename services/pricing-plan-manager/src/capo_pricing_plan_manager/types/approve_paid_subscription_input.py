"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ApprovePaidSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.idempotency_token
    import capo_pricing_plan_manager.types.subscription_arn


class ApprovePaidSubscriptionInput(TypedDict, closed=True):
    arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn"
    """<p>The ARN of the subscription to approve.</p>"""
    if_match: "str"
    """<p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response. This ensures you are approving the expected version of the subscription.</p>"""
    client_token: NotRequired[
        "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovePaidSubscriptionInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ApprovePaidSubscriptionInput:
    out: ApprovePaidSubscriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ApprovePaidSubscriptionInput.arn required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
