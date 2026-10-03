"""Generated from Smithy shape ``com.amazonaws.ssm#SendAutomationSignalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_id
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.signal_type


class SendAutomationSignalRequest(TypedDict, closed=True):
    automation_execution_id: (
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    )
    """<p>The unique identifier for an existing Automation execution that you want to send the signal to.</p>"""
    signal_type: "capo_ssm.types.signal_type.SignalType"
    """<p>The type of signal to send to an Automation execution. </p>"""
    payload: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The data sent with the signal. The data schema depends on the type of signal used in the request.</p> <p>For <code>Approve</code> and <code>Reject</code> signal types, the payload is an optional comment that you can send with the signal type. For example:</p> <p> <code>Comment="Looks good"</code> </p> <p>For <code>StartStep</code> and <code>Resume</code> signal types, you must send the name of the Automation step to start or resume as the payload. For example:</p> <p> <code>StepName="step1"</code> </p> <p>For the <code>StopStep</code> signal type, you must send the step execution ID as the payload. For example:</p> <p> <code>StepExecutionId="97fff367-fc5a-4299-aed8-0123456789ab"</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendAutomationSignalRequest) -> dict:
    out: dict = {}
    out["AutomationExecutionId"] = value["automation_execution_id"]
    import capo_ssm.types.signal_type

    out["SignalType"] = capo_ssm.types.signal_type.serialize_aws_json_1_1(
        value["signal_type"]
    )
    if "payload" in value:
        import capo_ssm.types.automation_parameter_map

        out["Payload"] = capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
            value["payload"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendAutomationSignalRequest:
    out: SendAutomationSignalRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecutionId") is not None:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    else:
        raise DeserializationError(
            "SendAutomationSignalRequest.automation_execution_id required"
        )
    if data.get("SignalType") is not None:
        import capo_ssm.types.signal_type

        out["signal_type"] = capo_ssm.types.signal_type.deserialize_aws_json_1_1(
            data["SignalType"]
        )
    else:
        raise DeserializationError("SendAutomationSignalRequest.signal_type required")
    if data.get("Payload") is not None:
        import capo_ssm.types.automation_parameter_map

        out["payload"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Payload"]
            )
        )
    return out
