"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateStateMachineAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.timestamp


class UpdateStateMachineAliasOutput(TypedDict, closed=True):
    update_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date and time the state machine alias was updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateMachineAliasOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.timestamp

    out["updateDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["update_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateMachineAliasOutput:
    out: UpdateStateMachineAliasOutput = {}  # type: ignore[typeddict-item]
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
    return out
