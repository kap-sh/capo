"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.name
    import capo_sfn.types.state_machine_type
    import capo_sfn.types.timestamp


class StateMachineListItem(TypedDict, closed=True):
    state_machine_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the state machine.</p>"""
    name: "capo_sfn.types.name.Name"
    r"""<p>The name of the state machine.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    type: "capo_sfn.types.state_machine_type.StateMachineType"
    """<p></p>"""
    creation_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the state machine is created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineListItem) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    out["name"] = value["name"]
    import capo_sfn.types.state_machine_type

    out["type"] = capo_sfn.types.state_machine_type.serialize_aws_json_1_0(
        value["type"]
    )
    import capo_sfn.types.timestamp

    out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateMachineListItem:
    out: StateMachineListItem = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        out["state_machine_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_sfn.types.state_machine_type

        out["type"] = capo_sfn.types.state_machine_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_sfn.types.state_machine_type.StateMachineType", ""
        )
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
