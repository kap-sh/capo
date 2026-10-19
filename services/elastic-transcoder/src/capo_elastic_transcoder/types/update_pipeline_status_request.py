"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#UpdatePipelineStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.id
    import capo_elastic_transcoder.types.pipeline_status


class UpdatePipelineStatusRequest(TypedDict, closed=True):
    id: "capo_elastic_transcoder.types.id.Id"
    """<p>The identifier of the pipeline to update.</p>"""
    status: "capo_elastic_transcoder.types.pipeline_status.PipelineStatus"
    """<p>The desired status of the pipeline:</p> <ul> <li> <p> <code>Active</code>: The pipeline is processing jobs.</p> </li> <li> <p> <code>Paused</code>: The pipeline is not currently processing jobs.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipelineStatusRequest) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> UpdatePipelineStatusRequest:
    out: UpdatePipelineStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
