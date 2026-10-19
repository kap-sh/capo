"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.batch_put_asset_property_error_entries


class BatchPutAssetPropertyValueResponse(TypedDict, closed=True):
    error_entries: "capo_iotsitewise.types.batch_put_asset_property_error_entries.BatchPutAssetPropertyErrorEntries"
    """<p>A list of the errors (if any) associated with the batch put request. Each error entry contains the <code>entryId</code> of the entry that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyValueResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.batch_put_asset_property_error_entries

    out["errorEntries"] = (
        capo_iotsitewise.types.batch_put_asset_property_error_entries.serialize_json(
            value["error_entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutAssetPropertyValueResponse:
    out: BatchPutAssetPropertyValueResponse = {}  # type: ignore[typeddict-item]
    if data.get("errorEntries") is not None:
        import capo_iotsitewise.types.batch_put_asset_property_error_entries

        out["error_entries"] = (
            capo_iotsitewise.types.batch_put_asset_property_error_entries.deserialize_json(
                data["errorEntries"]
            )
        )
    else:
        out["error_entries"] = []
    return out
