"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StartAutomationEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.event_id
    import capo_compute_optimizer_automation.types.event_status
    import capo_compute_optimizer_automation.types.recommended_action_id


class StartAutomationEventResponse(TypedDict, closed=True):
    recommended_action_id: NotRequired[
        "capo_compute_optimizer_automation.types.recommended_action_id.RecommendedActionId"
    ]
    """<p>The ID of the recommended action being automated.</p>"""
    event_id: NotRequired["capo_compute_optimizer_automation.types.event_id.EventId"]
    """<p>The ID of the automation event.</p>"""
    event_status: NotRequired[
        "capo_compute_optimizer_automation.types.event_status.EventStatus"
    ]
    """<p>The current status of the automation event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAutomationEventResponse) -> dict:
    out: dict = {}
    if "recommended_action_id" in value:
        out["recommendedActionId"] = value["recommended_action_id"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_status" in value:
        import capo_compute_optimizer_automation.types.event_status

        out["eventStatus"] = (
            capo_compute_optimizer_automation.types.event_status.serialize_aws_json_1_0(
                value["event_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAutomationEventResponse:
    out: StartAutomationEventResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActionId") is not None:
        out["recommended_action_id"] = data["recommendedActionId"]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("eventStatus") is not None:
        import capo_compute_optimizer_automation.types.event_status

        out["event_status"] = (
            capo_compute_optimizer_automation.types.event_status.deserialize_aws_json_1_0(
                data["eventStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartAutomationEventResponse) -> dict:
    out: dict = {}
    if "recommended_action_id" in value:
        out["recommendedActionId"] = value["recommended_action_id"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_status" in value:
        import capo_compute_optimizer_automation.types.event_status

        out["eventStatus"] = (
            capo_compute_optimizer_automation.types.event_status.serialize_cbor(
                value["event_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StartAutomationEventResponse:
    out: StartAutomationEventResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActionId") is not None:
        out["recommended_action_id"] = data["recommendedActionId"]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("eventStatus") is not None:
        import capo_compute_optimizer_automation.types.event_status

        out["event_status"] = (
            capo_compute_optimizer_automation.types.event_status.deserialize_cbor(
                data["eventStatus"]
            )
        )
    return out
