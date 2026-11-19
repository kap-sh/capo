"""Generated from Smithy shape ``com.amazonaws.guardduty#ListInvestigationRecordsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_id
    import capo_guardduty.types.investigation_status
    import capo_guardduty.types.next_token
    import capo_guardduty.types.records


class ListInvestigationRecordsResponse(TypedDict, closed=True):
    investigation_id: NotRequired[
        "capo_guardduty.types.investigation_id.InvestigationId"
    ]
    """<p>The unique identifier of the investigation.</p>"""
    status: NotRequired["capo_guardduty.types.investigation_status.InvestigationStatus"]
    """<p>The current status of the investigation. Possible values are <code>RUNNING</code>, <code>COMPLETED</code>, and <code>FAILED</code>. Records are returned only when the status is <code>COMPLETED</code>. If the status is <code>RUNNING</code> or <code>FAILED</code>, the response contains an empty list of records and no <code>NextToken</code>.</p>"""
    records: NotRequired["capo_guardduty.types.records.Records"]
    """<p>The records for the investigation, in the order that GuardDuty created them, oldest first. This list can contain fewer records than <code>MaxResults</code>, or no records, even when more records are available. To check for more records, use <code>NextToken</code>.</p>"""
    next_token: NotRequired["capo_guardduty.types.next_token.NextToken"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items. If this value is absent, there are no more records to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationRecordsResponse) -> dict:
    out: dict = {}
    if "investigation_id" in value:
        out["investigationId"] = value["investigation_id"]
    if "status" in value:
        import capo_guardduty.types.investigation_status

        out["status"] = capo_guardduty.types.investigation_status.serialize_json(
            value["status"]
        )
    if "records" in value:
        import capo_guardduty.types.records

        out["records"] = capo_guardduty.types.records.serialize_json(value["records"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvestigationRecordsResponse:
    out: ListInvestigationRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("investigationId") is not None:
        out["investigation_id"] = data["investigationId"]
    if data.get("status") is not None:
        import capo_guardduty.types.investigation_status

        out["status"] = capo_guardduty.types.investigation_status.deserialize_json(
            data["status"]
        )
    if data.get("records") is not None:
        import capo_guardduty.types.records

        out["records"] = capo_guardduty.types.records.deserialize_json(data["records"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListInvestigationRecordsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "records" in value:
        import capo_guardduty.types.records

        out["records"] = capo_guardduty.types.records.redact_sensitive(value["records"])
    return out
