"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PipelineSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.resource_status
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class PipelineSummary(TypedDict, closed=True):
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The description of the pipeline.</p>"""
    pipeline_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the pipeline.</p>"""
    version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the pipeline.</p>"""
    status: "capo_iotsitewise.types.resource_status.ResourceStatus"
    """<p>The current lifecycle status of the pipeline.</p>"""
    created_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the pipeline was created, in Unix epoch time.</p>"""
    updated_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the pipeline was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineSummary) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["pipelineArn"] = value["pipeline_arn"]
    out["version"] = value["version"]
    import capo_iotsitewise.types.resource_status

    out["status"] = capo_iotsitewise.types.resource_status.serialize_json(
        value["status"]
    )
    import capo_iotsitewise.types.timestamp

    out["createdAt"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_iotsitewise.types.timestamp

    out["updatedAt"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> PipelineSummary:
    out: PipelineSummary = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
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
        raise DeserializationError("PipelineSummary.status required")
    if data.get("createdAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["created_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["updated_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
