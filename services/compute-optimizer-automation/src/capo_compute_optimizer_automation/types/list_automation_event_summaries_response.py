"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationEventSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_event_summary_list
    import capo_compute_optimizer_automation.types.next_token


class ListAutomationEventSummariesResponse(TypedDict, closed=True):
    automation_event_summaries: NotRequired[
        "capo_compute_optimizer_automation.types.automation_event_summary_list.AutomationEventSummaryList"
    ]
    """<p> The list of automation event summaries that match the specified criteria. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationEventSummariesResponse) -> dict:
    out: dict = {}
    if "automation_event_summaries" in value:
        import capo_compute_optimizer_automation.types.automation_event_summary_list

        out["automationEventSummaries"] = (
            capo_compute_optimizer_automation.types.automation_event_summary_list.serialize_aws_json_1_0(
                value["automation_event_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationEventSummariesResponse:
    out: ListAutomationEventSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("automationEventSummaries") is not None:
        import capo_compute_optimizer_automation.types.automation_event_summary_list

        out["automation_event_summaries"] = (
            capo_compute_optimizer_automation.types.automation_event_summary_list.deserialize_aws_json_1_0(
                data["automationEventSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAutomationEventSummariesResponse) -> dict:
    out: dict = {}
    if "automation_event_summaries" in value:
        import capo_compute_optimizer_automation.types.automation_event_summary_list

        out["automationEventSummaries"] = (
            capo_compute_optimizer_automation.types.automation_event_summary_list.serialize_cbor(
                value["automation_event_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAutomationEventSummariesResponse:
    out: ListAutomationEventSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("automationEventSummaries") is not None:
        import capo_compute_optimizer_automation.types.automation_event_summary_list

        out["automation_event_summaries"] = (
            capo_compute_optimizer_automation.types.automation_event_summary_list.deserialize_cbor(
                data["automationEventSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
