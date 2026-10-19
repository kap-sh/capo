"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#PutAuditEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail_data.types.audit_event_result_entries
    import capo_cloudtrail_data.types.result_error_entries


class PutAuditEventsResponse(TypedDict, closed=True):
    successful: (
        "capo_cloudtrail_data.types.audit_event_result_entries.AuditEventResultEntries"
    )
    """<p>Lists events in the provided event payload that were successfully ingested into CloudTrail.</p>"""
    failed: "capo_cloudtrail_data.types.result_error_entries.ResultErrorEntries"
    """<p>Lists events in the provided event payload that could not be ingested into CloudTrail, and includes the error code and error message returned for events that could not be ingested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAuditEventsResponse) -> dict:
    out: dict = {}
    import capo_cloudtrail_data.types.audit_event_result_entries

    out["successful"] = (
        capo_cloudtrail_data.types.audit_event_result_entries.serialize_json(
            value["successful"]
        )
    )
    import capo_cloudtrail_data.types.result_error_entries

    out["failed"] = capo_cloudtrail_data.types.result_error_entries.serialize_json(
        value["failed"]
    )
    return out


def deserialize_json(data: dict) -> PutAuditEventsResponse:
    out: PutAuditEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("successful") is not None:
        import capo_cloudtrail_data.types.audit_event_result_entries

        out["successful"] = (
            capo_cloudtrail_data.types.audit_event_result_entries.deserialize_json(
                data["successful"]
            )
        )
    else:
        out["successful"] = []
    if data.get("failed") is not None:
        import capo_cloudtrail_data.types.result_error_entries

        out["failed"] = (
            capo_cloudtrail_data.types.result_error_entries.deserialize_json(
                data["failed"]
            )
        )
    else:
        out["failed"] = []
    return out
