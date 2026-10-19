"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingModel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.pricing_model_type


class PricingModel(TypedDict, closed=True):
    pricing_model_type: (
        "capo_marketplace_discovery.types.pricing_model_type.PricingModelType"
    )
    """<p>The machine-readable type of the pricing model.</p>"""
    display_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the pricing model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingModel) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.pricing_model_type

    out["pricingModelType"] = (
        capo_marketplace_discovery.types.pricing_model_type.serialize_json(
            value["pricing_model_type"]
        )
    )
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> PricingModel:
    out: PricingModel = {}  # type: ignore[typeddict-item]
    if data.get("pricingModelType") is not None:
        import capo_marketplace_discovery.types.pricing_model_type

        out["pricing_model_type"] = (
            capo_marketplace_discovery.types.pricing_model_type.deserialize_json(
                data["pricingModelType"]
            )
        )
    else:
        import typing

        out["pricing_model_type"] = typing.cast(
            "capo_marketplace_discovery.types.pricing_model_type.PricingModelType", ""
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    return out
