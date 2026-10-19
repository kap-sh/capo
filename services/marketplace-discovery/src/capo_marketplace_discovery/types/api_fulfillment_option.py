"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ApiFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.aws_supported_service_list
    import capo_marketplace_discovery.types.fulfillment_option_type


class ApiFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: (
        "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    )
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to integrate with and use this API.</p>"""
    aws_supported_services: "capo_marketplace_discovery.types.aws_supported_service_list.AwsSupportedServiceList"
    """<p>The AWS services supported by this API integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import capo_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        capo_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    import capo_marketplace_discovery.types.aws_supported_service_list

    out["awsSupportedServices"] = (
        capo_marketplace_discovery.types.aws_supported_service_list.serialize_json(
            value["aws_supported_services"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApiFulfillmentOption:
    out: ApiFulfillmentOption = {}  # type: ignore[typeddict-item]
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
    if data.get("usageInstructions") is not None:
        out["usage_instructions"] = data["usageInstructions"]
    if data.get("awsSupportedServices") is not None:
        import capo_marketplace_discovery.types.aws_supported_service_list

        out["aws_supported_services"] = (
            capo_marketplace_discovery.types.aws_supported_service_list.deserialize_json(
                data["awsSupportedServices"]
            )
        )
    else:
        out["aws_supported_services"] = []
    return out
