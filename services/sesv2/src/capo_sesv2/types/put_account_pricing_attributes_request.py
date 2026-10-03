"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountPricingAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.pricing_plan


class PutAccountPricingAttributesRequest(TypedDict, closed=True):
    plan: "capo_sesv2.types.pricing_plan.PricingPlan"
    """<p>The pricing plan to apply to your Amazon SES account. For details about each plan, see <a href="http://aws.amazon.com/ses/pricing/">Amazon SES Pricing</a>. Can be one of the following:</p> <ul> <li> <p> <code>NONE</code> </p> </li> <li> <p> <code>ESSENTIALS</code> </p> </li> <li> <p> <code>PRO</code> </p> </li> <li> <p> <code>ENTERPRISE</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountPricingAttributesRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.pricing_plan

    out["Plan"] = capo_sesv2.types.pricing_plan.serialize_json(value["plan"])
    return out


def deserialize_json(data: dict) -> PutAccountPricingAttributesRequest:
    out: PutAccountPricingAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Plan") is not None:
        import capo_sesv2.types.pricing_plan

        out["plan"] = capo_sesv2.types.pricing_plan.deserialize_json(data["Plan"])
    else:
        raise DeserializationError("PutAccountPricingAttributesRequest.plan required")
    return out
