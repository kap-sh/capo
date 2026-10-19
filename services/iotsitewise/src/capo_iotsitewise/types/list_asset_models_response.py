"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_summaries
    import capo_iotsitewise.types.next_token


class ListAssetModelsResponse(TypedDict, closed=True):
    asset_model_summaries: (
        "capo_iotsitewise.types.asset_model_summaries.AssetModelSummaries"
    )
    """<p>A list that summarizes each asset model.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetModelsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_model_summaries

    out["assetModelSummaries"] = (
        capo_iotsitewise.types.asset_model_summaries.serialize_json(
            value["asset_model_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetModelsResponse:
    out: ListAssetModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetModelSummaries") is not None:
        import capo_iotsitewise.types.asset_model_summaries

        out["asset_model_summaries"] = (
            capo_iotsitewise.types.asset_model_summaries.deserialize_json(
                data["assetModelSummaries"]
            )
        )
    else:
        out["asset_model_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
