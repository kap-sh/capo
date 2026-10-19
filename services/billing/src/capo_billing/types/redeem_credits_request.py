"""Generated from Smithy shape ``com.amazonaws.billing#RedeemCreditsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.promo_code


class RedeemCreditsRequest(TypedDict, closed=True):
    promo_code: "capo_billing.types.promo_code.PromoCode"
    """<p>The promotional credit code to redeem.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RedeemCreditsRequest) -> dict:
    out: dict = {}
    out["promoCode"] = value["promo_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RedeemCreditsRequest:
    out: RedeemCreditsRequest = {}  # type: ignore[typeddict-item]
    if data.get("promoCode") is not None:
        out["promo_code"] = data["promoCode"]
    else:
        out["promo_code"] = ""
    return out
