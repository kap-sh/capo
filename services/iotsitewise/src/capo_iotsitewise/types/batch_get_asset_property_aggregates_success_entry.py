"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesSuccessEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.aggregated_values
    import capo_iotsitewise.types.entry_id


class BatchGetAssetPropertyAggregatesSuccessEntry(TypedDict, closed=True):
    entry_id: "capo_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    aggregated_values: "capo_iotsitewise.types.aggregated_values.AggregatedValues"
    """<p>The requested aggregated asset property values (for example, average, minimum, and maximum).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesSuccessEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    import capo_iotsitewise.types.aggregated_values

    out["aggregatedValues"] = capo_iotsitewise.types.aggregated_values.serialize_json(
        value["aggregated_values"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyAggregatesSuccessEntry:
    out: BatchGetAssetPropertyAggregatesSuccessEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        out["entry_id"] = ""
    if data.get("aggregatedValues") is not None:
        import capo_iotsitewise.types.aggregated_values

        out["aggregated_values"] = (
            capo_iotsitewise.types.aggregated_values.deserialize_json(
                data["aggregatedValues"]
            )
        )
    else:
        out["aggregated_values"] = []
    return out
