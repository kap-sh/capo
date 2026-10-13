"""Generated from Smithy shape ``com.amazonaws.sfn#TestStateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.inspection_data
    import capo_sfn.types.sensitive_cause
    import capo_sfn.types.sensitive_data
    import capo_sfn.types.sensitive_error
    import capo_sfn.types.state_name
    import capo_sfn.types.test_execution_status


class TestStateOutput(TypedDict, closed=True):
    output: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON output data of the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    error: NotRequired["capo_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error returned when the execution of a state fails.</p>"""
    cause: NotRequired["capo_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A detailed explanation of the cause for the error when the execution of a state fails.</p>"""
    inspection_data: NotRequired["capo_sfn.types.inspection_data.InspectionData"]
    """<p>Returns additional details about the state's execution, including its input and output data processing flow, and HTTP request and response information. The <code>inspectionLevel</code> request parameter specifies which details are returned.</p>"""
    next_state: NotRequired["capo_sfn.types.state_name.StateName"]
    """<p>The name of the next state to transition to. If you haven't defined a next state in your definition or if the execution of the state fails, this field doesn't contain a value.</p>"""
    status: NotRequired["capo_sfn.types.test_execution_status.TestExecutionStatus"]
    """<p>The execution status of the state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestStateOutput) -> dict:
    out: dict = {}
    if "output" in value:
        out["output"] = value["output"]
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    if "inspection_data" in value:
        import capo_sfn.types.inspection_data

        out["inspectionData"] = capo_sfn.types.inspection_data.serialize_aws_json_1_0(
            value["inspection_data"]
        )
    if "next_state" in value:
        out["nextState"] = value["next_state"]
    if "status" in value:
        import capo_sfn.types.test_execution_status

        out["status"] = capo_sfn.types.test_execution_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestStateOutput:
    out: TestStateOutput = {}  # type: ignore[typeddict-item]
    if data.get("output") is not None:
        out["output"] = data["output"]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("cause") is not None:
        out["cause"] = data["cause"]
    if data.get("inspectionData") is not None:
        import capo_sfn.types.inspection_data

        out["inspection_data"] = (
            capo_sfn.types.inspection_data.deserialize_aws_json_1_0(
                data["inspectionData"]
            )
        )
    if data.get("nextState") is not None:
        out["next_state"] = data["nextState"]
    if data.get("status") is not None:
        import capo_sfn.types.test_execution_status

        out["status"] = capo_sfn.types.test_execution_status.deserialize_aws_json_1_0(
            data["status"]
        )
    return out


def redact_sensitive(value: TestStateOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "output" in value:
        out["output"] = "*** Sensitive Data Redacted ***"
    if "error" in value:
        out["error"] = "*** Sensitive Data Redacted ***"
    if "cause" in value:
        out["cause"] = "*** Sensitive Data Redacted ***"
    if "inspection_data" in value:
        out["inspection_data"] = "*** Sensitive Data Redacted ***"
    return out
