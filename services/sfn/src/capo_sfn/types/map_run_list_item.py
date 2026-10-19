"""Generated from Smithy shape ``com.amazonaws.sfn#MapRunListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.long_arn
    import capo_sfn.types.timestamp


class MapRunListItem(TypedDict, closed=True):
    execution_arn: "capo_sfn.types.arn.Arn"
    """<p>The <code>executionArn</code> of the execution from which the Map Run was started.</p>"""
    map_run_arn: "capo_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of the Map Run.</p>"""
    state_machine_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the executed state machine.</p>"""
    start_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date on which the Map Run started.</p>"""
    stop_date: NotRequired["capo_sfn.types.timestamp.Timestamp"]
    """<p>The date on which the Map Run stopped.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapRunListItem) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    out["mapRunArn"] = value["map_run_arn"]
    out["stateMachineArn"] = value["state_machine_arn"]
    import capo_sfn.types.timestamp

    out["startDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    if "stop_date" in value:
        import capo_sfn.types.timestamp

        out["stopDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
            value["stop_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MapRunListItem:
    out: MapRunListItem = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        out["execution_arn"] = ""
    if data.get("mapRunArn") is not None:
        out["map_run_arn"] = data["mapRunArn"]
    else:
        out["map_run_arn"] = ""
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        out["state_machine_arn"] = ""
    if data.get("startDate") is not None:
        import capo_sfn.types.timestamp

        out["start_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("stopDate") is not None:
        import capo_sfn.types.timestamp

        out["stop_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    return out
