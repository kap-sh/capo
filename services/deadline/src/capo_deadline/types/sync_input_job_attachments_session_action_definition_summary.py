"""Generated from Smithy shape ``com.amazonaws.deadline#SyncInputJobAttachmentsSessionActionDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.step_id


class SyncInputJobAttachmentsSessionActionDefinitionSummary(TypedDict, closed=True):
    step_id: NotRequired["capo_deadline.types.step_id.StepId"]
    """The step ID for the sync input job attachments session action summary."""


# --- restJson1 ser/de ---
def serialize_json(
    value: SyncInputJobAttachmentsSessionActionDefinitionSummary,
) -> dict:
    out: dict = {}
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    return out


def deserialize_json(
    data: dict,
) -> SyncInputJobAttachmentsSessionActionDefinitionSummary:
    out: SyncInputJobAttachmentsSessionActionDefinitionSummary = {}  # type: ignore[typeddict-item]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    return out
