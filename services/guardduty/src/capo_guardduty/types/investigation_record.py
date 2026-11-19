"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationRecord``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.narrative
    import capo_guardduty.types.record_id
    import capo_guardduty.types.record_title
    import capo_guardduty.types.record_type
    import capo_guardduty.types.supporting_data
    import capo_guardduty.types.timestamp


class InvestigationRecord(TypedDict, closed=True):
    record_id: NotRequired["capo_guardduty.types.record_id.RecordId"]
    """<p>The unique identifier of the record.</p>"""
    type: NotRequired["capo_guardduty.types.record_type.RecordType"]
    """<p>The type of the record. Possible values:</p> <ul> <li> <p> <code>UPDATE</code> – A progress milestone, such as the request that started the investigation or a response from GuardDuty.</p> </li> <li> <p> <code>FETCH</code> – Data that GuardDuty retrieved for the investigation, such as a finding, a detector configuration, or a list of your member accounts. The record includes what GuardDuty requested and what it received.</p> </li> <li> <p> <code>OBSERVATION</code> – A fact that GuardDuty noted about your environment, such as the affected resource, the activity on that resource, or your detection coverage.</p> </li> <li> <p> <code>ANALYSIS</code> – An assessment that GuardDuty derived from the data, such as a threat assessment, a comparison against normal behavior, or a process lineage.</p> </li> <li> <p> <code>METADATA</code> – Operational details about the investigation itself, such as how long the investigation took.</p> </li> </ul>"""
    title: NotRequired["capo_guardduty.types.record_title.RecordTitle"]
    """<p>A short title that describes the step.</p>"""
    narrative: NotRequired["capo_guardduty.types.narrative.Narrative"]
    """<p>A plain-text explanation of the step. A narrative can span several paragraphs. Not every record includes a narrative.</p>"""
    created_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which GuardDuty created the record.</p>"""
    supporting_data: NotRequired["capo_guardduty.types.supporting_data.SupportingData"]
    """<p>The structured details for the step. The member that is set matches the record type. <code>UPDATE</code> records never include supporting data, and records of other types don't always include it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationRecord) -> dict:
    out: dict = {}
    if "record_id" in value:
        out["recordId"] = value["record_id"]
    if "type" in value:
        import capo_guardduty.types.record_type

        out["type"] = capo_guardduty.types.record_type.serialize_json(value["type"])
    if "title" in value:
        out["title"] = value["title"]
    if "narrative" in value:
        out["narrative"] = value["narrative"]
    if "created_at" in value:
        import capo_guardduty.types.timestamp

        out["createdAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "supporting_data" in value:
        import capo_guardduty.types.supporting_data

        out["supportingData"] = capo_guardduty.types.supporting_data.serialize_json(
            value["supporting_data"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationRecord:
    out: InvestigationRecord = {}  # type: ignore[typeddict-item]
    if data.get("recordId") is not None:
        out["record_id"] = data["recordId"]
    if data.get("type") is not None:
        import capo_guardduty.types.record_type

        out["type"] = capo_guardduty.types.record_type.deserialize_json(data["type"])
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("narrative") is not None:
        out["narrative"] = data["narrative"]
    if data.get("createdAt") is not None:
        import capo_guardduty.types.timestamp

        out["created_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("supportingData") is not None:
        import capo_guardduty.types.supporting_data

        out["supporting_data"] = capo_guardduty.types.supporting_data.deserialize_json(
            data["supportingData"]
        )
    return out


def redact_sensitive(value: InvestigationRecord) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "supporting_data" in value:
        import capo_guardduty.types.supporting_data

        out["supporting_data"] = capo_guardduty.types.supporting_data.redact_sensitive(
            value["supporting_data"]
        )
    return out
