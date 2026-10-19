"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ProfessionalServicesFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.fulfillment_option_type


class ProfessionalServicesFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: (
        "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    )
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfessionalServicesFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import capo_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        capo_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    return out


def deserialize_json(data: dict) -> ProfessionalServicesFulfillmentOption:
    out: ProfessionalServicesFulfillmentOption = {}  # type: ignore[typeddict-item]
    if data.get("fulfillmentOptionId") is not None:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        out["fulfillment_option_id"] = ""
    if data.get("fulfillmentOptionType") is not None:
        import capo_marketplace_discovery.types.fulfillment_option_type

        out["fulfillment_option_type"] = (
            capo_marketplace_discovery.types.fulfillment_option_type.deserialize_json(
                data["fulfillmentOptionType"]
            )
        )
    else:
        import typing

        out["fulfillment_option_type"] = typing.cast(
            "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType",
            "",
        )
    if data.get("fulfillmentOptionDisplayName") is not None:
        out["fulfillment_option_display_name"] = data["fulfillmentOptionDisplayName"]
    else:
        out["fulfillment_option_display_name"] = ""
    return out
