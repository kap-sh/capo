"""Generated from Smithy shape ``com.amazonaws.sfn#StartExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.timestamp


class StartExecutionOutput(TypedDict, closed=True):
    execution_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the execution.</p>"""
    start_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the execution is started.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartExecutionOutput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    import capo_sfn.types.timestamp

    out["startDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartExecutionOutput:
    out: StartExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        out["execution_arn"] = ""
    if data.get("startDate") is not None:
        import capo_sfn.types.timestamp

        out["start_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
