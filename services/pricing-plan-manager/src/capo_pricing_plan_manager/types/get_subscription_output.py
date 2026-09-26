"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#GetSubscriptionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.subscription


class GetSubscriptionOutput(TypedDict, closed=True):
    subscription: "capo_pricing_plan_manager.types.subscription.Subscription"
    """<p>The details of the requested subscription.</p>"""
    e_tag: "str"
    """<p>The entity tag for concurrency control. Use this value in the <code>If-Match</code> header for subsequent operations on this subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionOutput) -> dict:
    out: dict = {}
    import capo_pricing_plan_manager.types.subscription

    out["subscription"] = capo_pricing_plan_manager.types.subscription.serialize_json(
        value["subscription"]
    )
    return out


def deserialize_json(data: dict) -> GetSubscriptionOutput:
    out: GetSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if data.get("subscription") is not None:
        import capo_pricing_plan_manager.types.subscription

        out["subscription"] = (
            capo_pricing_plan_manager.types.subscription.deserialize_json(
                data["subscription"]
            )
        )
    else:
        raise DeserializationError("GetSubscriptionOutput.subscription required")
    return out
