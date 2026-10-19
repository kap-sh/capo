"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetEnrichmentEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_enrichment_status
    import capo_iotsitewise.types.timestamp


class DatasetEnrichmentEntry(TypedDict, closed=True):
    status: "capo_iotsitewise.types.dataset_enrichment_status.DatasetEnrichmentStatus"
    """<p>The enrichment status of the data type in the dataset.</p>"""
    last_enriched_at: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the data was last enriched, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetEnrichmentEntry) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.dataset_enrichment_status

    out["status"] = capo_iotsitewise.types.dataset_enrichment_status.serialize_json(
        value["status"]
    )
    if "last_enriched_at" in value:
        import capo_iotsitewise.types.timestamp

        out["lastEnrichedAt"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["last_enriched_at"]
        )
    return out


def deserialize_json(data: dict) -> DatasetEnrichmentEntry:
    out: DatasetEnrichmentEntry = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_iotsitewise.types.dataset_enrichment_status

        out["status"] = (
            capo_iotsitewise.types.dataset_enrichment_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iotsitewise.types.dataset_enrichment_status.DatasetEnrichmentStatus",
            "",
        )
    if data.get("lastEnrichedAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_enriched_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastEnrichedAt"]
        )
    return out
