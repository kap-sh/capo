"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteStateMachineAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn


class DeleteStateMachineAliasInput(TypedDict, closed=True):
    state_machine_alias_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine alias to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteStateMachineAliasInput) -> dict:
    out: dict = {}
    out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteStateMachineAliasInput:
    out: DeleteStateMachineAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineAliasArn") is not None:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    else:
        out["state_machine_alias_arn"] = ""
    return out
