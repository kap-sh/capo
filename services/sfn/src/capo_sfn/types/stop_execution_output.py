"""Generated from Smithy shape ``com.amazonaws.sfn#StopExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.timestamp


class StopExecutionOutput(TypedDict, closed=True):
    stop_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the execution is stopped.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopExecutionOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.timestamp

    out["stopDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["stop_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StopExecutionOutput:
    out: StopExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("stopDate") is not None:
        import capo_sfn.types.timestamp

        out["stop_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    else:
        import datetime

        out["stop_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
