"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SageMakerAlgorithmFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.fulfillment_option_type
    import capo_marketplace_discovery.types.sage_maker_algorithm_recommendation


class SageMakerAlgorithmFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: (
        "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    )
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    fulfillment_option_version: NotRequired["str"]
    """<p>The version identifier of the fulfillment option.</p>"""
    release_notes: NotRequired["str"]
    """<p>Release notes describing changes in this version of the fulfillment option.</p>"""
    usage_instructions: NotRequired["str"]
    """<p>Instructions on how to use this SageMaker algorithm.</p>"""
    recommendation: NotRequired[
        "capo_marketplace_discovery.types.sage_maker_algorithm_recommendation.SageMakerAlgorithmRecommendation"
    ]
    """<p>Recommended instance types for training and inference with this algorithm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerAlgorithmFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import capo_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        capo_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "fulfillment_option_version" in value:
        out["fulfillmentOptionVersion"] = value["fulfillment_option_version"]
    if "release_notes" in value:
        out["releaseNotes"] = value["release_notes"]
    if "usage_instructions" in value:
        out["usageInstructions"] = value["usage_instructions"]
    if "recommendation" in value:
        import capo_marketplace_discovery.types.sage_maker_algorithm_recommendation

        out["recommendation"] = (
            capo_marketplace_discovery.types.sage_maker_algorithm_recommendation.serialize_json(
                value["recommendation"]
            )
        )
    return out


def deserialize_json(data: dict) -> SageMakerAlgorithmFulfillmentOption:
    out: SageMakerAlgorithmFulfillmentOption = {}  # type: ignore[typeddict-item]
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
    if data.get("fulfillmentOptionVersion") is not None:
        out["fulfillment_option_version"] = data["fulfillmentOptionVersion"]
    if data.get("releaseNotes") is not None:
        out["release_notes"] = data["releaseNotes"]
    if data.get("usageInstructions") is not None:
        out["usage_instructions"] = data["usageInstructions"]
    if data.get("recommendation") is not None:
        import capo_marketplace_discovery.types.sage_maker_algorithm_recommendation

        out["recommendation"] = (
            capo_marketplace_discovery.types.sage_maker_algorithm_recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    return out
