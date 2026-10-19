"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateStateMachineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.revision_id
    import capo_sfn.types.timestamp


class UpdateStateMachineOutput(TypedDict, closed=True):
    update_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date and time the state machine was updated.</p>"""
    revision_id: NotRequired["capo_sfn.types.revision_id.RevisionId"]
    """<p>The revision identifier for the updated state machine.</p>"""
    state_machine_version_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the published state machine version.</p> <p>If the <code>publish</code> parameter isn't set to <code>true</code>, this field returns null.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateMachineOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.timestamp

    out["updateDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["update_date"]
    )
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "state_machine_version_arn" in value:
        out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateMachineOutput:
    out: UpdateStateMachineOutput = {}  # type: ignore[typeddict-item]
    if data.get("updateDate") is not None:
        import capo_sfn.types.timestamp

        out["update_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["updateDate"]
        )
    else:
        import datetime

        out["update_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("stateMachineVersionArn") is not None:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    return out
