"""Generated from Smithy shape ``com.amazonaws.ssm#GetAutomationExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_id


class GetAutomationExecutionRequest(TypedDict, closed=True):
    automation_execution_id: (
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    )
    """<p>The unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation runbook is initiated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutomationExecutionRequest) -> dict:
    out: dict = {}
    out["AutomationExecutionId"] = value["automation_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutomationExecutionRequest:
    out: GetAutomationExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecutionId") is not None:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    else:
        out["automation_execution_id"] = ""
    return out
