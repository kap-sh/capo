"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetRelationshipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_relationship_summaries
    import capo_iotsitewise.types.next_token


class ListAssetRelationshipsResponse(TypedDict, closed=True):
    asset_relationship_summaries: (
        "capo_iotsitewise.types.asset_relationship_summaries.AssetRelationshipSummaries"
    )
    """<p>A list that summarizes each asset relationship.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetRelationshipsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_relationship_summaries

    out["assetRelationshipSummaries"] = (
        capo_iotsitewise.types.asset_relationship_summaries.serialize_json(
            value["asset_relationship_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetRelationshipsResponse:
    out: ListAssetRelationshipsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetRelationshipSummaries") is not None:
        import capo_iotsitewise.types.asset_relationship_summaries

        out["asset_relationship_summaries"] = (
            capo_iotsitewise.types.asset_relationship_summaries.deserialize_json(
                data["assetRelationshipSummaries"]
            )
        )
    else:
        out["asset_relationship_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
