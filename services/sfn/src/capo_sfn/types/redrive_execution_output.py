"""Generated from Smithy shape ``com.amazonaws.sfn#RedriveExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.timestamp


class RedriveExecutionOutput(TypedDict, closed=True):
    redrive_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the execution was last redriven.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RedriveExecutionOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.timestamp

    out["redriveDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["redrive_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RedriveExecutionOutput:
    out: RedriveExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("redriveDate") is not None:
        import capo_sfn.types.timestamp

        out["redrive_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["redriveDate"]
        )
    else:
        import datetime

        out["redrive_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
