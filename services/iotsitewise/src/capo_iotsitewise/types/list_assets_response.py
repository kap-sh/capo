"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_summaries
    import capo_iotsitewise.types.next_token


class ListAssetsResponse(TypedDict, closed=True):
    asset_summaries: "capo_iotsitewise.types.asset_summaries.AssetSummaries"
    """<p>A list that summarizes each asset.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_summaries

    out["assetSummaries"] = capo_iotsitewise.types.asset_summaries.serialize_json(
        value["asset_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetsResponse:
    out: ListAssetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetSummaries") is not None:
        import capo_iotsitewise.types.asset_summaries

        out["asset_summaries"] = (
            capo_iotsitewise.types.asset_summaries.deserialize_json(
                data["assetSummaries"]
            )
        )
    else:
        out["asset_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
