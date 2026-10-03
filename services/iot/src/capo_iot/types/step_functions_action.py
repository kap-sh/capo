"""Generated from Smithy shape ``com.amazonaws.iot#StepFunctionsAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.execution_name_prefix
    import capo_iot.types.state_machine_name


class StepFunctionsAction(TypedDict, closed=True):
    execution_name_prefix: NotRequired[
        "capo_iot.types.execution_name_prefix.ExecutionNamePrefix"
    ]
    """<p>(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.</p>"""
    state_machine_name: "capo_iot.types.state_machine_name.StateMachineName"
    """<p>The name of the Step Functions state machine whose execution will be started.</p>"""
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepFunctionsAction) -> dict:
    out: dict = {}
    if "execution_name_prefix" in value:
        out["executionNamePrefix"] = value["execution_name_prefix"]
    out["stateMachineName"] = value["state_machine_name"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> StepFunctionsAction:
    out: StepFunctionsAction = {}  # type: ignore[typeddict-item]
    if data.get("executionNamePrefix") is not None:
        out["execution_name_prefix"] = data["executionNamePrefix"]
    if data.get("stateMachineName") is not None:
        out["state_machine_name"] = data["stateMachineName"]
    else:
        raise DeserializationError("StepFunctionsAction.state_machine_name required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("StepFunctionsAction.role_arn required")
    return out
