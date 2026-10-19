"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListProjectAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_i_ds
    import capo_iotsitewise.types.next_token


class ListProjectAssetsResponse(TypedDict, closed=True):
    asset_ids: "capo_iotsitewise.types.asset_i_ds.AssetIDs"
    """<p>A list that contains the IDs of each asset associated with the project.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectAssetsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_i_ds

    out["assetIds"] = capo_iotsitewise.types.asset_i_ds.serialize_json(
        value["asset_ids"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProjectAssetsResponse:
    out: ListProjectAssetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetIds") is not None:
        import capo_iotsitewise.types.asset_i_ds

        out["asset_ids"] = capo_iotsitewise.types.asset_i_ds.deserialize_json(
            data["assetIds"]
        )
    else:
        out["asset_ids"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
