"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#CancelSubscriptionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.subscription


class CancelSubscriptionOutput(TypedDict, closed=True):
    subscription: "capo_pricing_plan_manager.types.subscription.Subscription"
    """<p>The details of the subscription with the pending cancellation. For active subscriptions, a <code>scheduledChange</code> of type <code>CANCELLATION</code> is included.</p>"""
    e_tag: "str"
    """<p>The updated entity tag for concurrency control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelSubscriptionOutput) -> dict:
    out: dict = {}
    import capo_pricing_plan_manager.types.subscription

    out["subscription"] = capo_pricing_plan_manager.types.subscription.serialize_json(
        value["subscription"]
    )
    return out


def deserialize_json(data: dict) -> CancelSubscriptionOutput:
    out: CancelSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if data.get("subscription") is not None:
        import capo_pricing_plan_manager.types.subscription

        out["subscription"] = (
            capo_pricing_plan_manager.types.subscription.deserialize_json(
                data["subscription"]
            )
        )
    else:
        raise DeserializationError("CancelSubscriptionOutput.subscription required")
    return out
