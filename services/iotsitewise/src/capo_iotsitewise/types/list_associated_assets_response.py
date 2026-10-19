"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssociatedAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.associated_assets_summaries
    import capo_iotsitewise.types.next_token


class ListAssociatedAssetsResponse(TypedDict, closed=True):
    asset_summaries: (
        "capo_iotsitewise.types.associated_assets_summaries.AssociatedAssetsSummaries"
    )
    """<p>A list that summarizes the associated assets.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedAssetsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.associated_assets_summaries

    out["assetSummaries"] = (
        capo_iotsitewise.types.associated_assets_summaries.serialize_json(
            value["asset_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedAssetsResponse:
    out: ListAssociatedAssetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetSummaries") is not None:
        import capo_iotsitewise.types.associated_assets_summaries

        out["asset_summaries"] = (
            capo_iotsitewise.types.associated_assets_summaries.deserialize_json(
                data["assetSummaries"]
            )
        )
    else:
        out["asset_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
