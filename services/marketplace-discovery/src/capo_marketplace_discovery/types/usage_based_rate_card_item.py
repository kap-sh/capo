"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UsageBasedRateCardItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.rate_card_list


class UsageBasedRateCardItem(TypedDict, closed=True):
    rate_card: "capo_marketplace_discovery.types.rate_card_list.RateCardList"
    """<p>The per-unit rates for this usage-based rate card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageBasedRateCardItem) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.rate_card_list

    out["rateCard"] = capo_marketplace_discovery.types.rate_card_list.serialize_json(
        value["rate_card"]
    )
    return out


def deserialize_json(data: dict) -> UsageBasedRateCardItem:
    out: UsageBasedRateCardItem = {}  # type: ignore[typeddict-item]
    if data.get("rateCard") is not None:
        import capo_marketplace_discovery.types.rate_card_list

        out["rate_card"] = (
            capo_marketplace_discovery.types.rate_card_list.deserialize_json(
                data["rateCard"]
            )
        )
    else:
        out["rate_card"] = []
    return out
