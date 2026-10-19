"""Generated from Smithy shape ``com.amazonaws.bedrock#PricingTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.rate_card


class PricingTerm(TypedDict, closed=True):
    rate_card: "capo_bedrock.types.rate_card.RateCard"
    """<p>Describes a usage price for each dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingTerm) -> dict:
    out: dict = {}
    import capo_bedrock.types.rate_card

    out["rateCard"] = capo_bedrock.types.rate_card.serialize_json(value["rate_card"])
    return out


def deserialize_json(data: dict) -> PricingTerm:
    out: PricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("rateCard") is not None:
        import capo_bedrock.types.rate_card

        out["rate_card"] = capo_bedrock.types.rate_card.deserialize_json(
            data["rateCard"]
        )
    else:
        out["rate_card"] = []
    return out
