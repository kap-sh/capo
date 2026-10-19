"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteStateMachineVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.long_arn


class DeleteStateMachineVersionInput(TypedDict, closed=True):
    state_machine_version_arn: "capo_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of the state machine version to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteStateMachineVersionInput) -> dict:
    out: dict = {}
    out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteStateMachineVersionInput:
    out: DeleteStateMachineVersionInput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineVersionArn") is not None:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    else:
        out["state_machine_version_arn"] = ""
    return out
