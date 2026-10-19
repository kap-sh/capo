"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelPropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_property_summaries
    import capo_iotsitewise.types.next_token


class ListAssetModelPropertiesResponse(TypedDict, closed=True):
    asset_model_property_summaries: "capo_iotsitewise.types.asset_model_property_summaries.AssetModelPropertySummaries"
    """<p>A list that summarizes the properties associated with the specified asset model.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetModelPropertiesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_model_property_summaries

    out["assetModelPropertySummaries"] = (
        capo_iotsitewise.types.asset_model_property_summaries.serialize_json(
            value["asset_model_property_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetModelPropertiesResponse:
    out: ListAssetModelPropertiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelPropertySummaries") is not None:
        import capo_iotsitewise.types.asset_model_property_summaries

        out["asset_model_property_summaries"] = (
            capo_iotsitewise.types.asset_model_property_summaries.deserialize_json(
                data["assetModelPropertySummaries"]
            )
        )
    else:
        out["asset_model_property_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
