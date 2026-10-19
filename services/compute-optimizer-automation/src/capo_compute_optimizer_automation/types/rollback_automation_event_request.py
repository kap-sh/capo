"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RollbackAutomationEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.client_token
    import capo_compute_optimizer_automation.types.event_id


class RollbackAutomationEventRequest(TypedDict, closed=True):
    event_id: "capo_compute_optimizer_automation.types.event_id.EventId"
    """<p> The ID of the automation event to roll back. </p>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RollbackAutomationEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RollbackAutomationEventRequest:
    out: RollbackAutomationEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
