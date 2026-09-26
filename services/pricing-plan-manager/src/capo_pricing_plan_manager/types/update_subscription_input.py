"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#UpdateSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.idempotency_token
    import capo_pricing_plan_manager.types.subscription_arn


class UpdateSubscriptionInput(TypedDict, closed=True):
    arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn"
    """<p>The ARN of the subscription to update.</p>"""
    plan_tier: "str"
    """<p>The new tier level for the subscription.</p>"""
    usage_level: NotRequired["str"]
    """<p>The usage level within the plan tier. Specify <code>DEFAULT</code> for the base configuration. If omitted, the usage level is reset to the default.</p>"""
    if_match: "str"
    """<p>The <code>ETag</code> value from a previous <code>GetSubscription</code> or <code>ListSubscriptions</code> response. This ensures you are updating the expected version of the subscription.</p>"""
    client_token: NotRequired[
        "capo_pricing_plan_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the request is handled only once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["planTier"] = value["plan_tier"]
    if "usage_level" in value:
        out["usageLevel"] = value["usage_level"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionInput:
    out: UpdateSubscriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateSubscriptionInput.arn required")
    if data.get("planTier") is not None:
        out["plan_tier"] = data["planTier"]
    else:
        raise DeserializationError("UpdateSubscriptionInput.plan_tier required")
    if data.get("usageLevel") is not None:
        out["usage_level"] = data["usageLevel"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
