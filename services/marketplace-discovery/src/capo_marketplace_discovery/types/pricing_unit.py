"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingUnit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.pricing_unit_type


class PricingUnit(TypedDict, closed=True):
    pricing_unit_type: (
        "capo_marketplace_discovery.types.pricing_unit_type.PricingUnitType"
    )
    """<p>The machine-readable type of the pricing unit.</p>"""
    display_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the pricing unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingUnit) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.pricing_unit_type

    out["pricingUnitType"] = (
        capo_marketplace_discovery.types.pricing_unit_type.serialize_json(
            value["pricing_unit_type"]
        )
    )
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> PricingUnit:
    out: PricingUnit = {}  # type: ignore[typeddict-item]
    if data.get("pricingUnitType") is not None:
        import capo_marketplace_discovery.types.pricing_unit_type

        out["pricing_unit_type"] = (
            capo_marketplace_discovery.types.pricing_unit_type.deserialize_json(
                data["pricingUnitType"]
            )
        )
    else:
        import typing

        out["pricing_unit_type"] = typing.cast(
            "capo_marketplace_discovery.types.pricing_unit_type.PricingUnitType", ""
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    return out
