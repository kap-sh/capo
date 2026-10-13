"""Generated from Smithy shape ``com.amazonaws.datazone#GetLineageEventOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.lineage_event
    import capo_datazone.types.lineage_event_identifier
    import capo_datazone.types.lineage_event_processing_status


class GetLineageEventOutput(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the domain.</p>"""
    id: NotRequired[
        "capo_datazone.types.lineage_event_identifier.LineageEventIdentifier"
    ]
    """<p>The ID of the lineage event.</p>"""
    event: NotRequired["capo_datazone.types.lineage_event.LineageEvent"]
    """<p>The lineage event details.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the lineage event.</p>"""
    processing_status: NotRequired[
        "capo_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
    ]
    """<p>The progressing status of the lineage event.</p>"""
    event_time: NotRequired["datetime.datetime"]
    """<p>The time of the lineage event.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the lineage event was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLineageEventOutput) -> dict:
    out: dict = {}
    if "event" in value:
        import capo_datazone.types.lineage_event

        out["event"] = capo_datazone.types.lineage_event.serialize_json(value["event"])
    return out


def deserialize_json(data: dict) -> GetLineageEventOutput:
    out: GetLineageEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("event") is not None:
        import capo_datazone.types.lineage_event

        out["event"] = capo_datazone.types.lineage_event.deserialize_json(data["event"])
    return out


def redact_sensitive(value: GetLineageEventOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event" in value:
        out["event"] = "*** Sensitive Data Redacted ***"
    return out
