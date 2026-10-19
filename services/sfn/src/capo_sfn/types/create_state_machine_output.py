"""Generated from Smithy shape ``com.amazonaws.sfn#CreateStateMachineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.timestamp


class CreateStateMachineOutput(TypedDict, closed=True):
    state_machine_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the created state machine.</p>"""
    creation_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the state machine is created.</p>"""
    state_machine_version_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies the created state machine version. If you do not set the <code>publish</code> parameter to <code>true</code>, this field returns null value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateMachineOutput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    import capo_sfn.types.timestamp

    out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    if "state_machine_version_arn" in value:
        out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStateMachineOutput:
    out: CreateStateMachineOutput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        out["state_machine_arn"] = ""
    if data.get("creationDate") is not None:
        import capo_sfn.types.timestamp

        out["creation_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("stateMachineVersionArn") is not None:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    return out
