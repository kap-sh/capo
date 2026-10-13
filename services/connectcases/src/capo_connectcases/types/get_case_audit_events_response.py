"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseAuditEventsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.audit_events_list
    import capo_connectcases.types.next_token


class GetCaseAuditEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""
    audit_events: "capo_connectcases.types.audit_events_list.AuditEventsList"
    """<p>A list of case audits where each represents a particular edit of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseAuditEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_connectcases.types.audit_events_list

    out["auditEvents"] = capo_connectcases.types.audit_events_list.serialize_json(
        value["audit_events"]
    )
    return out


def deserialize_json(data: dict) -> GetCaseAuditEventsResponse:
    out: GetCaseAuditEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("auditEvents") is not None:
        import capo_connectcases.types.audit_events_list

        out["audit_events"] = (
            capo_connectcases.types.audit_events_list.deserialize_json(
                data["auditEvents"]
            )
        )
    else:
        raise DeserializationError("GetCaseAuditEventsResponse.audit_events required")
    return out


def redact_sensitive(value: GetCaseAuditEventsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "audit_events" in value:
        import capo_connectcases.types.audit_events_list

        out["audit_events"] = (
            capo_connectcases.types.audit_events_list.redact_sensitive(
                value["audit_events"]
            )
        )
    return out
