"""Generated from Smithy shape ``com.amazonaws.billingconductor#AutoTransferBillingGroupCreationPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_plan_arn


class AutoTransferBillingGroupCreationPreference(TypedDict, closed=True):
    enabled: "bool"
    """<p> Specifies whether Billing Conductor automatically creates billing groups for the billing transfer. The preference is disabled by default. </p>"""
    pricing_plan_arn: NotRequired[
        "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the pricing plan to apply to the automatically created billing groups. This value is required when <code>Enabled</code> is <code>true</code>, and must be omitted when <code>Enabled</code> is <code>false</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTransferBillingGroupCreationPreference) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "pricing_plan_arn" in value:
        out["PricingPlanArn"] = value["pricing_plan_arn"]
    return out


def deserialize_json(data: dict) -> AutoTransferBillingGroupCreationPreference:
    out: AutoTransferBillingGroupCreationPreference = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("PricingPlanArn") is not None:
        out["pricing_plan_arn"] = data["PricingPlanArn"]
    return out
