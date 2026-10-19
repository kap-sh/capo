"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineVersionListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.long_arn
    import capo_sfn.types.timestamp


class StateMachineVersionListItem(TypedDict, closed=True):
    state_machine_version_arn: "capo_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) that identifies a state machine version. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, <code>stateMachineARN:1</code>.</p>"""
    creation_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The creation date of a state machine version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineVersionListItem) -> dict:
    out: dict = {}
    out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    import capo_sfn.types.timestamp

    out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateMachineVersionListItem:
    out: StateMachineVersionListItem = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineVersionArn") is not None:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    else:
        out["state_machine_version_arn"] = ""
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
    return out
