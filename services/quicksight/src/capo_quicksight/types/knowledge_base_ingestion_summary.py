"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseIngestionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.kb_ingestion_id
    import capo_quicksight.types.kb_ingestion_status


class KnowledgeBaseIngestionSummary(TypedDict, closed=True):
    ingestion_id: "capo_quicksight.types.kb_ingestion_id.KbIngestionId"
    """<p>The unique identifier for the ingestion job.</p>"""
    ingestion_status: "capo_quicksight.types.kb_ingestion_status.KbIngestionStatus"
    """<p>The status of the ingestion job.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time of the ingestion job.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the ingestion job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseIngestionSummary) -> dict:
    out: dict = {}
    out["IngestionId"] = value["ingestion_id"]
    import capo_quicksight.types.kb_ingestion_status

    out["IngestionStatus"] = capo_quicksight.types.kb_ingestion_status.serialize_json(
        value["ingestion_status"]
    )
    if "start_time" in value:
        import capo_quicksight.types._prelude.timestamp

        out["StartTime"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_quicksight.types._prelude.timestamp

        out["EndTime"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseIngestionSummary:
    out: KnowledgeBaseIngestionSummary = {}  # type: ignore[typeddict-item]
    if data.get("IngestionId") is not None:
        out["ingestion_id"] = data["IngestionId"]
    else:
        out["ingestion_id"] = ""
    if data.get("IngestionStatus") is not None:
        import capo_quicksight.types.kb_ingestion_status

        out["ingestion_status"] = (
            capo_quicksight.types.kb_ingestion_status.deserialize_json(
                data["IngestionStatus"]
            )
        )
    else:
        import typing

        out["ingestion_status"] = typing.cast(
            "capo_quicksight.types.kb_ingestion_status.KbIngestionStatus", ""
        )
    if data.get("StartTime") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["start_time"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["end_time"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["EndTime"]
        )
    return out
