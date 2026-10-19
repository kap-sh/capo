"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SaasFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_discovery.types.fulfillment_option_type
    import capo_marketplace_discovery.types.saas_quick_launch_status
    import capo_marketplace_discovery.types.url


class SaasFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: (
        "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    )
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    fulfillment_url: NotRequired["str"]
    """<p>The URL of the seller's software registration landing page.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to access and use this SaaS product.</p>"""
    available_from_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the SaaS product became available for fulfillment.</p>"""
    launch_url: NotRequired["capo_marketplace_discovery.types.url.URL"]
    """<p>The URL that a buyer uses to launch the seller's SaaS product. This URL is distinct from <code>fulfillmentUrl</code>, which is the seller's software registration landing page.</p>"""
    quick_launch: "capo_marketplace_discovery.types.saas_quick_launch_status.SaasQuickLaunchStatus"
    """<p>Specifies whether the SaaS product supports quick-launch deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaasFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import capo_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        capo_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "fulfillment_url" in value:
        out["fulfillmentUrl"] = value["fulfillment_url"]
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    if "available_from_time" in value:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["availableFromTime"] = (
            capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["available_from_time"]
            )
        )
    if "launch_url" in value:
        out["launchUrl"] = value["launch_url"]
    import capo_marketplace_discovery.types.saas_quick_launch_status

    out["quickLaunch"] = (
        capo_marketplace_discovery.types.saas_quick_launch_status.serialize_json(
            value["quick_launch"]
        )
    )
    return out


def deserialize_json(data: dict) -> SaasFulfillmentOption:
    out: SaasFulfillmentOption = {}  # type: ignore[typeddict-item]
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
    if data.get("fulfillmentUrl") is not None:
        out["fulfillment_url"] = data["fulfillmentUrl"]
    if data.get("usageInstructions") is not None:
        out["usage_instructions"] = data["usageInstructions"]
    if data.get("availableFromTime") is not None:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["available_from_time"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["availableFromTime"]
            )
        )
    if data.get("launchUrl") is not None:
        out["launch_url"] = data["launchUrl"]
    if data.get("quickLaunch") is not None:
        import capo_marketplace_discovery.types.saas_quick_launch_status

        out["quick_launch"] = (
            capo_marketplace_discovery.types.saas_quick_launch_status.deserialize_json(
                data["quickLaunch"]
            )
        )
    else:
        import typing

        out["quick_launch"] = typing.cast(
            "capo_marketplace_discovery.types.saas_quick_launch_status.SaasQuickLaunchStatus",
            "",
        )
    return out
