"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FulfillmentOptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.fulfillment_option_type
    import capo_marketplace_discovery.types.non_empty_string


class FulfillmentOptionSummary(TypedDict, closed=True):
    fulfillment_option_type: (
        "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    )
    """<p>The machine-readable type of the fulfillment option, such as <code>SAAS</code> or <code>AMAZON_MACHINE_IMAGE</code>.</p>"""
    display_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the fulfillment option type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentOptionSummary) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        capo_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> FulfillmentOptionSummary:
    out: FulfillmentOptionSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    return out
