"""Generated from Smithy shape ``com.amazonaws.pipes#StopPipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.pipe_arn
    import capo_pipes.types.pipe_name
    import capo_pipes.types.pipe_state
    import capo_pipes.types.requested_pipe_state
    import capo_pipes.types.timestamp


class StopPipeResponse(TypedDict, closed=True):
    arn: NotRequired["capo_pipes.types.pipe_arn.PipeArn"]
    """<p>The ARN of the pipe.</p>"""
    name: NotRequired["capo_pipes.types.pipe_name.PipeName"]
    """<p>The name of the pipe.</p>"""
    desired_state: NotRequired[
        "capo_pipes.types.requested_pipe_state.RequestedPipeState"
    ]
    """<p>The state the pipe should be in.</p>"""
    current_state: NotRequired["capo_pipes.types.pipe_state.PipeState"]
    """<p>The state the pipe is in.</p>"""
    creation_time: NotRequired["capo_pipes.types.timestamp.Timestamp"]
    """<p>The time the pipe was created.</p>"""
    last_modified_time: NotRequired["capo_pipes.types.timestamp.Timestamp"]
    """<p>When the pipe was last updated, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopPipeResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "desired_state" in value:
        out["DesiredState"] = value["desired_state"]
    if "current_state" in value:
        out["CurrentState"] = value["current_state"]
    if "creation_time" in value:
        import capo_pipes.types.timestamp

        out["CreationTime"] = capo_pipes.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_pipes.types.timestamp

        out["LastModifiedTime"] = capo_pipes.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> StopPipeResponse:
    out: StopPipeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DesiredState") is not None:
        out["desired_state"] = data["DesiredState"]
    if data.get("CurrentState") is not None:
        out["current_state"] = data["CurrentState"]
    if data.get("CreationTime") is not None:
        import capo_pipes.types.timestamp

        out["creation_time"] = capo_pipes.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_pipes.types.timestamp

        out["last_modified_time"] = capo_pipes.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
