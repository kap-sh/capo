"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateIntegrationWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.uuid


class CreateIntegrationWorkflowResponse(TypedDict, closed=True):
    workflow_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>Unique identifier for the workflow.</p>"""
    message: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>A message indicating create request was received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateIntegrationWorkflowResponse:
    out: CreateIntegrationWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
