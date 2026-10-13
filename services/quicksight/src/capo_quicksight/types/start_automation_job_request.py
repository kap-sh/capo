"""Generated from Smithy shape ``com.amazonaws.quicksight#StartAutomationJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.automate_id
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.sensitive_io_payload


class StartAutomationJobRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the automation.</p>"""
    automation_group_id: "capo_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation group that contains the automation to run.</p>"""
    automation_id: "capo_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation to run.</p>"""
    input_payload: NotRequired[
        "capo_quicksight.types.sensitive_io_payload.SensitiveIOPayload"
    ]
    """<p>The input payload for the automation job, provided as a JSON string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomationJobRequest) -> dict:
    out: dict = {}
    if "input_payload" in value:
        out["InputPayload"] = value["input_payload"]
    return out


def deserialize_json(data: dict) -> StartAutomationJobRequest:
    out: StartAutomationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("InputPayload") is not None:
        out["input_payload"] = data["InputPayload"]
    return out


def redact_sensitive(value: StartAutomationJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_payload" in value:
        out["input_payload"] = "*** Sensitive Data Redacted ***"
    return out
