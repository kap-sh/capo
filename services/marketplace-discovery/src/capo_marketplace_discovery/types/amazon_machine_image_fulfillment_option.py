"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_discovery.types.amazon_machine_image_ebs_volume
    import capo_marketplace_discovery.types.amazon_machine_image_operating_system_list
    import capo_marketplace_discovery.types.amazon_machine_image_recommendation
    import capo_marketplace_discovery.types.fulfillment_option_type


class AmazonMachineImageFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_name: "str"
    """<p>The display name of the fulfillment option version.</p>"""
    fulfillment_option_version: NotRequired["str"]
    """<p>The version identifier of the fulfillment option.</p>"""
    fulfillment_option_type: (
        "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    )
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    operating_systems: "capo_marketplace_discovery.types.amazon_machine_image_operating_system_list.AmazonMachineImageOperatingSystemList"
    """<p>The operating systems supported by this AMI.</p>"""
    recommendation: NotRequired[
        "capo_marketplace_discovery.types.amazon_machine_image_recommendation.AmazonMachineImageRecommendation"
    ]
    """<p>Recommended instance types for running this AMI.</p>"""
    release_notes: NotRequired["str"]
    """<p>Release notes describing changes in this version of the fulfillment option.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to deploy and use this fulfillment option.</p>"""
    available_from_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the AMI became available for fulfillment.</p>"""
    access_url_template: NotRequired["str"]
    """<p>The URL pattern for accessing the product when an instance is running.</p>"""
    architecture: "str"
    """<p>The architecture of the AMI, such as <code>x86_64</code>.</p>"""
    ami_alias: NotRequired["str"]
    """<p>The alias of the AMI associated with this fulfillment option.</p>"""
    ebs_volume: NotRequired[
        "capo_marketplace_discovery.types.amazon_machine_image_ebs_volume.AmazonMachineImageEbsVolume"
    ]
    """<p>The supported Amazon EBS volume configuration for the AMI.</p>"""
    short_description: NotRequired["str"]
    """<p>A short description of the fulfillment option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    out["fulfillmentOptionName"] = value["fulfillment_option_name"]
    if "fulfillment_option_version" in value:
        out["fulfillmentOptionVersion"] = value["fulfillment_option_version"]
    import capo_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        capo_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    import capo_marketplace_discovery.types.amazon_machine_image_operating_system_list

    out["operatingSystems"] = (
        capo_marketplace_discovery.types.amazon_machine_image_operating_system_list.serialize_json(
            value["operating_systems"]
        )
    )
    if "recommendation" in value:
        import capo_marketplace_discovery.types.amazon_machine_image_recommendation

        out["recommendation"] = (
            capo_marketplace_discovery.types.amazon_machine_image_recommendation.serialize_json(
                value["recommendation"]
            )
        )
    if "release_notes" in value:
        out["releaseNotes"] = value["release_notes"]
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    if "available_from_time" in value:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["availableFromTime"] = (
            capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
                value["available_from_time"]
            )
        )
    if "access_url_template" in value:
        out["accessUrlTemplate"] = value["access_url_template"]
    out["architecture"] = value["architecture"]
    if "ami_alias" in value:
        out["amiAlias"] = value["ami_alias"]
    if "ebs_volume" in value:
        import capo_marketplace_discovery.types.amazon_machine_image_ebs_volume

        out["ebsVolume"] = (
            capo_marketplace_discovery.types.amazon_machine_image_ebs_volume.serialize_json(
                value["ebs_volume"]
            )
        )
    if "short_description" in value:
        out["shortDescription"] = value["short_description"]
    return out


def deserialize_json(data: dict) -> AmazonMachineImageFulfillmentOption:
    out: AmazonMachineImageFulfillmentOption = {}  # type: ignore[typeddict-item]
    if data.get("fulfillmentOptionId") is not None:
        out["fulfillment_option_id"] = data["fulfillmentOptionId"]
    else:
        out["fulfillment_option_id"] = ""
    if data.get("fulfillmentOptionName") is not None:
        out["fulfillment_option_name"] = data["fulfillmentOptionName"]
    else:
        out["fulfillment_option_name"] = ""
    if data.get("fulfillmentOptionVersion") is not None:
        out["fulfillment_option_version"] = data["fulfillmentOptionVersion"]
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
    if data.get("operatingSystems") is not None:
        import capo_marketplace_discovery.types.amazon_machine_image_operating_system_list

        out["operating_systems"] = (
            capo_marketplace_discovery.types.amazon_machine_image_operating_system_list.deserialize_json(
                data["operatingSystems"]
            )
        )
    else:
        out["operating_systems"] = []
    if data.get("recommendation") is not None:
        import capo_marketplace_discovery.types.amazon_machine_image_recommendation

        out["recommendation"] = (
            capo_marketplace_discovery.types.amazon_machine_image_recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    if data.get("releaseNotes") is not None:
        out["release_notes"] = data["releaseNotes"]
    if data.get("usageInstructions") is not None:
        out["usage_instructions"] = data["usageInstructions"]
    if data.get("availableFromTime") is not None:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["available_from_time"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["availableFromTime"]
            )
        )
    if data.get("accessUrlTemplate") is not None:
        out["access_url_template"] = data["accessUrlTemplate"]
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    else:
        out["architecture"] = ""
    if data.get("amiAlias") is not None:
        out["ami_alias"] = data["amiAlias"]
    if data.get("ebsVolume") is not None:
        import capo_marketplace_discovery.types.amazon_machine_image_ebs_volume

        out["ebs_volume"] = (
            capo_marketplace_discovery.types.amazon_machine_image_ebs_volume.deserialize_json(
                data["ebsVolume"]
            )
        )
    if data.get("shortDescription") is not None:
        out["short_description"] = data["shortDescription"]
    return out
