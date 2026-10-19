"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.resource_status
    import capo_iotsitewise.types.version


class CreateTaskResponse(TypedDict, closed=True):
    task_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the created task.</p>"""
    task_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the created task.</p>"""
    version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the newly created task.</p>"""
    status: "capo_iotsitewise.types.resource_status.ResourceStatus"
    """<p>The current lifecycle status of the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTaskResponse) -> dict:
    out: dict = {}
    out["taskName"] = value["task_name"]
    out["taskArn"] = value["task_arn"]
    out["version"] = value["version"]
    import capo_iotsitewise.types.resource_status

    out["status"] = capo_iotsitewise.types.resource_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateTaskResponse:
    out: CreateTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("taskName") is not None:
        out["task_name"] = data["taskName"]
    else:
        out["task_name"] = ""
    if data.get("taskArn") is not None:
        out["task_arn"] = data["taskArn"]
    else:
        out["task_arn"] = ""
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
        raise DeserializationError("CreateTaskResponse.status required")
    return out
