"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#GetSubscriptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.subscription_arn


class GetSubscriptionInput(TypedDict, closed=True):
    arn: "capo_pricing_plan_manager.types.subscription_arn.SubscriptionArn"
    """<p>The ARN of the subscription to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetSubscriptionInput:
    out: GetSubscriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSubscriptionInput.arn required")
    return out
