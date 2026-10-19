"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreatePipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.resource_status
    import capo_iotsitewise.types.version


class CreatePipelineResponse(TypedDict, closed=True):
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the created pipeline.</p>"""
    pipeline_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the created pipeline.</p>"""
    version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the newly created pipeline.</p>"""
    status: "capo_iotsitewise.types.resource_status.ResourceStatus"
    """<p>The current lifecycle status of the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipelineResponse) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["pipelineArn"] = value["pipeline_arn"]
    out["version"] = value["version"]
    import capo_iotsitewise.types.resource_status

    out["status"] = capo_iotsitewise.types.resource_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreatePipelineResponse:
    out: CreatePipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("pipelineArn") is not None:
        out["pipeline_arn"] = data["pipelineArn"]
    else:
        out["pipeline_arn"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.resource_status

        out["status"] = capo_iotsitewise.types.resource_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreatePipelineResponse.status required")
    return out
