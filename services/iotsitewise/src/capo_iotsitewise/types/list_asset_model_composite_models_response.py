"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelCompositeModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_model_summaries
    import capo_iotsitewise.types.next_token


class ListAssetModelCompositeModelsResponse(TypedDict, closed=True):
    asset_model_composite_model_summaries: "capo_iotsitewise.types.asset_model_composite_model_summaries.AssetModelCompositeModelSummaries"
    """<p>A list that summarizes each composite model.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetModelCompositeModelsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_model_composite_model_summaries

    out["assetModelCompositeModelSummaries"] = (
        capo_iotsitewise.types.asset_model_composite_model_summaries.serialize_json(
            value["asset_model_composite_model_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetModelCompositeModelsResponse:
    out: ListAssetModelCompositeModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelCompositeModelSummaries") is not None:
        import capo_iotsitewise.types.asset_model_composite_model_summaries

        out["asset_model_composite_model_summaries"] = (
            capo_iotsitewise.types.asset_model_composite_model_summaries.deserialize_json(
                data["assetModelCompositeModelSummaries"]
            )
        )
    else:
        out["asset_model_composite_model_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
