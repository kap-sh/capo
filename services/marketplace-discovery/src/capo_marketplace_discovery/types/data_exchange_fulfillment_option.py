"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DataExchangeFulfillmentOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.data_artifact_list
    import capo_marketplace_discovery.types.fulfillment_option_type


class DataExchangeFulfillmentOption(TypedDict, closed=True):
    fulfillment_option_id: "str"
    """<p>The unique identifier of the fulfillment option.</p>"""
    fulfillment_option_type: (
        "capo_marketplace_discovery.types.fulfillment_option_type.FulfillmentOptionType"
    )
    """<p>The category of the fulfillment option.</p>"""
    fulfillment_option_display_name: "str"
    """<p>A human-readable name for the fulfillment option type.</p>"""
    data_artifacts: NotRequired[
        "capo_marketplace_discovery.types.data_artifact_list.DataArtifactList"
    ]
    """<p>The data artifacts included in this Data Exchange fulfillment option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataExchangeFulfillmentOption) -> dict:
    out: dict = {}
    out["fulfillmentOptionId"] = value["fulfillment_option_id"]
    import capo_marketplace_discovery.types.fulfillment_option_type

    out["fulfillmentOptionType"] = (
        capo_marketplace_discovery.types.fulfillment_option_type.serialize_json(
            value["fulfillment_option_type"]
        )
    )
    out["fulfillmentOptionDisplayName"] = value["fulfillment_option_display_name"]
    if "data_artifacts" in value:
        import capo_marketplace_discovery.types.data_artifact_list

        out["dataArtifacts"] = (
            capo_marketplace_discovery.types.data_artifact_list.serialize_json(
                value["data_artifacts"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataExchangeFulfillmentOption:
    out: DataExchangeFulfillmentOption = {}  # type: ignore[typeddict-item]
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
    if data.get("dataArtifacts") is not None:
        import capo_marketplace_discovery.types.data_artifact_list

        out["data_artifacts"] = (
            capo_marketplace_discovery.types.data_artifact_list.deserialize_json(
                data["dataArtifacts"]
            )
        )
    return out
