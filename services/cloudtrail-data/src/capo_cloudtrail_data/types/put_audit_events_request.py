"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#PutAuditEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail_data.types.audit_events
    import capo_cloudtrail_data.types.channel_arn
    import capo_cloudtrail_data.types.external_id


class PutAuditEventsRequest(TypedDict, closed=True):
    audit_events: "capo_cloudtrail_data.types.audit_events.AuditEvents"
    """<p>The JSON payload of events that you want to ingest. You can also point to the JSON event payload in a file.</p>"""
    channel_arn: "capo_cloudtrail_data.types.channel_arn.ChannelArn"
    """<p>The ARN or ID (the ARN suffix) of a channel.</p>"""
    external_id: NotRequired["capo_cloudtrail_data.types.external_id.ExternalId"]
    """<p>A unique identifier that is conditionally required when the channel's resource policy includes an external ID. This value can be any string, such as a passphrase or account number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAuditEventsRequest) -> dict:
    out: dict = {}
    import capo_cloudtrail_data.types.audit_events

    out["auditEvents"] = capo_cloudtrail_data.types.audit_events.serialize_json(
        value["audit_events"]
    )
    return out


def deserialize_json(data: dict) -> PutAuditEventsRequest:
    out: PutAuditEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("auditEvents") is not None:
        import capo_cloudtrail_data.types.audit_events

        out["audit_events"] = capo_cloudtrail_data.types.audit_events.deserialize_json(
            data["auditEvents"]
        )
    else:
        out["audit_events"] = []
    return out
