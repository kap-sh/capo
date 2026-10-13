"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionStartedEventDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.history_event_execution_data_details
    import capo_sfn.types.sensitive_data


class ExecutionStartedEventDetails(TypedDict, closed=True):
    input: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON data input to the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    input_details: NotRequired[
        "capo_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about the input for an execution history event.</p>"""
    role_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used for executing Lambda tasks.</p>"""
    state_machine_alias_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies a state machine alias used for starting the state machine execution.</p>"""
    state_machine_version_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies a state machine version used for starting the state machine execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionStartedEventDetails) -> dict:
    out: dict = {}
    if "input" in value:
        out["input"] = value["input"]
    if "input_details" in value:
        import capo_sfn.types.history_event_execution_data_details

        out["inputDetails"] = (
            capo_sfn.types.history_event_execution_data_details.serialize_aws_json_1_0(
                value["input_details"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "state_machine_alias_arn" in value:
        out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    if "state_machine_version_arn" in value:
        out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionStartedEventDetails:
    out: ExecutionStartedEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("inputDetails") is not None:
        import capo_sfn.types.history_event_execution_data_details

        out["input_details"] = (
            capo_sfn.types.history_event_execution_data_details.deserialize_aws_json_1_0(
                data["inputDetails"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("stateMachineAliasArn") is not None:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    if data.get("stateMachineVersionArn") is not None:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    return out


def redact_sensitive(value: ExecutionStartedEventDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        out["input"] = "*** Sensitive Data Redacted ***"
    return out
