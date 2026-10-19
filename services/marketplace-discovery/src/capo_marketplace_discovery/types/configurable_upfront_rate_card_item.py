"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ConfigurableUpfrontRateCardItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.constraints
    import capo_marketplace_discovery.types.rate_card_list
    import capo_marketplace_discovery.types.selector


class ConfigurableUpfrontRateCardItem(TypedDict, closed=True):
    selector: "capo_marketplace_discovery.types.selector.Selector"
    """<p>The selector criteria for this rate card, such as duration.</p>"""
    constraints: "capo_marketplace_discovery.types.constraints.Constraints"
    """<p>Constraints on how the buyer can configure this rate card, such as whether multiple dimensions can be selected.</p>"""
    rate_card: "capo_marketplace_discovery.types.rate_card_list.RateCardList"
    """<p>The per-unit rates for this configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableUpfrontRateCardItem) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.selector

    out["selector"] = capo_marketplace_discovery.types.selector.serialize_json(
        value["selector"]
    )
    import capo_marketplace_discovery.types.constraints

    out["constraints"] = capo_marketplace_discovery.types.constraints.serialize_json(
        value["constraints"]
    )
    import capo_marketplace_discovery.types.rate_card_list

    out["rateCard"] = capo_marketplace_discovery.types.rate_card_list.serialize_json(
        value["rate_card"]
    )
    return out


def deserialize_json(data: dict) -> ConfigurableUpfrontRateCardItem:
    out: ConfigurableUpfrontRateCardItem = {}  # type: ignore[typeddict-item]
    if data.get("selector") is not None:
        import capo_marketplace_discovery.types.selector

        out["selector"] = capo_marketplace_discovery.types.selector.deserialize_json(
            data["selector"]
        )
    else:
        raise DeserializationError("ConfigurableUpfrontRateCardItem.selector required")
    if data.get("constraints") is not None:
        import capo_marketplace_discovery.types.constraints

        out["constraints"] = (
            capo_marketplace_discovery.types.constraints.deserialize_json(
                data["constraints"]
            )
        )
    else:
        raise DeserializationError(
            "ConfigurableUpfrontRateCardItem.constraints required"
        )
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
