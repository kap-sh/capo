"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_get_asset_property_value_entries
    import capo_iotsitewise.types.next_token


class BatchGetAssetPropertyValueRequest(TypedDict, closed=True):
    entries: "capo_iotsitewise.types.batch_get_asset_property_value_entries.BatchGetAssetPropertyValueEntries"
    """<p>The list of asset property value entries for the batch get request. You can specify up to 128 entries per request.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.batch_get_asset_property_value_entries

    out["entries"] = (
        capo_iotsitewise.types.batch_get_asset_property_value_entries.serialize_json(
            value["entries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueRequest:
    out: BatchGetAssetPropertyValueRequest = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_iotsitewise.types.batch_get_asset_property_value_entries

        out["entries"] = (
            capo_iotsitewise.types.batch_get_asset_property_value_entries.deserialize_json(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
