"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateInvestigationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.client_token
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.trigger_prompt


class CreateInvestigationRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the GuardDuty detector for the account in which the investigation is created.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    trigger_prompt: NotRequired["capo_guardduty.types.trigger_prompt.TriggerPrompt"]
    """<p>A natural-language description of what to investigate. For example:</p> <ul> <li> <p> <code>"Investigate finding 1ab2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 in account 123456789012"</code> </p> </li> <li> <p> <code>"Analyze findings in account with id 123456789012"</code> </p> </li> <li> <p> <code>"Analyze findings in my organization"</code> </p> </li> </ul>"""
    client_token: NotRequired["capo_guardduty.types.client_token.ClientToken"]
    """<p>The idempotency token for the create request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInvestigationRequest) -> dict:
    out: dict = {}
    if "trigger_prompt" in value:
        out["triggerPrompt"] = value["trigger_prompt"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateInvestigationRequest:
    out: CreateInvestigationRequest = {}  # type: ignore[typeddict-item]
    if data.get("triggerPrompt") is not None:
        out["trigger_prompt"] = data["triggerPrompt"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
