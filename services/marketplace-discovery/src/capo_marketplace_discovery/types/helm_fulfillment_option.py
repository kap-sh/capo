"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#HelmFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.aws_supported_service_list
    import capo_marketplace_discovery.types.fulfillment_option_type
    import capo_marketplace_discovery.types.helm_operating_system_list


class HelmFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_name: "str"
    """<p>The display name of the fulfillment option version.</p>"""
    fulfillment_option_type: (
        "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    )
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    fulfillment_option_version: NotRequired["str"]
    """<p>The version identifier of the fulfillment option.</p>"""
    operating_systems: NotRequired[
        "capo_marketplace_discovery.types.helm_operating_system_list.HelmOperatingSystemList"
    ]
    """<p>The operating systems supported by this Helm chart.</p>"""
    release_notes: NotRequired["str"]
    """<p>Release notes describing changes in this version of the fulfillment option.</p>"""
    aws_supported_services: NotRequired[
        "capo_marketplace_discovery.types.aws_supported_service_list.AwsSupportedServiceList"
    ]
    """<p>The AWS services supported by this Helm chart deployment.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to deploy and use this Helm chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HelmFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    out["fulfillmentOptionName"] = value["fulfillment_option_name"]
    import capo_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        capo_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "fulfillment_option_version" in value:
        out["fulfillmentOptionVersion"] = value["fulfillment_option_version"]
    if "operating_systems" in value:
        import capo_marketplace_discovery.types.helm_operating_system_list

        out["operatingSystems"] = (
            capo_marketplace_discovery.types.helm_operating_system_list.serialize_json(
                value["operating_systems"]
            )
        )
    if "release_notes" in value:
        out["releaseNotes"] = value["release_notes"]
    if "aws_supported_services" in value:
        import capo_marketplace_discovery.types.aws_supported_service_list

        out["awsSupportedServices"] = (
            capo_marketplace_discovery.types.aws_supported_service_list.serialize_json(
                value["aws_supported_services"]
            )
        )
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    return out


def deserialize_json(data: dict) -> HelmFulfillmentOption:
    out: HelmFulfillmentOption = {}  # type: ignore[typeddict-item]
    if data.get("fulfillmentOptionId") is not None:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        out["fulfillment_option_id"] = ""
    if data.get("fulfillmentOptionName") is not None:
        out["fulfillment_option_name"] = data["fulfillmentOptionName"]
    else:
        out["fulfillment_option_name"] = ""
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
    if data.get("fulfillmentOptionVersion") is not None:
        out["fulfillment_option_version"] = data["fulfillmentOptionVersion"]
    if data.get("operatingSystems") is not None:
        import capo_marketplace_discovery.types.helm_operating_system_list

        out["operating_systems"] = (
            capo_marketplace_discovery.types.helm_operating_system_list.deserialize_json(
                data["operatingSystems"]
            )
        )
    if data.get("releaseNotes") is not None:
        out["release_notes"] = data["releaseNotes"]
    if data.get("awsSupportedServices") is not None:
        import capo_marketplace_discovery.types.aws_supported_service_list

        out["aws_supported_services"] = (
            capo_marketplace_discovery.types.aws_supported_service_list.deserialize_json(
                data["awsSupportedServices"]
            )
        )
    if data.get("usageInstructions") is not None:
        out["usage_instructions"] = data["usageInstructions"]
    return out
