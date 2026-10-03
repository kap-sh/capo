"""Generated from Smithy shape ``com.amazonaws.pipes#Pipe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.arn
    import capo_pipes.types.arn_or_url
    import capo_pipes.types.optional_arn
    import capo_pipes.types.pipe_arn
    import capo_pipes.types.pipe_name
    import capo_pipes.types.pipe_state
    import capo_pipes.types.pipe_state_reason
    import capo_pipes.types.requested_pipe_state
    import capo_pipes.types.timestamp


class Pipe(TypedDict, closed=True):
    name: NotRequired["capo_pipes.types.pipe_name.PipeName"]
    """<p>The name of the pipe.</p>"""
    arn: NotRequired["capo_pipes.types.pipe_arn.PipeArn"]
    """<p>The ARN of the pipe.</p>"""
    desired_state: NotRequired[
        "capo_pipes.types.requested_pipe_state.RequestedPipeState"
    ]
    """<p>The state the pipe should be in.</p>"""
    current_state: NotRequired["capo_pipes.types.pipe_state.PipeState"]
    """<p>The state the pipe is in.</p>"""
    state_reason: NotRequired["capo_pipes.types.pipe_state_reason.PipeStateReason"]
    """<p>The reason the pipe is in its current state.</p>"""
    creation_time: NotRequired["capo_pipes.types.timestamp.Timestamp"]
    """<p>The time the pipe was created.</p>"""
    last_modified_time: NotRequired["capo_pipes.types.timestamp.Timestamp"]
    """<p>When the pipe was last updated, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    source: NotRequired["capo_pipes.types.arn_or_url.ArnOrUrl"]
    """<p>The ARN of the source resource.</p>"""
    target: NotRequired["capo_pipes.types.arn.Arn"]
    """<p>The ARN of the target resource.</p>"""
    enrichment: NotRequired["capo_pipes.types.optional_arn.OptionalArn"]
    """<p>The ARN of the enrichment resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Pipe) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "desired_state" in value:
        out["DesiredState"] = value["desired_state"]
    if "current_state" in value:
        out["CurrentState"] = value["current_state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
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
    if "source" in value:
        out["Source"] = value["source"]
    if "target" in value:
        out["Target"] = value["target"]
    if "enrichment" in value:
        out["Enrichment"] = value["enrichment"]
    return out


def deserialize_json(data: dict) -> Pipe:
    out: Pipe = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("DesiredState") is not None:
        out["desired_state"] = data["DesiredState"]
    if data.get("CurrentState") is not None:
        out["current_state"] = data["CurrentState"]
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
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
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    if data.get("Enrichment") is not None:
        out["enrichment"] = data["Enrichment"]
    return out
