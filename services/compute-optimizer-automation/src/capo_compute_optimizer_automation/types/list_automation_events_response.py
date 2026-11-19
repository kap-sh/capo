"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_events
    import capo_compute_optimizer_automation.types.next_token


class ListAutomationEventsResponse(TypedDict, closed=True):
    automation_events: NotRequired[
        "capo_compute_optimizer_automation.types.automation_events.AutomationEvents"
    ]
    """<p> The list of automation events that match the specified criteria. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p> The token to use to retrieve the next page of results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationEventsResponse) -> dict:
    out: dict = {}
    if "automation_events" in value:
        import capo_compute_optimizer_automation.types.automation_events

        out["automationEvents"] = (
            capo_compute_optimizer_automation.types.automation_events.serialize_aws_json_1_0(
                value["automation_events"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationEventsResponse:
    out: ListAutomationEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("automationEvents") is not None:
        import capo_compute_optimizer_automation.types.automation_events

        out["automation_events"] = (
            capo_compute_optimizer_automation.types.automation_events.deserialize_aws_json_1_0(
                data["automationEvents"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAutomationEventsResponse) -> dict:
    out: dict = {}
    if "automation_events" in value:
        import capo_compute_optimizer_automation.types.automation_events

        out["automationEvents"] = (
            capo_compute_optimizer_automation.types.automation_events.serialize_cbor(
                value["automation_events"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAutomationEventsResponse:
    out: ListAutomationEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("automationEvents") is not None:
        import capo_compute_optimizer_automation.types.automation_events

        out["automation_events"] = (
            capo_compute_optimizer_automation.types.automation_events.deserialize_cbor(
                data["automationEvents"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
