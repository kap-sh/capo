"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationEventStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_event_steps
    import capo_compute_optimizer_automation.types.next_token


class ListAutomationEventStepsResponse(TypedDict, closed=True):
    automation_event_steps: NotRequired[
        "capo_compute_optimizer_automation.types.automation_event_steps.AutomationEventSteps"
    ]
    """<p> The list of steps for the specified automation event. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationEventStepsResponse) -> dict:
    out: dict = {}
    if "automation_event_steps" in value:
        import capo_compute_optimizer_automation.types.automation_event_steps

        out["automationEventSteps"] = (
            capo_compute_optimizer_automation.types.automation_event_steps.serialize_aws_json_1_0(
                value["automation_event_steps"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationEventStepsResponse:
    out: ListAutomationEventStepsResponse = {}  # type: ignore[typeddict-item]
    if data.get("automationEventSteps") is not None:
        import capo_compute_optimizer_automation.types.automation_event_steps

        out["automation_event_steps"] = (
            capo_compute_optimizer_automation.types.automation_event_steps.deserialize_aws_json_1_0(
                data["automationEventSteps"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAutomationEventStepsResponse) -> dict:
    out: dict = {}
    if "automation_event_steps" in value:
        import capo_compute_optimizer_automation.types.automation_event_steps

        out["automationEventSteps"] = (
            capo_compute_optimizer_automation.types.automation_event_steps.serialize_cbor(
                value["automation_event_steps"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAutomationEventStepsResponse:
    out: ListAutomationEventStepsResponse = {}  # type: ignore[typeddict-item]
    if data.get("automationEventSteps") is not None:
        import capo_compute_optimizer_automation.types.automation_event_steps

        out["automation_event_steps"] = (
            capo_compute_optimizer_automation.types.automation_event_steps.deserialize_cbor(
                data["automationEventSteps"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
