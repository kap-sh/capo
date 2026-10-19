"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StartAutomationEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.client_token
    import capo_compute_optimizer_automation.types.recommended_action_id


class StartAutomationEventRequest(TypedDict, closed=True):
    recommended_action_id: "capo_compute_optimizer_automation.types.recommended_action_id.RecommendedActionId"
    """<p> The ID of the recommended action to automate. </p>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAutomationEventRequest) -> dict:
    out: dict = {}
    out["recommendedActionId"] = value["recommended_action_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAutomationEventRequest:
    out: StartAutomationEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActionId") is not None:
        out["recommended_action_id"] = data["recommendedActionId"]
    else:
        out["recommended_action_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
