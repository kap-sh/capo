"""Generated from Smithy shape ``com.amazonaws.sfn#PublishStateMachineVersionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.timestamp


class PublishStateMachineVersionOutput(TypedDict, closed=True):
    creation_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the version was created.</p>"""
    state_machine_version_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) (ARN) that identifies the state machine version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublishStateMachineVersionOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.timestamp

    out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PublishStateMachineVersionOutput:
    out: PublishStateMachineVersionOutput = {}  # type: ignore[typeddict-item]
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
    else:
        out["state_machine_version_arn"] = ""
    return out
