"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetAssetPropertyValueHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_value_history
    import capo_iotsitewise.types.next_token


class GetAssetPropertyValueHistoryResponse(TypedDict, closed=True):
    asset_property_value_history: (
        "capo_iotsitewise.types.asset_property_value_history.AssetPropertyValueHistory"
    )
    """<p>The asset property's value history.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetPropertyValueHistoryResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_property_value_history

    out["assetPropertyValueHistory"] = (
        capo_iotsitewise.types.asset_property_value_history.serialize_json(
            value["asset_property_value_history"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetAssetPropertyValueHistoryResponse:
    out: GetAssetPropertyValueHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("assetPropertyValueHistory") is not None:
        import capo_iotsitewise.types.asset_property_value_history

        out["asset_property_value_history"] = (
            capo_iotsitewise.types.asset_property_value_history.deserialize_json(
                data["assetPropertyValueHistory"]
            )
        )
    else:
        out["asset_property_value_history"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
