"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeTaskResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.resource_status
    import capo_iotsitewise.types.task_configuration
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.workspace_name


class DescribeTaskResponse(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    task_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the task.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The description of the task.</p>"""
    task_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the task.</p>"""
    version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the task.</p>"""
    task_configuration: "capo_iotsitewise.types.task_configuration.TaskConfiguration"
    """<p>The task execution configuration. Contains a <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html">containerTaskConfiguration</a> for custom container workloads.</p>"""
    status: "capo_iotsitewise.types.resource_status.ResourceStatus"
    """<p>The current lifecycle status of the task.</p>"""
    created_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the task was created, in Unix epoch time.</p>"""
    updated_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the task was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTaskResponse) -> dict:
    out: dict = {}
    out["workspaceName"] = value["workspace_name"]
    out["taskName"] = value["task_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["taskArn"] = value["task_arn"]
    out["version"] = value["version"]
    import capo_iotsitewise.types.task_configuration

    out["taskConfiguration"] = capo_iotsitewise.types.task_configuration.serialize_json(
        value["task_configuration"]
    )
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


def deserialize_json(data: dict) -> DescribeTaskResponse:
    out: DescribeTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("taskName") is not None:
        out["task_name"] = data["taskName"]
    else:
        out["task_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("taskArn") is not None:
        out["task_arn"] = data["taskArn"]
    else:
        out["task_arn"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("taskConfiguration") is not None:
        import capo_iotsitewise.types.task_configuration

        out["task_configuration"] = (
            capo_iotsitewise.types.task_configuration.deserialize_json(
                data["taskConfiguration"]
            )
        )
    else:
        out["task_configuration"] = {"$unknown": {"name": ""}}
    if data.get("status") is not None:
        import capo_iotsitewise.types.resource_status

        out["status"] = capo_iotsitewise.types.resource_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DescribeTaskResponse.status required")
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


def redact_sensitive(value: DescribeTaskResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "task_configuration" in value:
        import capo_iotsitewise.types.task_configuration

        out["task_configuration"] = (
            capo_iotsitewise.types.task_configuration.redact_sensitive(
                value["task_configuration"]
            )
        )
    return out
