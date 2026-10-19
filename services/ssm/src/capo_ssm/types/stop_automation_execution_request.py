"""Generated from Smithy shape ``com.amazonaws.ssm#StopAutomationExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_id
    import capo_ssm.types.stop_type


class StopAutomationExecutionRequest(TypedDict, closed=True):
    automation_execution_id: (
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    )
    """<p>The execution ID of the Automation to stop.</p>"""
    type: NotRequired["capo_ssm.types.stop_type.StopType"]
    """<p>The stop request type. Valid types include the following: Cancel and Complete. The default type is Cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAutomationExecutionRequest) -> dict:
    out: dict = {}
    out["AutomationExecutionId"] = value["automation_execution_id"]
    if "type" in value:
        import capo_ssm.types.stop_type

        out["Type"] = capo_ssm.types.stop_type.serialize_aws_json_1_1(value["type"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAutomationExecutionRequest:
    out: StopAutomationExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecutionId") is not None:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    else:
        out["automation_execution_id"] = ""
    if data.get("Type") is not None:
        import capo_ssm.types.stop_type

        out["type"] = capo_ssm.types.stop_type.deserialize_aws_json_1_1(data["Type"])
    return out
